from voice import *

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is WallE')
    elif 'acti champ' in voice_data:
        print("actiCHamp")
    else:
        print(voice_data)

if __name__ == "__main__":   
 
    print ("How can I help you?")
    voice_data= record_audio()
    respond(voice_data)