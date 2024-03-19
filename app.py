import pyttsx3 
from PyPDF2 import PdfReader
import keyboard
droit = pyttsx3.init()
droit.setProperty('rate', 180)
droit.say("Bonjour, Je m'appelle Kassambara Abdramane ")
droit.runAndWait()
def lecture_pdf(fichier):
    with open(fichier, 'rb') as pdf_file_obj:
        pdf_reader = PdfReader(pdf_file_obj)
        num_pages = len(pdf_reader.pages)
        print(num_pages)
        debut_lecture = ""
        for page in pdf_reader.pages:
            debut_lecture += page.extract_text()
        droit.say(debut_lecture)
        droit.runAndWait()
def quitter_programme(e):
    if e.name == 'q':
        droit.stop()
        exit()
keyboard.on_press(quitter_programme)
keyboard.wait('esc')
lecture_pdf("sand-indiana.pdf")
