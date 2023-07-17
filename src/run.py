from src.utils import MyPrint
from src.wordle import Wordle

file_path = 'src/Data/unigram_freq.csv'
wordle = Wordle(file_path)
wordle.run()
