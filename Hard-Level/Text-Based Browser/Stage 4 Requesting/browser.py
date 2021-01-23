import os
import sys
import requests


path = sys.argv[-1]
os.makedirs(path, exist_ok=True)


class Browser:
    def __init__(self):
        self.downloads = path
        self.history = []
        self.history_index = -1
        self.cashed_sites = os.listdir(path)
        self.commands = {"exit": self.exit,
                         "back": self.back}
        self.is_work = True
        self.request = ""

    def main_loop(self):
        while self.is_work:
            self.request = input()
            if self.request in self.commands:
                self.commands[self.request]()
            else:
                if self.request in self.cashed_sites:
                    with open(f"{path}\\{self.request}", "r", encoding="utf-8") as cash:
                        print("".join(cash.readlines()))
                    self.add_to_history()
                else:
                    response = requests.get(("" if self.request.startswith("https://") else "https://") + self.request)
                    print(response.content.decode())
                    with open(f"{path}\\{self.request.split('.')[0]}", "w", encoding="utf-8") as cash:
                        print(response.content.decode(), end="", file=cash)
                        cash.close()
                    self.cashed_sites.append(self.request.split('.')[0])
                    self.add_to_history()

    def add_to_history(self):
        entry = self.request.split('.')[0]
        self.history = self.history[:self.history_index + 1] + [entry]
        self.history_index += 1

    def back(self):
        self.history_index -= 1
        if self.history and self.history_index > -1:
            with open(f"{path}\\{self.history[self.history_index]}", "r", encoding="utf-8") as cash:
                print("".join(cash.readlines()))
        else:
            print("History is empty!")

    def exit(self):
        self.is_work = False


browser = Browser()
browser.main_loop()
