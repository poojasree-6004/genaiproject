from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
app = Flask(__name__)
def generate_story(prompt):
    try:
        response = model.generate_content(prompt)
        story = response.text.strip()
        if '.' in story:
            story = story[:story.rfind('.') + 1]
        return story
    except Exception as e:
        return f"Error: {e}"
@app.route("/", methods=["GET", "POST"])
def index():
    story = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            story = generate_story(prompt)
    return render_template("index.html", story=story)
if __name__ == "__main__":
    app.run(debug=True)
