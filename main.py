
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    dict_of_chars = count_chars(text)
    list_of_dicts = sort_list_of_dict(dict_of_chars)
    print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()
    for d in list_of_dicts:
        print(f"The {d['char']} character was found {d['num']} times")
    print(" --- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
            
def count_words(text_to_count):
    list_of_words = text_to_count.split()
    return len(list_of_words)

def count_chars(text_to_count):
    dict_of_chars = dict()
    for c in text_to_count.lower():
        dict_of_chars[c] = (dict_of_chars.get(c, 0)) + 1
    return dict_of_chars

def sort_list_of_dict(d):
    list_of_dicts = []
    for k in d:
        if k.isalpha():
            list_of_dicts.append({"char": k, "num": d[k]})
        else:
            continue
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(d):
    return d["num"]

main()

