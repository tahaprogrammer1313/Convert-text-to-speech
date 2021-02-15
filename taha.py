from gtts import gTTS

import os


mytext = input("Enter a text: ") #Enter a text: taha >>>>>>> mp3

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("taha1414.mp3")

os.system("mpg321 taha1414.mp3")
