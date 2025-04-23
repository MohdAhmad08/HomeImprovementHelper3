import os
import streamlit as st
from mistral_utils import get_mistral_response

# Configure page
st.set_page_config(
    page_title="Home Improvement Advisor",
    page_icon="🏠",
    layout="wide"
)

# Keywords to check if input is related to home improvement
HOME_KEYWORDS = ["home", "renovation", "repair", "paint", "plumbing", "tools", "flooring", "DIY", "kitchen", "bathroom", "interior", "maintenance"]

def is_home_improvement_query(query):
    return any(keyword in query.lower() for keyword in HOME_KEYWORDS)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and expert home improvement advisor. You only answer questions strictly related to home renovation, repair, DIY projects, tools, and materials. Politely refuse to answer unrelated questions."},
        {"role": "assistant", "content": "Hello! I'm your Home Improvement Advisor. How can I help you with your renovation or DIY projects today?"}
    ]

def main():
    st.title("🏠 Home Improvement Advisor")
    st.markdown("""
    Get personalized advice for home renovation, repairs, and DIY projects.
    """)

    # Developer info
    st.markdown("---")
    st.markdown("### Developed by:")
    st.markdown("- **Mohd Ahmad** (12321720)")
    st.markdown("- **Supriyo Tandi** (12326766)")
    st.markdown("---")
    
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        st.error("Mistral AI API key not found.")
        return

    # Show chat history
    for message in st.session_state.messages[1:]:  # Skip system message
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Ask about your home improvement project...", key="home_improvement_input")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.text("Thinking...")

            if not is_home_improvement_query(user_input):
                response = "I'm designed to help only with home improvement topics like renovations, DIY, repairs, and tools. Please ask something related to that!"
            else:
                try:
                    response = get_mistral_response(
                        user_input,
                        st.session_state.messages[:-1]
                    )
                except Exception as e:
                    response = f"Error getting response: {str(e)}"

            message_placeholder.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    with st.sidebar:
        st.title("About")
        st.markdown("This chatbot helps with home renovation advice, DIY guidance, and repairs.")
        if st.button("Clear Conversation"):
            st.session_state.messages = [
                {"role": "system", "content": "You are a helpful and expert home improvement advisor. You only answer questions strictly related to home renovation, repair, DIY projects, tools, and materials. Politely refuse to answer unrelated questions."},
                {"role": "assistant", "content": "Hello! I'm your Home Improvement Advisor. How can I help you with your renovation or DIY projects today?"}
            ]
            st.rerun()

if __name__ == "__main__":
    main()
