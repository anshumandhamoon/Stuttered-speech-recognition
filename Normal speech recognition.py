import pyaudio
import wave
import speech_recognition as sr
import pyttsx
from os import path

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()
engine=pyttsx.init()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "Please say something... Recording"


frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "Finished recording"
engine.say("Finished Recording")
engine.runAndWait()


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()



WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "file.wav")

#for text to speech

print ("Analyzing file.... Please wait")
engine.say("Analyzing file.... Please wait")
engine.runAndWait()

# use "test.wav" as the audio source
r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source) # read the entire WAV file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`

    a="Google Speech Recognition thinks you said: " + r.recognize_google(audio)
    print a
    engine.say(a)
    engine.runAndWait()
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
