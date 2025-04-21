#!/bin/bash

# Script to export the Home Improvement Advisor for deployment

echo "🏠 Preparing Home Improvement Advisor for deployment 🏠"

# Create deployment directory if it doesn't exist
DEPLOY_DIR="deployment_package"
mkdir -p $DEPLOY_DIR

# Copy required files
echo "Copying files to $DEPLOY_DIR..."
cp app.py $DEPLOY_DIR/
cp mistral_utils.py $DEPLOY_DIR/
cp README.md $DEPLOY_DIR/
cp -r .streamlit $DEPLOY_DIR/
cp .gitignore $DEPLOY_DIR/

# Create requirements.txt for Streamlit Cloud
echo "Creating requirements.txt..."
cat > $DEPLOY_DIR/requirements.txt << EOL
streamlit>=1.32.0
requests>=2.31.0
python-dotenv>=1.0.0
EOL

# Create empty .env file as placeholder
echo "Creating placeholder .env file..."
cat > $DEPLOY_DIR/.env.example << EOL
# Mistral AI API Key (required)
# Obtain your API key from https://mistral.ai
MISTRAL_API_KEY=your_mistral_api_key_here
EOL

echo "✅ Deployment package created successfully in $DEPLOY_DIR"
echo "⚠️ Remember to set up your MISTRAL_API_KEY in Streamlit Cloud's secrets manager!"
echo ""
echo "Next steps:"
echo "1. Copy these files to your GitHub repository"
echo "2. Deploy to Streamlit Cloud using app.py as the main file"
echo "3. Add MISTRAL_API_KEY to Streamlit Cloud's secrets"

# Make the script executable
chmod +x git_export.sh