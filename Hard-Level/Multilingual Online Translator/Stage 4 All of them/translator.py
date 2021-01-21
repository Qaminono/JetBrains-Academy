import requests

from bs4 import BeautifulSoup

supporting_languages = {"1": "Arabic",
                        "2": "German",
                        "3": "English",
                        "4": "Spanish",
                        "5": "French",
                        "6": "Hebrew",
                        "7": "Japanese",
                        "8": "Dutch",
                        "9": "Polish",
                        "10": "Portuguese",
                        "11": "Romanian",
                        "12": "Russian",
                        "13": "Turkish"}

greeting = "Hello, you're welcome to the translator.\nTranslator supports:\n" \
           + "\n".join([key + '.' + value for key, value in supporting_languages.items()])

print(greeting)
from_lang = input("Type the number of your language: ")
to_lang = input("Type the number of language you want to translate to: ")
word = input("Type the word you want to translate: ")

link = r"https://context.reverso.net/translation/" \
       + supporting_languages[from_lang].lower() + "-" \
       + supporting_languages[to_lang].lower() + "/" + word

r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})

if r.status_code in range(200, 400):
    print(r.status_code, "OK")
else:
    print(r.status_code, "Not OK")

soup = BeautifulSoup(r.content, "html.parser")

div = soup.find_all('div', {'id': "translations-content"})
foreign_words = [word.strip() for word in div[0].text.split()]

div_src = soup.find_all('div', {'class': "src ltr"})
div_trg = soup.find_all('div', {'class': "trg ltr"})
quotes = list(zip([tag.text.strip() for tag in div_src], [tag.text.strip() for tag in div_trg]))

print(f"{supporting_languages[to_lang]} Translations:")
print("\n".join(foreign_words) + "\n")
print(f"{supporting_languages[to_lang]} Examples:")
print("\n".join([quote[0] + ":\n" + quote[1] + "\n" for quote in quotes]))
