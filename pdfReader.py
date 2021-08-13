# PDF reader python Project

import pyttsx3
import PyPDF2

pdf_book = open('d:/My_projects/UdayveerSingh.pdf','rb')
reading_pdf = PyPDF2.PdfFileReader(pdf_book)

pdf_speaker = pyttsx3.init()             # enable text to speech

choose_page = reading_pdf.getPage(0)     # select page number 0th index based

pdf_text = choose_page.extractText()     # extract all the text from the page

pdf_speaker.say("Hey Udayveer I'm going to speak")
pdf_speaker.say(pdf_text)   # enable to speak
pdf_speaker.say("Thank You")
pdf_speaker.runAndWait()    # make speech audible in the system

