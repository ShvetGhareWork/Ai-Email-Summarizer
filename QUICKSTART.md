# 🚀 Quick Start - AI Email Summarizer

**Get up and running in 5 minutes!**

---

## Prerequisites

- Python 3.8+
- Gmail account
- Google Gemini API key (FREE)

---

## Installation

```bash
# 1. Clone repository
git clone https://github.com/yourusername/ai-email-summarizer.git
cd ai-email-summarizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure credentials
cp .env.example .env
# Edit .env with your credentials
```

---

## Configuration

Edit `.env`:

```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
GEMINI_API_KEY=your-gemini-key
```

**Get Gemini Key**: [Google AI Studio](https://aistudio.google.com/)

---

## Usage

```bash
python automate.py
```

**Output**: `email_summaries.md`

---

## Example Output

```markdown
## Email 1

**From:** newsletter@example.com
**Subject:** Weekly AI Updates

**Summary:**
- New GPT-4 features announced
- Upcoming AI conference in March
- Free webinar on prompt engineering
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection failed | Use App Password, not regular password |
| No emails found | Normal if inbox is empty |
| API error | Check Gemini API key in Google AI Studio |

---

## Need Help?

📖 [Full Documentation](README.md)  
🔧 [Setup Guide](SETUP_GUIDE.md)  
📁 [Project Structure](PROJECT_STRUCTURE.md)

---

**Time saved: 30 minutes/day** ⏰  
**Cost: FREE** 💰 (Gemini free tier)
