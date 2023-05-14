from googletrans import Translator

def to_english(text):
    translator = Translator()
    return translator.translate(text, dest="en").text
def to_french(text):
    translator = Translator()
    return translator.translate(text, dest="fr").text
def to_arabic(text):
    translator = Translator()
    return translator.translate(text, dest="ar").text