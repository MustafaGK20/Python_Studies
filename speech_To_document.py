from PyPDF2 import PdfReader
from gtts import gTTS
import os

document_type = input("pdf?/txt?:")
document_name = input("Document_Name:")


if document_type.lower().strip() == "txt":
    text = open(file=document_name, mode="r")
    text = text.read()
    tts = gTTS(text=text, lang="tr")
    tts.save("txt_voice.mp3")
    os.system("txt_voice.mp3")


else:
    pdf = PdfReader(document_name)
    number_of_pages = len(pdf.pages)
    text_pdf = []
    for page in range(number_of_pages):

        page = pdf.pages[page]
        text = page.extract_text()
        text_pdf.append(text)
    text_pdf = str(text_pdf)
    tts = gTTS(text=text_pdf, lang="tr")
    tts.save("pdf_voice.mp3")
    os.system("pdf_voice.mp3")