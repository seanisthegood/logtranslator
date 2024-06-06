from flask import Flask, render_template, request, jsonify # type: ignore
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)


# Set your OpenAI API key
# openai_api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_key = openai_api_key
def index():
    app_name = "Logarithm Translator"
    navigation = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about"},
        {"name": "Contact", "url": "/contact"},
    ]
    return render_template('index.html', app_name=app_name, navigation=navigation)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        logarithm = request.form['logarithm']
        translation = translate_logarithm(logarithm)
        return jsonify({'translation': translation})
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/contact/')
def contact():
    return render_template('contact.html')

def translate_logarithm(logarithm):
    try:
        response = openai.chat.completions.create(
            messages=[
        {
            "role": "user",
            "content":f"Translate the following logarithm into human-readable language and explain it, but do not give the solution. Maybe elaborate a litle bit. Restate it a different way: '{logarithm}'",
            }
            ],
        model="gpt-3.5-turbo",
        )
        
        # print(response.choices[0].message.content)
        translation = response.choices[0].message.content
        
        
        return translation
        
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
