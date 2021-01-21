import requests

from bs4 import BeautifulSoup

language_choice = input('Type "en" if you want to translate from French into English, '
                        'or "fr" if you want to translate from English into French:')
language = {"en": "french-english",
            "fr": "english-french"}
word_choice = input("Type the word you want to translate:")
print(f'You chose "{language_choice}" as the language to translate "{word_choice}" to.')
link = r"https://context.reverso.net/translation/" + language[language_choice] + "/" + word_choice

r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})

if r.status_code in range(200, 400):
    print(r.status_code, "OK")
else:
    print(r.status_code, "Not OK")

soup = BeautifulSoup(r.content, "html.parser")
div = soup.find_all('div', {'id': "translations-content"})
print("Translations")
print([word.strip() for word in div[0].text.split()])
div_src = soup.find_all('div', {'class': "src ltr"})
div_trg = soup.find_all('div', {'class': "trg ltr"})
print(list(zip([tag.text.strip() for tag in div_src], [tag.text.strip() for tag in div_trg])))
