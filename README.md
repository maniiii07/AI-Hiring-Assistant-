# AI Hiring Assistant

## Project Overview
The **AI Hiring Assistant** is a Streamlit-based chatbot designed to streamline the technical screening process during hiring. It gathers candidate details, such as their name, contact information, experience, and technical expertise, and then generates tailored technical interview questions using the **Mistral-7B-Instruct** model from Hugging Face.

### Key Features:
- Automated **technical interview question generation** based on the candidate's tech stack.
- **Interactive** chatbot interface for candidate screening.
- **Privacy-focused**: Candidate data is cleared after the session.
- **Easy-to-use** navigation with a sidebar for switching between Home, Interview, and About Us pages.

---

## Installation Instructions
### Prerequisites
Ensure you have the following installed on your machine:
- **Python 3.8+**
- **pip** (Python package manager)

### Steps to Set Up Locally
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/ai-hiring-assistant.git
   cd ai-hiring-assistant
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the Hugging Face API Key:**
   - Replace the `token` variable inside `app.py` with your Hugging Face API Key.
   
5. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
6. Open the displayed **local URL** in your web browser.

---

## Usage Guide
### Home Page
- Provides an overview of the AI Hiring Assistant and how it works.
- Includes a **data privacy disclaimer** ensuring no candidate data is stored.

### Interview Page
1. **Enter Candidate Information:**
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position
   - Tech Stack (comma-separated)
2. Click **"Generate Technical Questions"** to let AI generate questions.
3. The chatbot displays the generated questions along with the candidate's profile.
4. Click **"Exit & Reset"** to clear data and return to the Home page.

### About Us Page
- Describes the project and its purpose.
- Provides a contact email for inquiries.

---

## Technical Details
### Libraries Used
- `streamlit` – Frontend UI framework.
- `requests` – API calls to Hugging Face for AI-generated responses.
- `Hugging Face Inference API` – Powered by `Mistral-7B-Instruct-v0.1` for generating questions.

### Architectural Decisions
- **Session State**: Used to maintain user progress during an interview session.
- **State Resetting**: Implemented a function to clear session data after each interview to ensure data privacy.
- **Model Choice**: `Mistral-7B-Instruct` was chosen for its strong instruction-following capabilities.

---

## Prompt Design
Prompts are carefully crafted to extract the necessary information and generate relevant interview questions. Example:
```plaintext
Generate 3-5 technical interview questions for a candidate proficient in {tech_stack}.
```
This ensures that the AI provides structured and relevant questions based on the candidate’s expertise.

---

## Challenges & Solutions
### 1. API Response Handling
- **Issue:** The Hugging Face API sometimes returns unexpected responses or takes time to load.
- **Solution:** Implemented response error handling and a message for users when the model is still loading.

### 2. Ensuring Data Privacy
- **Issue:** Candidate data persistence could be a concern.
- **Solution:** Used `st.session_state` and a reset function to clear data after the session.

### 3. Generating Relevant Interview Questions
- **Issue:** Some responses from the model were too general.
- **Solution:** Improved prompt design by explicitly specifying "technical interview questions" to ensure relevant outputs.

---

## Future Enhancements
- **Cloud Deployment:** Host on Streamlit Sharing or Hugging Face Spaces.
- **User Authentication:** Add authentication for hiring managers.
- **More AI Models:** Integrate additional models for better response variations.

---

## Contact
For support, reach out via email: [support1mani@gmail.com](mailto:bmanipreetham@gmail.com)

