from tts import text_to_speech
from translate import to_english, to_french, to_arabic

def user_accepts():
    user_consent = input("Do you want to the ai to read the above text?:\n")
    if user_consent.lower() == "yes":
        return True
    if user_consent.lower() == "no":
        return False
    user_accepts()    

def snapTranslate(data):
    translate = {"en": to_english, "fr": to_french, "ar": to_arabic}
    if (data.strip() != ""):
        print(data.strip())
        data = "".join(data.strip().split('\n'))
        language = choose_language()
        translator = translate[language]
        data = translator(data)
        text_to_speech(data, language)
    else:
        print("No text detected")
def choose_language():
    user_input = input("Which language do you want to translate the text into [en] [fr] [ar]?\n")
    langauge_options = ["en", "fr", "ar"]
    while user_input.strip() == "" or not user_input in langauge_options:
        print("Invalid option")
        user_input = input("Which language do you want to translate the text into [en] [fr] [ar]?\n")
    return user_input