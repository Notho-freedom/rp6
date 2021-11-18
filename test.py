import speechRecongnition as speechRecongnition
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognitizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices = engine.setProperty('voices',voices[1].id)

def talk(text):
	engine.say(text)
	engine.say(text)
	engine.runAndWait()


def take_command():
	try:
		with sr.Microphone() as source:
			print('listening')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'alexa' in command:
				command = command.replace('alexa','')
				print(command)
	except Exception as e:
		raise e
	return command

def run_alexa():
	command = take_command()
	print(command)
	if 'play' in command:
		song = command.replace('play','')
		talk('playing'+song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%H:%M %p')
		talk('current time is'+time)
	elif 'who the heck is' in command:
		person = command.replace('who the heck is','')
		info = wikipedia.summary(person,1)

	print('listening...')

run_alexa()