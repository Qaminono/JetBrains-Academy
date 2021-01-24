# -*- coding: utf-8 -*-
import requests
import sys


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
supporting_languages_tags = {"1": "rtl arabic",
                             "6": "rtl"}

greeting = "Hello, you're welcome to the translator.\nTranslator supports:\n" \
           + "\n".join([key + '.' + value for key, value in supporting_languages.items()])
if sys.argv[1:4]:
    from_language = {value.lower(): key for key, value in supporting_languages.items()}[sys.argv[1]]
    to_language = "0" if sys.argv[2] == "all" else\
        {value.lower(): key for key, value in supporting_languages.items()}[sys.argv[2]]
    word_to_translate = sys.argv[3]
else:
    print(greeting)
    from_language = input("Type the number of your language: ")
    to_language = input("Type the number of a language you want to translate to or '0' to translate to all languages:")
    word_to_translate = input("Type the word you want to translate: ")


def to_file_and_terminal(func):
    def wrapper(*args):
        out = func(*args)
        file.write(out)
        print(out, end="")
    return wrapper


@to_file_and_terminal
def translate(from_lang, to_lang, word):
    link = r"https://context.reverso.net/translation/" \
           + supporting_languages[from_lang].lower() + "-" \
           + supporting_languages[to_lang].lower() + "/" + word

    r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(r.content, "html.parser")

    div = soup.find_all('div', {'id': "translations-content"})
    foreign_words = [word.strip() for word in div[0].text.split()]

    class_src = f"src {supporting_languages_tags.get(from_lang, 'ltr')}"
    class_trg = f"trg {supporting_languages_tags.get(to_lang, 'ltr')}"

    div_src = soup.find_all('div', {'class': class_src})
    div_trg = soup.find_all('div', {'class': class_trg})
    quotes = list(zip([tag.text.strip() for tag in div_src], [tag.text.strip() for tag in div_trg]))
    return f"{supporting_languages[to_lang]} Translations:" \
           + "\n" + str(foreign_words[0]) + "\n\n" \
           + f"{supporting_languages[to_lang]} Examples:"\
           + "\n" + quotes[0][0] + ":\n" + quotes[0][1] + "\n\n"


with open(f"{word_to_translate}.txt", "a+", encoding="utf-8") as file:
    if to_language == "0":
        for language in supporting_languages:
            if language != from_language:
                translate(from_language, language, word_to_translate)
    else:
        translate(from_language, to_language, word_to_translate)
