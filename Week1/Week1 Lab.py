def count_lines_words_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            lines = content.split('\n') #split by line
            line_count = len(lines)

            words = content.split() #split by default (spacers used as delimiter)
            word_count = len(words)

            char_count = len(content) #counts characters

            return line_count, word_count, char_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == "__main__":
    file_path = "sample.txt"
    result = count_lines_words_characters(file_path)

    if result is not None:
        line_count, word_count, char_count = result
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
