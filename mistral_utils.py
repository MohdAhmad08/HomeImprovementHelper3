import os
import json
import requests

def get_mistral_response(user_query, conversation_history=[]):
    """
    Get a response from Mistral AI for a home improvement query
    
    Args:
        user_query (str): The user's input query
        conversation_history (list): Previous messages in the conversation
        
    Returns:
        str: The response from Mistral AI
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("Mistral API key not found. Please set the MISTRAL_API_KEY environment variable.")
    
    # Prepare the conversation history in the format Mistral expects
    messages = []
    
    # Add system message with home improvement context
    messages.append({
        "role": "system",
        "content": """You are a knowledgeable Home Improvement Advisor, specializing in home renovation, 
        DIY projects, repairs, and home maintenance. Provide detailed, practical advice for homeowners 
        of all skill levels. Include step-by-step instructions, tool recommendations, material suggestions, 
        and safety precautions when relevant. If you're uncertain about specific local building codes or 
        regulations, remind the user to check with local authorities. For complex or potentially dangerous 
        projects, suggest when it might be better to hire a professional."""
    })
    
    # Add conversation history
    for message in conversation_history:
        # Only include user and assistant messages, not system messages
        if message["role"] in ["user", "assistant"]:
            messages.append({"role": message["role"], "content": message["content"]})
    
    # Add the current user query
    messages.append({"role": "user", "content": user_query})
    
    # Configure the API request
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Use the mistral-medium model for a good balance of quality and speed
    payload = {
        "model": "mistral-medium",  # Choose appropriate model
        "messages": messages,
        "temperature": 0.7,  # Slightly creative but still focused
        "max_tokens": 1024,  # Allow for detailed responses
        "top_p": 0.9
    }
    
    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    
    # Check for API errors
    if response.status_code != 200:
        error_message = f"API request failed with status code {response.status_code}: {response.text}"
        raise Exception(error_message)
    
    # Extract and return the text response
    try:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        raise Exception(f"Failed to parse API response: {str(e)}")
