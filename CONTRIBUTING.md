# Contributing to AI Email Summarizer

Thank you for your interest in contributing to the AI Email Summarizer project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Error messages (if any)

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- Clear description of the feature
- Use case / problem it solves
- Proposed implementation (if you have ideas)

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Include comments for complex logic
- Keep functions focused and small

### Testing

Before submitting a PR:
- Test with multiple email types (plain text, HTML, multipart)
- Test edge cases (empty emails, encoding issues)
- Verify the script runs without errors

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/ai-email-summarizer.git
cd ai-email-summarizer

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your credentials

# Run the script
python automate.py
```

## Future Enhancement Ideas

- [ ] Support for multiple email providers (Outlook, Yahoo)
- [ ] Email categorization (work, personal, promotional)
- [ ] Priority scoring
- [ ] Web dashboard
- [ ] Scheduled automation
- [ ] Email response suggestions
- [ ] Integration with task management tools
- [ ] Support for other AI models (Claude, Gemini)

## Questions?

Feel free to open an issue for any questions!

---

**Thank you for contributing!** 🙏
