# 🚀 Complete Setup Guide - AI Email Summarizer

This guide will walk you through every step needed to get the AI Email Summarizer running on your machine.

---

## 📋 Prerequisites Checklist

Before starting, make sure you have:

- [ ] Python 3.8 or higher installed
- [ ] A Gmail account
- [ ] Internet connection
- [ ] Text editor (VS Code, Notepad++, etc.)
- [ ] Command line/terminal access

---

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

### macOS
```bash
brew install python3
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## Step 2: Download the Project

### Option A: Using Git
```bash
git clone https://github.com/yourusername/ai-email-summarizer.git
cd ai-email-summarizer
```

### Option B: Download ZIP
1. Go to the GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed python-dotenv-1.0.0 openai-1.54.0 html2text-2024.2.26
```

---

## Step 4: Enable Gmail IMAP

### 4.1 Enable IMAP Access

1. Go to [Gmail](https://mail.google.com)
2. Click the ⚙️ gear icon → "See all settings"
3. Click "Forwarding and POP/IMAP" tab
4. Under "IMAP access", select **"Enable IMAP"**
5. Click "Save Changes"

![Gmail IMAP Settings](screenshots/gmail_imap.png)

---

## Step 5: Generate Gmail App Password

⚠️ **CRITICAL**: You MUST use an App Password, NOT your regular Gmail password!

### 5.1 Enable 2-Factor Authentication (if not already enabled)

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Under "Signing in to Google", click "2-Step Verification"
3. Follow the prompts to set it up

### 5.2 Generate App Password

1. Go to [App Passwords](https://myaccount.google.com/apppasswords)
2. You may need to sign in again
3. Under "Select app", choose **"Mail"**
4. Under "Select device", choose **"Other (Custom name)"**
5. Enter: `AI Email Summarizer`
6. Click **"Generate"**
7. You'll see a 16-character password like: `abcd efgh ijkl mnop`
8. **COPY THIS PASSWORD** - you'll need it in the next step
9. Click "Done"

![App Password Generation](screenshots/app_password.png)

⚠️ **Note**: You won't be able to see this password again, so copy it now!

---

## Step 6: Get Google Gemini API Key

### 6.1 Access Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Accept the terms of service if prompted

### 6.2 Generate API Key

1. Click **"Get API key"** in the left sidebar
2. Click **"Create API key in new project"** (or select an existing project)
3. **COPY THE KEY** immediately
4. Store it safely - you can retrieve it later from the API keys page

![Gemini API Key](screenshots/gemini_key.png)

### 6.3 Free Tier

- Gemini API has a generous free tier
- 15 requests per minute for Gemini 1.5 Flash
- No credit card required for free tier
- Perfect for this email summarization use case

---

## Step 7: Configure Environment Variables

### 7.1 Create .env File

```bash
cp .env.example .env
```

### 7.2 Edit .env File

Open `.env` in a text editor and fill in your credentials:

```env
# Gmail Configuration
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop

# Google Gemini API Configuration
GEMINI_API_KEY=your-gemini-api-key-here
```

**Replace:**
- `your-email@gmail.com` → Your actual Gmail address
- `abcd efgh ijkl mnop` → The 16-character App Password (remove spaces)
- `your-gemini-api-key-here` → Your Google Gemini API key

### 7.3 Save and Close

⚠️ **Security**: Never share your `.env` file or commit it to Git!

---

## Step 8: Test the Setup

### 8.1 Send Yourself a Test Email

1. From another email account (or the same one), send yourself an email
2. Make sure it's unread in your Gmail inbox

### 8.2 Run the Script

```bash
python automate.py
```

### 8.3 Expected Output

```
============================================================
AI Email Summarizer - AWS AI for Bharat Challenge Week 2
============================================================

🔄 Connecting to Gmail...
✔ Connected to Gmail successfully!
🔍 Searching for unread emails...
✔ Found 1 unread email(s)

📧 Processing email 1/1...
   Subject: Test Email
   🤖 Generating AI summary...
   ✔ Summary generated!

✔ All summaries saved to email_summaries.md
✔ Processed 1 email(s) successfully!
✔ Disconnected from Gmail

============================================================
Process completed!
============================================================
```

### 8.4 Check the Output

Open `email_summaries.md` to see your email summary!

---

## 🐛 Troubleshooting

### Error: "Failed to connect to Gmail"

**Possible causes:**
1. Using regular password instead of App Password
2. IMAP not enabled
3. Incorrect email address

**Solutions:**
- Double-check you're using the 16-character App Password
- Verify IMAP is enabled in Gmail settings
- Make sure EMAIL_ADDRESS in .env is correct

---

### Error: "No module named 'dotenv'"

**Cause**: Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt
```

---

### Error: "Gemini API error"

**Possible causes:**
1. Invalid API key
2. API quota exceeded
3. Network issues

**Solutions:**
- Verify your API key in .env
- Check your API quota in Google AI Studio
- Check your internet connection

---

### Error: "No unread emails found"

**This is not an error!** It means you have no unread emails.

**Solution**: Send yourself a test email and run the script again.

---

### Error: "Empty message body"

**Cause**: Some emails only contain images or attachments

**Solution**: This is normal. The script will skip these and continue with other emails.

---

## 🎯 Next Steps

Now that everything is set up:

1. ✅ Let unread emails accumulate
2. ✅ Run `python automate.py` whenever you want summaries
3. ✅ Read `email_summaries.md` instead of individual emails
4. ✅ Save 30 minutes every day!

---

## 🔄 Regular Usage

### Daily Workflow

1. Open terminal in project folder
2. Run:
   ```bash
   python automate.py
   ```
3. Open `email_summaries.md`
4. Read summaries instead of full emails
5. Only open important emails in Gmail

### Automation (Optional)

You can schedule the script to run automatically:

**Windows (Task Scheduler)**:
- Create a task that runs `python C:\path\to\automate.py` daily

**macOS/Linux (cron)**:
```bash
# Edit crontab
crontab -e

# Add this line to run daily at 9 AM
0 9 * * * cd /path/to/ai-email-summarizer && python automate.py
```

---

## 📊 Cost Estimation

### Google Gemini API Costs

- **Model**: Gemini 1.5 Flash
- **Free Tier**: 15 requests per minute
- **Cost**: FREE for most personal use cases
- **Paid tier**: $0.00001875 per 1K characters (if you exceed free tier)

**Monthly estimate** (50 emails/day):
- 50 emails × 30 days = 1,500 emails
- **Cost**: **FREE** (within free tier limits)

💡 **Tip**: Gemini 1.5 Flash is perfect for this use case and completely free for personal use!

---

## 🔒 Security Best Practices

1. ✅ Never commit `.env` to Git
2. ✅ Use App Passwords, not regular passwords
3. ✅ Rotate API keys periodically
4. ✅ Don't share your `email_summaries.md` if it contains sensitive info
5. ✅ Keep your Python packages updated

---

## 🆘 Still Having Issues?

1. Check the [README.md](README.md) troubleshooting section
2. Review this guide step-by-step
3. Open an issue on GitHub
4. Contact: your-email@example.com

---

**🎉 Congratulations! You're now ready to automate your email workflow!**
