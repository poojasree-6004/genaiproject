#  Simple Story Generator using Gemini Flash 1.5 (Flask App)

This is a simple web-based story generator built with **Flask** and powered by **Google's Gemini 1.5 Flash model**. Enter a prompt, and it will generate a creative story for you.
##  Features
- Uses **Gemini 1.5 Flash** for story generation
- User-friendly HTML interface
- Powered by Flask backend
- Styled with responsive CSS
##  Project Structure
aiproject/
│
├── app.py                
├── templates/
│   └── index.html        
├── .env                 
└── README.md             
## 🔧 Installation
### 1. Clone the repository
git clone https://github.com/poojasree-6004/genaiproject.git
cd aiproject
### 2. Create a virtual environment
python -m venv venv
### 3. Activate the environment
  venv\Scripts\activate
### 4. Install dependencies
pip install flask python-dotenv google-generativeai
##  Setup API Key
1. Create a `.env` file in the project root:
2. GEMINI_API_KEY=your_api_key_here
3. Get your API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)
4. ##  Run the Application
python app.py
Open your browser and go to: [http://localhost:5000](http://localhost:5000)
##  Technologies Used
- [Flask](https://flask.palletsprojects.com/)
- [Google Generative AI Python SDK](https://github.com/google/generative-ai-python)
- [HTML & CSS](https://developer.mozilla.org/)
##  Example Prompt
A young girl finds a mysterious door in her backyard.




