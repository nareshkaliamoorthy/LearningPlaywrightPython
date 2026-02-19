# LearningPlaywrightPython

Playwright Python test project containing page objects and tests for the OrangeHRM demo site.

Contents
- pages/: page object modules
- tests/: pytest test cases using Playwright
- auth/: credentials (auth.json) — DO NOT COMMIT sensitive credentials; this repo's .gitignore prevents that

Quick start
1. Create and activate a virtual environment (recommended):
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
2. Install dependencies:
   pip install -r requirements.txt
   (If there is no requirements.txt, install playwright and pytest: pip install playwright pytest)
3. Install Playwright browsers:
   python -m playwright install
4. Run tests:
   pytest -q

Notes
- Sensitive files like `auth/auth.json` are excluded via `.gitignore`.
- If you push to GitHub over HTTPS you'll need to authenticate (use a Personal Access Token) or configure SSH keys.

