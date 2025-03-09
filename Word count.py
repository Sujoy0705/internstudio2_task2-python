def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    return len(words)

filename = "sample.txt"  # Replace with your file name
print("Word Count:", count_words_in_file(filename))