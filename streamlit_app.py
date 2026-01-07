import streamlit as st
import hr_logic

# -------------------------------------
# Page Configuration & Custom CSS
# -------------------------------------
st.set_page_config(page_title="HR Genie", page_icon="🧞‍♂️", layout="wide")

# Custom CSS for Premium Design V2 (Teal/Gold/Blue)
# Custom CSS for Premium Design V2 (Teal/Gold/Blue)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@500;600;700&display=swap');

    /* Global Styles */
    :root {
        --primary-blue: #1F3C88;
        --teal: #2EC4B6;
        --gold-accent: #E0B973;
        --light-bg: #F5F7FA;
        --white: #FFFFFF;
        --text-color: #2C3E50;
        --chat-bubble-user: #FFFFFF;
        --chat-bubble-genie: #F0F9F8;
    }
    
    .stApp {
        background-color: var(--light-bg);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: var(--white);
        border-right: 1px solid #E8EEF2;
    }
    
    /* Custom Headers */
    h1 {
        color: var(--primary-blue);
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        padding-bottom: 10px;
        border-bottom: 2px solid var(--light-bg);
    }
    
    h2, h3, h4 {
        font-family: 'Poppins', sans-serif;
        color: var(--primary-blue);
    }
    
    /* Buttons */
    div.stButton > button {
        width: 100%;
        background-color: var(--white);
        color: var(--text-color);
        border: 1px solid #E8EEF2;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
        text-align: left;
        display: flex;
        justify-content: flex-start;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }
    
    div.stButton > button:hover {
        border-color: var(--teal);
        background-color: var(--light-bg);
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transform: translateY(-2px);
    }
    
    div.stButton > button:active {
        transform: translateY(0);
        background-color: var(--white);
        color: var(--teal);
    }

    /* Chat Messages */
    .stChatMessage {
        background-color: transparent;
        animation: fadeIn 0.3s ease;
    }
    
    /* User Avatar */
    [data-testid="stChatMessage"] [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, var(--primary-blue), var(--teal));
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Bot Avatar */
    [data-testid="stChatMessage"] [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, var(--primary-blue), var(--teal));
        color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* Chat Bubbles (Targeting Streamlit's internal structure roughly, though limited) */
    .stMarkdown {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
    }

    /* Keyframes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { opacity: 0.3; transform: scale(0.95); }
        100% { opacity: 0.6; transform: scale(1.05); }
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# -------------------------------------
# Sidebar Structure
# -------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem; padding: 1rem; background: linear-gradient(135deg, #1F3C88 0%, #2a4ba0 100%); border-radius: 12px;">
            <div style="
                width: 56px; 
                height: 56px; 
                background-color: rgba(255, 255, 255, 0.15); 
                border-radius: 14px; 
                margin: 0 auto; 
                display: flex; 
                align-items: center; 
                justify-content: center;
                font-size: 26px;
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.2);
                position: relative;
            ">
                <i class="fas fa-magic"></i>🧞‍♂️
            </div>
            <h2 style="color: white; margin-top: 12px; margin-bottom: 0; font-family: 'Poppins', sans-serif; font-size: 20px;">HR Genie</h2>
            <p style="color: rgba(255, 255, 255, 0.8); font-size: 13px; margin: 4px 0 0 0;">Corporate HR Assistant</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ Quick Actions")
    
    # Callback to handle button clicks
    def quick_action(query):
        st.session_state.messages.append({"role": "user", "content": query})
        # Logic to process immediately is handled in the main loop re-run

    if st.button("👥 New Employee Onboarding"):
        quick_action("Explain Onboarding Lifecycle")
        
    if st.button("📄 HR Policies Overview"):
        quick_action("Show HR Policies Overview")
        
    if st.button("📅 Leave & Attendance"):
        quick_action("Explain Leave Policy")
        
    if st.button("🎁 Employee Benefits"):
        quick_action("Show Benefits Summary")
        
    if st.button("🛡️ Code of Conduct"):
        quick_action("Explain Code of Conduct")
        
    if st.button("❓ FAQ & Help"):
        quick_action("Show FAQ")

    st.markdown("---")
    st.markdown("""
        <div style="font-size: 12px; color: #7F8C8D; text-align: center;">
            <span style="color: #2EC4B6;">🔒</span> Confidential & Secure
        </div>
    """, unsafe_allow_html=True)

# -------------------------------------
# Main Chat Configuration
# -------------------------------------

# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "👋 **Hello! I'm HR Genie.**\n\nI can help you with onboarding, company policies, leaves, benefits, and more. \n\n*How can I assist you today?*"
    })

if "last_topic" not in st.session_state:
    st.session_state.last_topic = None

# Title Area
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 2rem;">
        <div>
            <h1 style="margin:0; border:none;">Welcome, John Doe</h1>
            <p style="color: #7F8C8D; margin:0;">Tech Dept • New Employee</p>
        </div>
        <div style="text-align: right; font-size: 12px; color: #7F8C8D;">
            <span style="color: #2EC4B6;">●</span> Online <br>
            Policy Updated: June 15, 2023
        </div>
    </div>
""", unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handling new user input
if prompt := st.chat_input("Type your question here..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process query
    response_data = hr_logic.process_query(prompt, st.session_state.last_topic)
    bot_response = response_data["text"]
    st.session_state.last_topic = response_data["topic"]
    
    # Append bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Special handling for "Quick Actions" (which append to messages but need to trigger a re-run logic)
# Check if the last message was from user and hasn't been responded to yet
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    last_user_msg = st.session_state.messages[-1]["content"]
    # Check if we already have a response (Streamlit re-runs script top-to-bottom)
    # If the length is odd (User just added a message), valid.
    if len(st.session_state.messages) % 2 != 0:
        # Get bot response
        response_data = hr_logic.process_query(last_user_msg, st.session_state.last_topic)
        bot_response = response_data["text"]
        st.session_state.last_topic = response_data["topic"]
        
        # Add to state
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun() # Force re-run to display the new message
