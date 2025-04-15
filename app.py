import os
import streamlit as st
from mistral_utils import get_mistral_response

# Configure page
st.set_page_config(
    page_title="Home Improvement Advisor",
    page_icon="🏠",
    layout="wide"
)

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Home Improvement Advisor. How can I help you with your renovation or DIY projects today?"}
    ]

def main():
    # App header
    st.title("🏠 Home Improvement Advisor")
    st.markdown("""
    Get personalized advice for home renovation, repairs, and DIY projects.
    Ask me about:
    - Planning renovations
    - Fixing common household issues
    - DIY project ideas and guidance
    - Material selection and cost estimates
    - Tools and techniques for home improvements
    """)
    
    # Check if Mistral API key is available
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        st.error("""
        Mistral AI API key not found. Please set the MISTRAL_API_KEY environment variable.
        
        You can do this by:
        1. Creating a .env file with MISTRAL_API_KEY=your_api_key
        2. Or setting it directly in your environment
        """)
        return
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # User input
    user_input = st.chat_input("Ask about your home improvement project...", key="home_improvement_input")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message in chat
        with st.chat_message("user"):
            st.write(user_input)
        
        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.text("Thinking...")
            
            # Prepare context by formatting the conversation history
            try:
                # Get response from Mistral AI
                response = get_mistral_response(
                    user_input, 
                    st.session_state.messages[:-1]  # Exclude the latest user message
                )
                
                # Update chat with response
                message_placeholder.write(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                message_placeholder.error(f"Error getting response: {str(e)}")
    
    # Add sidebar with information
    with st.sidebar:
        st.title("About")
        st.markdown("""
        ## Home Improvement Advisor
        
        This chatbot helps you with:
        - Home renovation advice
        - DIY project guidance
        - Repair tips and instructions
        - Material selection
        - Tool recommendations
        
        Powered by Mistral AI
        """)
        
        # Add a clear conversation button
        if st.button("Clear Conversation"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Hello! I'm your Home Improvement Advisor. How can I help you with your renovation or DIY projects today?"}
            ]
            st.rerun()

if __name__ == "__main__":
    main()
