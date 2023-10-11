# importing modules
import requests

# import pprint
welcome_message = (">>Do you want to translate something into Sith language? I got you covered!"
                   "\nWelcome to a Sith Language Translator<<")
print(welcome_message)
# defining url to my chosen API, in this case the API is public, so we don't need a key.
# Downside is, we have only 10 calls per hour ;)
url = "https://api.funtranslations.com/translate/sith.json"


# defining a function to cary out translation
def translate_to_sith():
    # an empty list to store user's translations
    translations = []
    # setting up a while loop to create a session for a user (when the session is terminated, program resets)
    while True:
        text = input("Enter a sentence in English (max. 50 characters)"
                     "\nor type `q` to exit: ")
        if text.lower() == "q":
            # user leaves the program
            break
        else:
            if len(text) > 50:
                print("Input sentence is too long. Please keep it under 50 characters.")
                # thanks to "continue" program won't reset
                continue

            querystring = {"text": text}
            # getting the response from API
            response = requests.get(url, params=querystring)
            # if/else statement that checks server answer, converts response object
            # into json file, and pulling out data we need
            if response.status_code == 200:
                data = json.loads(response.text)
                # fetching needed elements from a dictionary with our data
                translated = data["contents"]["translated"]
                print(f"Translated sentence: {translated}")
                # adding translated text to our list to store it for further manipulation
                translations.append(translated)
            else:
                print(f'Error: {response.status_code}')
    # counting translated sentences and printing them out with their index after user terminates the program
    for index, translation in enumerate(translations, start=1):
        print(f"Translation {index}: {translation}")
        # additional manipulation of our string
        split_translation = translation.split()
        reversed_translation = split_translation[::-1]
        print(f"In case you need it, here you have all the words in reverse order: \n{reversed_translation}")
    return translations


translate_to_sith()
