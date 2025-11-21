```markdown
# Streamlit Deploy Demo

This repository contains a minimal Streamlit app (app.py) you can deploy to Streamlit Cloud (https://share.streamlit.io).

## What is included
- app.py — minimal Streamlit application
- requirements.txt — Python dependencies

## How to deploy to Streamlit Cloud
1. Commit and push these files to your GitHub repository (e.g., Brandnn/test). Make the repo public or ensure your Streamlit account can access it.
2. Go to https://share.streamlit.io and log in with your GitHub account.
3. Click "New app" → select your repository (Brandnn/test), choose the branch (e.g., main), and set the main file path to `app.py`.
4. Click "Deploy". Streamlit Cloud will install dependencies from requirements.txt and start the app.
5. To update the app, push changes to the specified branch; Streamlit Cloud will rebuild the app automatically.

## Run locally
1. Create and activate a virtualenv (recommended).
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py

## Notes
- If you need secrets (API keys, tokens), use the Streamlit Cloud secrets manager or `.streamlit/secrets.toml` locally — do not commit secrets to the repo.
- If you want a custom theme or server settings, add `.streamlit/config.toml`.

If you want, I can also add a simple GitHub Actions workflow to run tests or lint on push, or prepare a `.streamlit/config.toml` with recommended settings.
```
