"""
Setup utility for Mistral API key
This script helps you set up your Mistral API key for the Home Improvement Advisor
"""

import os
import sys
import streamlit as st

def main():
    """
    Simple utility to set up the Mistral API key
    """
    print("\n🏠 Home Improvement Advisor - API Setup 🏠\n")
    print("This utility will help you set up your Mistral AI API key")
    print("You can get your API key from https://mistral.ai\n")
    
    # Check if .env file exists
    env_file = ".env"
    env_exists = os.path.exists(env_file)
    
    if env_exists:
        print("An .env file already exists. Would you like to update it?")
        response = input("Enter [y/n]: ").strip().lower()
        if response != 'y':
            print("\nSetup cancelled. Your existing .env file was not modified.")
            return
    
    # Get the API key from user
    api_key = input("\nPlease enter your Mistral AI API key: ").strip()
    
    if not api_key:
        print("\nNo API key provided. Setup cancelled.")
        return
    
    # Write to .env file
    with open(env_file, 'w') as f:
        f.write(f"# Mistral AI API Key\n")
        f.write(f"MISTRAL_API_KEY={api_key}\n")
    
    print("\n✅ API key successfully saved to .env file!")
    print("\nYou can now run the Home Improvement Advisor with:")
    print("streamlit run app.py")
    
    # Ask if user wants to start the app now
    print("\nWould you like to start the app now?")
    start_now = input("Enter [y/n]: ").strip().lower()
    
    if start_now == 'y':
        print("\nStarting Home Improvement Advisor...")
        os.system("streamlit run app.py")
    else:
        print("\nYou can start the app later by running: streamlit run app.py")

if __name__ == "__main__":
    main()