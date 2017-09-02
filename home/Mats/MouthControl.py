python = Runtime.createAndStart("python","Python")
mouth = Runtime.createAndStart("Mouth","MouthControl")
arduino = mouth.getArduino()
arduino.connect('COM11')
jaw = mouth.getJaw()
jaw.detach()
jaw.attach(arduino,11)
mouth.setmouth(110,120)
mouth.autoAttach = False
speech = Runtime.createAndStart("Speech","AcapelaSpeech")
mouth.setMouth(speech)
speech.setVoice("Will")
def onEndSpeaking(text):
	mouth.setmouth(90,120)
	jaw.moveTo(95)
	sleep(.5)
	mouth.setmouth(110,120)
python.subscribe(speech.getName(),"publishEndSpeaking")
# Start of main script
speech.speakBlocking("I'm speaking a very long text to test mouth movement")
speech.speakBlocking("A new sentence to test another long sentece") 
speech.speakBlocking("And one more") 