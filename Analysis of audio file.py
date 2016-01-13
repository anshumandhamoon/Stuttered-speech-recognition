from scipy.io.wavfile import read
from scipy.fftpack import fft
import matplotlib.pyplot as plt

id=read("file.wav")
#print "ID = ",id
audio=id[1]
#print "Audio = ",audio
#y=fft(audio)
#plt.plot(id)
print (audio)
plt.plot(audio)
plt.show()


#plt.plot(audio[0:512])
#plt.plot(audio[0:1024])
#plt.show()
