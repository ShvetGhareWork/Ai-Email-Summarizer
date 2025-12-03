# 📧 AI Email Summarizer

**Automatically Summarizing Unread Gmail Emails Using AI**

> AWS AI for Bharat Challenge - Week 2: Lazy Automation

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 🎯 Problem Statement

### "I hate doing X..."

**I hate spending 30+ minutes every morning reading through dozens of emails just to figure out which ones are important!**

As professionals, we receive countless emails daily—newsletters, notifications, work updates, promotional content, and more. Manually reading through each email to determine its importance is:

- ⏰ **Time-consuming**: Takes 20-30 minutes daily
- 😫 **Mentally draining**: Requires constant context switching
- 📉 **Inefficient**: Important emails get buried in the noise
- 🔄 **Repetitive**: Same process every single day

**The Solution?** Automate email summarization using AI! Let artificial intelligence read your emails and provide concise, actionable summaries in seconds.

---

## ✨ Features

✅ **Automatic Gmail Connection** - Securely connects to Gmail using IMAP  
✅ **Unread Email Detection** - Fetches only unread emails  
✅ **Smart Content Extraction** - Handles multipart emails, HTML, and various encodings  
✅ **AI-Powered Summaries** - Uses Google Gemini to generate 3-5 bullet point summaries  
✅ **Markdown Export** - Saves all summaries in a clean `email_summaries.md` file  
✅ **Edge Case Handling** - Manages empty emails, HTML-only content, and encoding issues  
✅ **Clear Terminal Output** - Provides real-time progress updates  
✅ **Secure Configuration** - Uses `.env` file for sensitive credentials  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **IMAP** | Gmail email fetching protocol |
| **Google Gemini** | AI model for summarization |
| **python-dotenv** | Environment variable management |
| **html2text** | HTML to plain text conversion |

---

## 📋 Prerequisites

Before running this project, you need:

1. **Python 3.8 or higher** installed
2. **Gmail account** with IMAP enabled
3. **Gmail App Password** (not your regular password)
4. **Google Gemini API Key**

---

## 🔧 Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-summarizer.git
cd ai-email-summarizer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Enable Gmail IMAP

