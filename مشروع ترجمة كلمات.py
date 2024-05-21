from gtts import gTTS
from googletrans import Translator
loka=Translator()

word=input("press enter word :\n")

print=input("لعب")

x=("لعب")

y=x

language="ar"
object=gTTS(text=y,lang=language)
object.save("play.mp3")

word1=input("press enter word :\n")
print=input("يقفز")

o=("يقفز")

m=o
language="ar"

object=gTTS(text=m,lang=language)
object.save("jump.mp3")