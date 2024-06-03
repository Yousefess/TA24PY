import random
from src.utils import print_success, print_error, print_warning

random.seed(42)

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000):
        self.word_len = word_len
        self.limit = limit
        self.words = self.generate_word_frequency(file_path, word_len, limit)

    def generate_word_frequency(self, file_path: str, word_len: int, limit: int):
        # Build Data
        words_freq = []
        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(',')
                frequency = int(frequency)
                words_freq.append((word, int(frequency)))

        # Sort Data
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

        # Limit Data
        words_freq = words_freq[:limit]

        # Drop Frequency Data
        words = [w_freq[0] for w_freq in words_freq]

        # word_len letters words
        words = list(filter(lambda w: len(w) == word_len, words))

        return words

    def run(self, ):
        # Random Word
        word = random.choice(self.words)
        word = word.upper()

        # Start Game
        num_try = 6
        success = False

        while num_try:
            guess_word = input(f'Enter a {self.word_len} letter word (or q to exit): ')
            if guess_word == 'q':
                break

            guess_word = guess_word.upper()

            # Word Length
            if len(guess_word) != 5:
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}!')

            # Check valid word
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid')
                continue

            # Check valid, invalid positions, invalid characters
            for w_letter, g_letter in zip(word, guess_word):
                if w_letter == g_letter:
                    print_success(f' {g_letter} ', end=' ')
                elif g_letter in word:
                    print_warning(f' {g_letter} ', end=' ')
                else:
                    print_error(f' {g_letter} ', end=' ')
            print()

            # Check success
            if word == guess_word:
                print()
                print_success(' Congratulations! ')
                success = True
                break

            num_try -= 1

        if not success:
            print_error(f'Game over: The word was "{word}".')

if __name__ == '__main__':
    wordle = Wordle
    wordle.run()