1. Go to [Gmail Settings](https://mail.google.com/mail/u/0/#settings/fwdandpop)
2. Click on **"Forwarding and POP/IMAP"** tab
3. Enable **"IMAP access"**
4. Click **"Save Changes"**

### Step 4: Generate Gmail App Password

⚠️ **Important**: You MUST use an App Password, not your regular Gmail password!

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (if not already enabled)
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Select **"Mail"** and **"Other (Custom name)"**
5. Enter "AI Email Summarizer" as the name
6. Click **"Generate"**
7. Copy the 16-character password (you'll use this in `.env`)

### Step 5: Get Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API key"**
4. Click **"Create API key in new project"** (or select existing project)
5. Copy the API key

### Step 6: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```env
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-16-char-app-password
   GEMINI_API_KEY=your-gemini-api-key
   ```

---

## 🚀 Running the Script

Simply run:

```bash
python automate.py
```

### Expected Output:

```
============================================================
AI Email Summarizer - AWS AI for Bharat Challenge Week 2
============================================================

🔄 Connecting to Gmail...
✔ Connected to Gmail successfully!
🔍 Searching for unread emails...
✔ Found 5 unread email(s)

📧 Processing email 1/5...
   Subject: Weekly Newsletter - AI Trends
   🤖 Generating AI summary...
   ✔ Summary generated!

📧 Processing email 2/5...
   Subject: Meeting Reminder: Project Sync
   🤖 Generating AI summary...
   ✔ Summary generated!

...

✔ All summaries saved to email_summaries.md
✔ Processed 5 email(s) successfully!
✔ Disconnected from Gmail

============================================================
Process completed!
============================================================
```

---

## 📄 Sample Output

The script generates `email_summaries.md` with content like:

```markdown
# Email Summaries

Generated on: 2025-12-03 19:43:48

---

## Email 1

**From:** newsletter@aitrends.com  
**Date:** Tue, 3 Dec 2025 10:30:00 +0530  
**Subject:** Weekly Newsletter - AI Trends

**Summary:**
- Latest developments in Large Language Models (LLMs)
- New GPT-4 features announced by OpenAI
- Upcoming AI conference in Bangalore next month
- Free webinar on prompt engineering this Friday

---

## Email 2

**From:** manager@company.com  
**Date:** Tue, 3 Dec 2025 14:15:00 +0530  
**Subject:** Meeting Reminder: Project Sync

**Summary:**
- Project sync meeting scheduled for tomorrow at 3 PM
- Agenda includes Q4 roadmap discussion
- Please prepare status updates for your tasks
- Meeting link will be shared 10 minutes before

---
```

---

## 📁 Project Structure

```
ai-email-summarizer/
│
├── automate.py              # Main automation script
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your actual credentials (gitignored)
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── email_summaries.md      # Generated summaries (gitignored)
│
├── .kiro/                  # Kiro AI assistant metadata
│   ├── kiro.json          # Project configuration
│   └── logs.txt           # Development logs
│
├── screenshots/            # Screenshots for documentation
│   ├── terminal_output.png
│   ├── gmail_setup.png
│   └── summary_example.png
│
└── blog/                   # AWS Builder Center blog draft
    └── blog_post.md
```

---

## 🖼️ Screenshots

### Terminal Output
![Terminal Output](screenshots/terminal_output.png)
*Real-time progress updates while processing emails*

### Gmail IMAP Setup
![Gmail Setup](screenshots/gmail_setup.png)
*Enabling IMAP access in Gmail settings*

### Generated Summary
![Summary Example](screenshots/summary_example.png)
*AI-generated email summaries in Markdown format*

---

## 🤖 How Kiro Helped Accelerate Development

This project was built with assistance from **Kiro**, an AI-powered development assistant. Here's how Kiro accelerated the development process:

### 🚀 Rapid Prototyping
- **Time Saved**: ~4 hours
- Kiro helped scaffold the entire project structure in minutes
- Generated boilerplate code for IMAP connection and email parsing
- Suggested best practices for handling multipart emails

### 🐛 Debugging Assistance
- **Time Saved**: ~2 hours
- Identified encoding issues with non-UTF-8 emails
- Suggested using `html2text` for HTML email conversion
- Helped implement proper error handling for edge cases

### 📝 Documentation
- **Time Saved**: ~1.5 hours
- Generated comprehensive README with setup instructions
- Created clear examples and troubleshooting guides
- Formatted markdown for better readability

### 💡 Best Practices
- Recommended using App Passwords instead of regular passwords
- Suggested environment variable management with `python-dotenv`
- Advised on API token limits and email body truncation
- Helped structure code with proper functions and error handling

### Total Development Time
- **Without Kiro**: Estimated 12-15 hours
- **With Kiro**: Actual 4-5 hours
- **Time Saved**: ~70% faster development! 🎉

---

## 🔒 Security Notes

⚠️ **Never commit your `.env` file to Git!**

- The `.env` file contains sensitive credentials
- Always use `.env.example` as a template
- Add `.env` to `.gitignore` (already included)
- Use App Passwords, not your main Gmail password

---

## 🐛 Troubleshooting

### Issue: "Failed to connect to Gmail"
**Solution**: Make sure you're using an App Password, not your regular password. Enable 2FA and generate a new App Password.

### Issue: "No unread emails found"
**Solution**: This is normal if you have no unread emails. Send yourself a test email to verify the script works.

### Issue: "OpenAI API error"
**Solution**: Check that your API key is correct and you have credits available in your OpenAI account.

### Issue: "Empty message body"
**Solution**: Some emails may only contain images or attachments. The script will skip these and continue processing others.

---

## 🎯 Future Enhancements

- [ ] Support for multiple email providers (Outlook, Yahoo)
- [ ] Email categorization (work, personal, promotional)
- [ ] Priority scoring for emails
- [ ] Automatic email responses for common queries
- [ ] Web dashboard for viewing summaries
- [ ] Scheduled automation (run every hour/day)
- [ ] Integration with task management tools

---

## 📜 License

MIT License - feel free to use this project for personal or commercial purposes.

---

## 👨‍💻 Author

Built for **AWS AI for Bharat Challenge - Week 2: Lazy Automation**

---

## 🙏 Acknowledgments

- **Google** for the Gemini API
- **AWS AI for Bharat** for the challenge inspiration
- **Kiro AI** for development acceleration
- The Python community for excellent libraries

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the [Gmail Setup](#step-3-enable-gmail-imap) instructions
3. Open an issue on GitHub
4. Contact: your-email@example.com

---

**⭐ If you found this project helpful, please give it a star on GitHub!**
#
