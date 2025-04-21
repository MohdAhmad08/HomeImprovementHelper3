# Deployment Guide for Home Improvement Advisor

This guide will help you deploy your Home Improvement Advisor application to Streamlit Cloud.

## Required Files for Deployment

Your project already contains all the necessary files for deployment:

1. **Main application file**: `app.py`
2. **Utility file**: `mistral_utils.py`
3. **Configuration file**: `.streamlit/config.toml`
4. **Deployment theme configuration**: `.streamlit/config.cloud.toml`

For Streamlit Cloud to correctly determine the required packages, Streamlit will detect these packages automatically from your imports. For this project, the main packages are:
- streamlit
- requests
- python-dotenv

## Deploying to Streamlit Cloud

### 1. Create a GitHub Repository
- Go to [GitHub](https://github.com) and sign in
- Click on "New" to create a new repository
- Name it "home-improvement-advisor" or any name you prefer
- Make it public or private
- Do not initialize with README, .gitignore, or license
- Click "Create repository"

### 2. Push Your Code to GitHub
Follow the instructions provided by GitHub after creating the repository:

```bash
# Initialize a Git repository if you haven't already
git init

# Add your files
git add .

# Don't include the .env file with your API key
git rm --cached .env

# Commit your changes
git commit -m "Initial commit"

# Add the remote repository
git remote add origin https://github.com/yourusername/home-improvement-advisor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Deploy on Streamlit Cloud
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Sign in with your GitHub account
- Click "New app"
- Select your repository, branch (main), and main file (`app.py`)
- Under "Advanced settings":
  - Add a secret:
    - Key: `MISTRAL_API_KEY`
    - Value: Your Mistral API key
- Click "Deploy"

### 4. Verify Configuration
- Once deployed, Streamlit Cloud will use its default port configuration
- Your `.streamlit/config.cloud.toml` will be used for theming
- The app will automatically handle the API key via the Streamlit secrets management

### 5. Access Your Deployed App
- Once deployed, Streamlit Cloud will provide a URL
- Your app will be publicly accessible at this URL
- Share it with others!

## Troubleshooting

### Connection Refused Error
If you see "connection refused" errors in the logs:
- This is likely due to a port configuration issue
- Make sure your app is not hardcoded to use a specific port
- For local development, stick with `app.py --server.port 5000`
- For Streamlit Cloud, it will manage ports automatically

### API Key Issues
- If the app can't find your API key, check that it's correctly set in Streamlit Cloud's secret management
- You can update the API key in Streamlit Cloud settings if needed

### Deployment Failed
If deployment fails:
- Check the logs in Streamlit Cloud
- Ensure all required files (`app.py`, `mistral_utils.py`) are included in your GitHub repository
- Verify that your GitHub repository is accessible to Streamlit Cloud

### Package Installation Issues
- Streamlit Cloud should automatically detect and install the required packages
- If you encounter package-related errors, consider adding a `requirements.txt` file to your GitHub repository with:
  ```
  streamlit>=1.32.0
  requests>=2.31.0
  python-dotenv>=1.0.0
  ```