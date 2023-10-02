from voice import *
from gtts import gTTS
import g4f
import subprocess
import time

def talkback(data):
    language= 'en'
    output = gTTS(text=data, lang=language, slow=False)
    output.save("output.mp3")
    #subprocess.run(['mpg321', r'output.mp3'])
    subprocess.run(['vlc', '--intf', 'dummy', '--play-and-exit', 'output.mp3'])

def ask_valid_question():
    question = record_audio()
    if "question" in question: 
        question.replace('question', "")
        print(question)
        return question
    else:
        time.sleep(1)
        ask_valid_question()

def answer(question):
    # Set with provider
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.DeepAi,
        messages=[{"role": "user", "content": question}],
        stream=True,
    )
    return response

if __name__ == "__main__":   
    question = ask_valid_question()
    while True:
        response = answer(question)
        try:
            message = " ".join(response)
            #if len(message) >100: talkback("Hold on this will take time.")
            talkback(message)
        except Exception as e:
            talkback('Something went wrong. Try asking again.')
        question = ask_valid_question()

        # for message in response:
        #     if "As an AI language model" in message: continue
        #     talkback(message)