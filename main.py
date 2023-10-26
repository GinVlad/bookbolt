def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_num_words(text)
    num_letters = count_letters(text)
    sorted_list = sort_letters(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for i in sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]

def sort_letters(num_letters):
    sorted = []
    for letter in num_letters:
        sorted.append({"char": letter, "num": num_letters[letter]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def count_num_words(text):
    return len(text.split())


def count_letters(words):
    result = {}
    for word in words:
        lowered = word.lower()
        if lowered in result:
            result[lowered] += 1
        else:
            result[lowered] = 1
    return result

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()