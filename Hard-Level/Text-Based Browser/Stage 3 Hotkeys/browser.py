import os
import sys


path = sys.argv[1]
os.makedirs(path, exist_ok=True)

nytimes_com = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


class Browser:
    def __init__(self):
        self.downloads = path
        self.history = []
        self.history_index = -1
        self.cashed_sites = [file.split(".")[0] for file in os.listdir(path)]
        self.sites = {'bloomberg.com': bloomberg_com,
                      'nytimes.com': nytimes_com}
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
                if self.request in self.sites:
                    print(self.sites[self.request])
                    if self.request not in self.cashed_sites:
                        with open(f"{path}\\{self.request.split('.')[0]}", "w", encoding="utf-8") as cash:
                            print(self.sites[self.request], end="", file=cash)
                            cash.close()
                        self.cashed_sites.append(self.request.split('.')[0])
                    self.add_to_history()
                elif self.request in self.cashed_sites:
                    with open(f"{path}\\{self.request}", "r", encoding="utf-8") as cash:
                        print("".join(cash.readlines()))
                    self.add_to_history()
                else:
                    print("Error: Incorrect URL")

    def add_to_history(self):
        entry = self.request + ("" if self.request.endswith(".com") else ".com")
        self.history = self.history[:self.history_index + 1] + [entry]
        self.history_index += 1

    def back(self):
        self.history_index -= 1
        if self.history:
            print(self.sites[self.history[self.history_index]])
        else:
            print("History is empty!")

    def exit(self):
        self.is_work = False


browser = Browser()
browser.main_loop()
