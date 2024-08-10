# app.py

from flask import Flask, render_template, send_file
import subprocess


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/run_voice_assistant')
def run_voice_assistant():
    subprocess.run(['python', 'VoiceAssistant_Pikachu.py'])  # Execute the Python script
    audio_file_path = 'response.wav'  # Path to the generated audio file
    return send_file(audio_file_path, mimetype='audio/wav')

if __name__ == '__main__':
    
    app.run(debug=True)

