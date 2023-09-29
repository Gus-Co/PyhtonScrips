import pyttsx3,PyPDF2

# install the pyttsx3,PyPDF2
# pip install pyttsx3
# pip install PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('so.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()