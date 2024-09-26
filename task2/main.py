def print_list(word_list):
    print("Список слів:", word_list)

def search_word_in_list(word_list, word_to_find):
    if word_to_find in word_list:
        print(f"Слово '{word_to_find}' знайдено у списку.")
    else:
        print(f"Слово '{word_to_find}' не знайдено у списку.")

def main():
    words = ["яблуко", "банан", "апельсин", "груша"]
    print_list(words)
    word_to_find = input("Введіть слово для пошуку: ")
    search_word_in_list(words, word_to_find)

if __name__ == "__main__":
    main()