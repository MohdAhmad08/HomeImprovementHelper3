# Deployment Guide for Home Improvement Advisor

This guide will help you deploy your Home Improvement Advisor application to Streamlit Cloud.

## Preparing Your Project for Deployment

### 1. Create a requirements.txt file
Streamlit Cloud needs this file to know which packages to install.

```bash
# Run this command in your terminal
echo "streamlit==1.32.0" > requirements.txt
echo "requests==2.31.0" >> requirements.txt
echo "python-dotenv==1.0.0" >> requirements.txt
```

### 2. Create a .gitignore file
To avoid uploading sensitive information to GitHub:

```bash
# Run this command in your terminal
echo ".env" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

### 3. Initialize Git repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit"
```

## Deploying to Streamlit Cloud

### 1. Create a GitHub Repository
- Go to [GitHub](https://github.com) and sign in
- Click on "New" to create a new repository
- Name it "home-improvement-advisor" or any name you prefer
- Make it public or private
- Do not initialize with README, .gitignore, or license
- Click "Create repository"

### 2. Push Your Code to GitHub
Follow the instructions provided by GitHub after creating the repository. It will be something like:

```bash
git remote add origin https://github.com/yourusername/home-improvement-advisor.git
git branch -M main
git push -u origin main
```

### 3. Deploy on Streamlit Cloud
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Sign in with your GitHub account
- Click "New app"
- Select your repository, branch (main), and main file (app.py)
- Under "Advanced settings":
  - Add a secret:
    - Key: MISTRAL_API_KEY
    - Value: Your Mistral API key
- Click "Deploy"

### 4. Access Your Deployed App
- Once deployed, Streamlit Cloud will provide a URL
- Your app will be publicly accessible at this URL
- Share it with others!

## Updating Your App

If you make changes to your code:

1. Commit your changes:
```bash
git add .
git commit -m "Description of changes"
```

2. Push to GitHub:
```bash
git push
```

3. Streamlit Cloud will automatically update your app with the new changes

## Troubleshooting

- If your app has errors, check the logs in Streamlit Cloud
- Make sure your MISTRAL_API_KEY is correctly set in Streamlit Cloud
- If you change your API key, update it in Streamlit Cloud's settings