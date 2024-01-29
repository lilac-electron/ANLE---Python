import argparse
import pandas as pd
import matplotlib.pyplot as plt

def count_lines_words_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            lines = content.split('\n') #split by line
            line_count = len(lines)

            words = content.split() #split by default (spacers used as delimiter)
            word_count = len(words)

            total_len=0
            for word in content.split():
                total_len += len(word)
            total_avg = total_len/word_count

            letters = [char.lower()for char in content if char.isalpha()]
            freq_dict = dict()
            for letter in letters:
                if letter not in freq_dict:
                    freq_dict[letter] = 1
                else:
                    freq_dict[letter] += 1
            temp = max(freq_dict.values())
            list_of_frequent_letters = [letter for letter in freq_dict if freq_dict[letter] == temp]


            char_count = len(content) #counts characters


            return line_count, word_count, char_count, total_avg, list_of_frequent_letters, freq_dict

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines, words, and characters in a text file.")
    parser.add_argument('file_path', help="Path to the text file")
    args = parser.parse_args()

    if args.file_path is not None:
        result = count_lines_words_characters(args.file_path)
    else:
        result = count_lines_words_characters('sample.txt')
    

    if result is not None:
        line_count, word_count, char_count, total_avg, list_of_letters, all_letters = result
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
        print(f"Average word length: {total_avg}")
        print(f"Most frequent letters: {list_of_letters}")

        plotdata = pd.DataFrame.from_dict(all_letters, orient='index')

        plotdata.plot(kind="bar",figsize=(15, 8))

        plt.title("Letter Frequencies")

        plt.xlabel("Letters")

        plt.ylabel("Freq of letter")

        plt.show()
        #print(plotdata)
