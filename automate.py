"""
AI Email Summarizer - Automatically Summarizing Unread Gmail Emails Using AI

This script connects to Gmail via IMAP, fetches unread emails, and uses
OpenAI's GPT model to generate concise summaries of each email.

Author: AWS AI for Bharat Challenge - Week 2
"""

import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv
import google.generativeai as genai
import html2text
from datetime import datetime

# Load environment variables
load_dotenv()

# Configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initialize HTML to text converter
html_converter = html2text.HTML2Text()
html_converter.ignore_links = False
html_converter.ignore_images = True


def connect_to_gmail():
    """
    Establishes a secure connection to Gmail using IMAP.
    
    Returns:
        imaplib.IMAP4_SSL: Connected IMAP client
    """
    try:
        print("🔄 Connecting to Gmail...")
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("✔ Connected to Gmail successfully!")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"❌ Failed to connect to Gmail: {e}")
        print("💡 Make sure you're using an App Password, not your regular password")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def decode_email_subject(subject):
    """
    Decodes email subject handling different encodings.
    
    Args:
        subject: Raw email subject
        
    Returns:
        str: Decoded subject string
    """
    if subject is None:
        return "No Subject"
    
    decoded_parts = decode_header(subject)
    decoded_subject = ""
    
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            try:
                decoded_subject += part.decode(encoding or 'utf-8', errors='ignore')
            except:
                decoded_subject += part.decode('utf-8', errors='ignore')
        else:
            decoded_subject += str(part)
    
    return decoded_subject


def extract_email_body(msg):
    """
    Extracts plain text body from email, handling multipart messages.
    
    Args:
        msg: Email message object
        
    Returns:
        str: Extracted email body text
    """
    body = ""
    
    if msg.is_multipart():
        # Handle multipart emails
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            
            # Skip attachments
            if "attachment" in content_disposition:
                continue
            
            try:
                part_body = part.get_payload(decode=True)
                if part_body is None:
                    continue
                
                # Try to decode with the specified charset
                charset = part.get_content_charset() or 'utf-8'
                part_body = part_body.decode(charset, errors='ignore')
                
                # Prefer plain text
                if content_type == "text/plain":
                    body = part_body
                    break
                # Convert HTML to plain text if no plain text available
                elif content_type == "text/html" and not body:
                    body = html_converter.handle(part_body)
            except Exception as e:
                print(f"⚠ Warning: Could not decode part - {e}")
                continue
    else:
        # Handle simple non-multipart emails
        try:
            payload = msg.get_payload(decode=True)
            if payload:
                charset = msg.get_content_charset() or 'utf-8'
                body = payload.decode(charset, errors='ignore')
                
                # Convert HTML to text if needed
                if msg.get_content_type() == "text/html":
                    body = html_converter.handle(body)
        except Exception as e:
            print(f"⚠ Warning: Could not decode message - {e}")
    
    # Clean up the body
    body = body.strip()
    
    # Limit body length for API (max ~3000 chars to stay within token limits)
    if len(body) > 3000:
        body = body[:3000] + "... [truncated]"
    
    return body if body else "Empty message body"


def generate_summary(subject, body):
    """
    Uses Google Gemini to generate a concise summary of the email.
    
    Args:
        subject: Email subject
        body: Email body text
        
    Returns:
        str: AI-generated summary in bullet points
    """
    try:
        prompt = f"""Summarize the following email in 3-5 concise bullet points. 
Focus on key information, action items, and important details.

Subject: {subject}

Body:
{body}

Provide the summary as bullet points (use - for bullets)."""

        response = model.generate_content(prompt)
        summary = response.text.strip()
        return summary
    
    except Exception as e:
        print(f"⚠ Warning: Could not generate summary - {e}")
        return "- Summary generation failed"


def fetch_and_summarize_emails(limit=10):
    """
    Main function to fetch unread emails and generate summaries.
    
    Args:
        limit: Maximum number of emails to process (default: 10)
    """
    # Validate environment variables
    if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, GEMINI_API_KEY]):
        print("❌ Error: Missing environment variables!")
        print("Please ensure EMAIL_ADDRESS, EMAIL_PASSWORD, and GEMINI_API_KEY are set in .env file")
        return
    
    # Connect to Gmail
    mail = connect_to_gmail()
    if not mail:
        return
    
    try:
        # Select inbox
        mail.select('inbox')
        
        # Search for unread emails
        print("🔍 Searching for unread emails...")
        status, messages = mail.search(None, 'UNSEEN')
        
        if status != 'OK':
            print("❌ Failed to search for emails")
            return
        
        email_ids = messages[0].split()
        
        if not email_ids:
            print("✔ No unread emails found!")
            return
        
        total_unread = len(email_ids)
        print(f"✔ Found {total_unread} unread email(s)")
        
        # Limit to specified number of emails
        if limit and total_unread > limit:
            email_ids = email_ids[:limit]
            print(f"📊 Processing only the first {limit} emails (to process all, modify the limit parameter)")
        
        # Prepare output file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        summaries = [f"# Email Summaries\n\nGenerated on: {timestamp}\n\n---\n\n"]
        
        # Process each email
        for i, email_id in enumerate(email_ids, 1):
            print(f"\n📧 Processing email {i}/{len(email_ids)}...")
            
            # Fetch email
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            
            if status != 'OK':
                print(f"⚠ Warning: Could not fetch email {i}")
                continue
            
            # Parse email
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            # Extract subject
            subject = decode_email_subject(msg['Subject'])
            sender = msg['From']
            date = msg['Date']
            
            print(f"   Subject: {subject[:50]}...")
            
            # Extract body
            body = extract_email_body(msg)
            
            if not body or body == "Empty message body":
                print("   ⚠ Warning: Empty email body, skipping...")
                continue
            
            # Generate summary
            print("   🤖 Generating AI summary...")
            summary = generate_summary(subject, body)
            
            # Format summary for markdown
            email_summary = f"""## Email {i}

**From:** {sender}  
**Date:** {date}  
**Subject:** {subject}

**Summary:**
{summary}

---

"""
            summaries.append(email_summary)
            print("   ✔ Summary generated!")
        
        # Save summaries to file
        output_file = "email_summaries.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(summaries)
        
        print(f"\n✔ All summaries saved to {output_file}")
        print(f"✔ Processed {len(summaries) - 1} email(s) successfully!")
        
    except Exception as e:
        print(f"❌ Error during email processing: {e}")
    
    finally:
        # Close connection
        try:
            mail.close()
            mail.logout()
            print("✔ Disconnected from Gmail")
        except:
            pass


if __name__ == "__main__":
    print("=" * 60)
    print("AI Email Summarizer - AWS AI for Bharat Challenge Week 2")
    print("=" * 60)
    print()
    
    fetch_and_summarize_emails()
    
    print("\n" + "=" * 60)
    print("Process completed!")
    print("=" * 60)
