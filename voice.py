import speech_recognition as sr

r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
usb_mic = [mic for mic in mic_list if "USB" in mic]
print(f"Selected Mic: {usb_mic}")
if len(usb_mic) > 0:
    # set the USB microphone as the source
    usb_index = mic_list.index(usb_mic[1])
    print(usb_index)
else:
    print("No USB microphone found. Please connect a USB microphone and try again.")

def record_audio():
    with sr.Microphone(device_index=usb_index) as source:
        audio = r.listen(source)
        voice_data = ''
        recorded_audio = ''
        try:
            voice_data= r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print('Sorry, my speech service is down')
    return voice_data