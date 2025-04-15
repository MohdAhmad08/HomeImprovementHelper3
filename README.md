# 🏠 Home Improvement Advisor

A Streamlit-based chatbot that provides personalized advice for home renovation, repairs, and DIY projects using the Mistral AI API.

## Features

- Interactive chat interface for home improvement questions
- Personalized advice for DIY projects and renovations
- Material recommendations and cost estimates
- Step-by-step instructions for common repairs
- Tool recommendations and techniques

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- A Mistral AI API key from [mistral.ai](https://mistral.ai)

### Quick Setup

1. **Clone or download this repository**

2. **Set up your Mistral AI API key**
   
   Run the setup utility:
   ```
   python setup_api.py
   ```
   
   This will guide you through adding your API key to the .env file.

   Alternatively, you can manually create a `.env` file with:
   ```
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

3. **Install required packages**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```
   streamlit run app.py
   ```

## Usage

Once the application is running, you can:

1. Type your home improvement questions in the chat input
2. Get detailed responses from the AI advisor
3. Ask follow-up questions to get more specific advice
4. Clear the conversation using the button in the sidebar

## Example Questions

- "How do I fix a leaky faucet?"
- "What's the best flooring option for a kitchen renovation?"
- "How much would it cost to renovate a small bathroom?"
- "What tools do I need to build a basic bookshelf?"
- "How do I properly insulate my attic?"

## Deployment

This application can be easily deployed on Streamlit Cloud or any other platform that supports Streamlit applications.

## License

This project is open source and available under the MIT License.