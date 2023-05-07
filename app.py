from flask import Flask, render_template, request
from gtts import gTTS
import os
from playsound import playsound

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        language = 'en'
        try:
            # Create the text-to-speech audio file
            tts = gTTS(text=text, lang=language)
            filename = 'audio.mp3'
            tts.save(filename)

            # Play the audio file using the playsound library
            playsound(filename)

            # Serve the audio file for playback
            return render_template('playback.html', filename=filename)
        except:
            # Display an error message if something went wrong
            return render_template('error.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/signin', methods=['POST', 'GET'])
def login():
    return render_template('signIn.html')