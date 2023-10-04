# pip install playsound==1.2.2

try:
    import playsound
except ModuleNotFoundError:
    pip.main(['install', 'playsound===1.2.2'])

from os import path 
from playsound import playsound

morse_letter = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
morse_number = ["-----", ".----", "..---", "...--",
                "....-", ".....", "-....", "--...", "---..", "----."]
x = dict()
for i in range(65, 91):
    x[chr(i)] = morse_letter[i-65]
for i in range(10):
    x.update({str(i): morse_number[i]})
x[" "] = "/"
word = str(input("Give me word : "))
keys = list(x.keys())
z = ""
for c in word:
    if c.upper() in keys:
        z = z+" "+x[c.upper()]
        print(c, " = ", x[c.upper()], end="\n")
        if c != " ":
           # playsound(path.dirname('space.mp3').replace("\\","/")+"space.mp3")
        #else:
            playsound(path.dirname(c.upper()+".mp3").replace("\\","/")+c.upper()+".mp3")
    else:
        print(c, " = ", x[c.upper()], end="\n")

print(z)
input()
