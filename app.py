import streamlit as st
import requests
from textblob import TextBlob
from googletrans import Translator
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Hugging Face API Key and Model
token = os.getenv("HUGGINGFACE_TOKEN")  # Load from environment
if not token:
    st.error("❌ Missing Hugging Face API Token. Please set it in the .env file.")
    st.stop()

model = "mistralai/Mistral-7B-Instruct-v0.1"
API_URL = f"https://api-inference.huggingface.co/models/{model}"
HEADERS = {"Authorization": f"Bearer {token}"}
translator = Translator()

def query_huggingface(payload):
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 503:
            return "⏳ Model is still loading. Please wait a moment."
        elif response.status_code == 403:
            return "❌ API Key issue: This model requires a Pro subscription."
        elif response.status_code != 200:
            return f"⚠️ Error {response.status_code}: {response.text}"
        
        response_json = response.json()
        if isinstance(response_json, list) and len(response_json) > 0:
            return response_json[0].get("generated_text", "⚠️ No text generated.")
        return "⚠️ Unexpected response format."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "😊 Positive"
    elif sentiment < 0:
        return "😟 Negative"
    return "😐 Neutral"

def translate_text(text, dest_language):
    try:
        return translator.translate(text, dest=dest_language).text
    except Exception:
        return "Translation error."

# Streamlit UI Styling
st.set_page_config(page_title="AI Hiring Assistant", page_icon="💼", layout="wide")
st.sidebar.title("📌 Navigation")
nav_selection = st.sidebar.radio("Go to", ["Home", "Interview", "About Us"], index=0)

if nav_selection == "Home":
    st.title("💼 AI Hiring Assistant")
    st.subheader("🚀 Transform Your Hiring Process with AI")
    
    st.write(
        "AI Hiring Assistant helps recruiters streamline the interview process by automatically generating relevant "
        "technical questions based on a candidate’s skill set. This reduces manual effort and ensures an unbiased screening process."
    )
    
    st.info("⚠️ Data Privacy: No candidate data is stored. All details are cleared after exiting.")

    st.subheader("🔍 Key Features:")
    
    features = [
        "📌 **AI-Powered Question Generation** - Generates relevant technical questions based on candidate skills.",
        "🛠️ **Multi-Language Support** - Communicate in different languages for a diverse hiring process.",
        "💬 **Sentiment Analysis** - Gauge candidate confidence and emotion through responses.",
        "⏳ **Time-Saving** - Automates the initial interview process, reducing screening time.",
        "🌍 **Global Accessibility** - Enables recruiters to interview candidates from any location.",
        "🔐 **Privacy-Focused** - No personal data storage, ensuring candidate information remains secure."
    ]
    
    for feature in features:
        st.write(feature)
    
    st.subheader("📊 How It Works:")
    st.write("1. **Enter Candidate Information** - Fill in details such as name, experience, and tech stack.")
    st.write("2. **AI Generates Questions** - AI automatically creates relevant technical interview questions.")
    st.write("3. **Multilingual & Sentiment Analysis** - Receive responses in multiple languages with emotional insights.")
    st.write("4. **Improve Your Hiring Decisions** - Use AI-generated insights to make more informed hiring choices.")
    
    st.subheader("📞 Get Started Today!")
    st.write("Use the navigation panel on the left to begin the interview process.")

elif nav_selection == "Interview":
    st.subheader("🤖 Chatbot Greeting")
    st.write("Hello! Welcome to the AI Hiring Assistant. Please provide candidate details to proceed.")
    
    with st.form("candidate_form"):
        st.subheader("🔍 Candidate Information")
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email Address")
        phone = st.text_input("📱 Phone Number")
        years_experience = st.number_input("💼 Years of Experience", min_value=0, max_value=50, step=1)
        desired_position = st.text_input("🎯 Desired Position")
        tech_stack = st.text_area("🛠️ Tech Stack (comma-separated, e.g., python,react,sql)")
        language = st.selectbox("🌍 Preferred Language", ["English", "Spanish", "French", "German", "Chinese"])
        submit_button = st.form_submit_button("Generate Technical Questions")
    
    if submit_button:
        if not tech_stack.strip():
            st.error("⚠️ Please provide a tech stack!")
        else:
            prompt = f"Generate 3-5 technical interview questions for a candidate proficient in {tech_stack}."
            response = query_huggingface({"inputs": prompt})
            translated_response = translate_text(response, language[:2].lower())
            sentiment = analyze_sentiment(response)
            
            st.subheader("📌 Interview Questions:")
            st.write(translated_response)
            st.write(f"**Sentiment Analysis:** {sentiment}")
            
            if st.button("Exit & Reset"):
                st.experimental_rerun()

elif nav_selection == "About Us":
    st.title("📖 About AI Hiring Assistant")
    st.write("This AI-powered hiring assistant streamlines the recruitment process by generating relevant technical interview questions tailored to a candidate's skill set. It now supports multilingual interactions and sentiment analysis.")
    st.subheader("🔗 Contact Us")
    st.write("For inquiries, reach out to us at [supportmani1@gmail.com](mailto:bmanipreetham@gmail.com)")
