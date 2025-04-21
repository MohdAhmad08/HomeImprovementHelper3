import os
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Home Improvement Advisor",
    page_icon="🏠",
    layout="wide"
)

# App header
st.title("🏠 Home Improvement Advisor")
st.markdown("""
Get personalized advice for home renovation, repairs, and DIY projects.
""")

# Add developer information below the header
st.markdown("---")
st.markdown("### Developed by:")
st.markdown("- **Mohd** (12321720)")
st.markdown("- **Supriyo Tandi** (12326766)")
st.markdown("---")

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
    
    ### Developed by:
    - Mohd (12321720)
    - Supriyo Tandi (12326766)
    """)
