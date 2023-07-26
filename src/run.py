from src.utils import MyPrint
from src.wordle import Wordle

# Local Imports
file_path = 'src/Data/unigram_freq.csv'

# Run the game
wordle = Wordle(file_path)
wordle.run()
