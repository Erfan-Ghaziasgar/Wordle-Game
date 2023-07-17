import csv
import random

from src.utils import MyPrint


class Wordle():
    def __init__(self, file: str, word_len: int = 5, limit: int = 10000, try_num: int = 6) -> list:
        self.words = self.generate_word(file, word_len, limit)
        self.word_len = word_len
        self.printer = MyPrint()
        self.try_num = try_num

    def generate_word(self, file: str, word_len: int, limit: int) -> list:
        words = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            words = [item for item in reader if len(item[0]) == word_len]
        sorted_words = sorted(words, key=lambda w: int(w[1]), reverse=True)
        sorted_words = [word[0] for word in sorted_words]
        return sorted_words[:limit]

    def select_word(self):
        selected_word = random.choice(self.words)
        selected_word = selected_word.upper()
        return selected_word

    def check_letter(self, selected_word, guess_word):
        for guess_char, word_char in zip(guess_word, selected_word):
            if guess_char == word_char:
                self.printer.success(f"{ guess_char }", end=' ')
            elif guess_char in selected_word:
                self.printer.warning(f"{ guess_char }", end=' ')
            else:
                self.printer.error(f"{ guess_char }", end=' ')
        print()

    def run(self):
        selected_word = self.select_word()
        print(selected_word)
        while self.try_num:
            guess_word = input("Enter your word(press 'q' to exit): ")
            if guess_word == 'q':
                break
            elif len(guess_word) != len(selected_word):
                self.printer.error(
                    f"Length of your word should be {len(selected_word)}")
                continue
            elif guess_word not in self.words:
                self.printer.warning(
                    'Your word is not in the dictionary of game')
                continue
            elif guess_word.upper() == selected_word:
                guess_word = guess_word.upper()
                self.check_letter(selected_word=selected_word,
                                  guess_word=guess_word)
                self.printer.success("Good Job .|.")
                break
            else:
                guess_word = guess_word.upper()
                self.check_letter(selected_word=selected_word,
                                  guess_word=guess_word)

            self.try_num -= 1
        else:
            print()
            self.printer.error(f"Game Over! Correct Word Is {selected_word}")
