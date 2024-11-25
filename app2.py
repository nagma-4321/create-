
print("hello")

import streamlit as st

# Initialize session state for tracking conversation
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

suggestion = "Please convert them to physical copies; otherwise, you might lose them due to storage issues."

# Define layout
st.set_page_config(page_title="Professional Chatbot", layout="wide")
st.title("DATE TO MEMORIES (2024 Edition)")
st.markdown("**Reliving Moments, Creating Memories**")

# Chat UI
st.write("### Chat Conversation")
chat_area = st.empty()

# Display chat history
def display_chat():
    chat_html = ""
    for i, (bot, user) in enumerate(st.session_state.responses):
        chat_html += f"""
        <div style="display: flex; margin-bottom: 10px;">
            <div style="flex: 1; text-align: left; background-color: #f0f8ff; padding: 10px; border-radius: 10px; border: 2px solid #FF4500; font-family: Arial, sans-serif; font-weight: bold;">
                Bot: {bot}
            </div>
        </div>
        """
        if user:
            chat_html += f"""
            <div style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
                <div style="flex: 1; text-align: right; background-color: #f5f5f5; padding: 10px; border-radius: 10px; border: 2px solid #32CD32; font-family: Verdana, sans-serif; font-weight: bold;">
                    You: {user}
                </div>
            </div>
            """
    chat_area.markdown(chat_html, unsafe_allow_html=True)

# Handle user response
def handle_response(user_response):
    current_index = st.session_state.current_question_index

    if not user_response:
        st.warning("Please respond to the question before proceeding!")
        return

    # Save the user's response
    question = questions[current_index]
    st.session_state.responses.append((question, user_response))

    # Add suggestion for Question 7
    if current_index == 7:
        st.session_state.responses.append(("Suggestion", suggestion))

    # Move to the next question
    st.session_state.current_question_index += 1

# Display next question or thank you message
if st.session_state.current_question_index < len(questions):
    display_chat()
    current_question = questions[st.session_state.current_question_index]
    st.markdown(f"**Bot:** {current_question}")

    # Input for user response
    user_input = st.text_input("Your Response", key="user_input")
    if st.button("Send"):
        handle_response(user_input)
else:
    # Display end message
    user_name = st.session_state.responses[0][1] if st.session_state.responses else "Friend"
    st.markdown(
        f"""
        <div style="background-color: #FFD700; padding: 20px; border-radius: 10px; text-align: center;">
            <h2>Thank You, {user_name}!</h2>
            <p>I appreciate your thoughtful responses and wish you all the best for the future.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Update chat display
display_chat()



        