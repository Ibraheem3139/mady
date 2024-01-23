from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system(f"start {output_file}")  # Opens the generated audio file

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(input_text)
