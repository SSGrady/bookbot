def get_num_words(corpus: str):
    split_corpus = corpus.split()
    return len(split_corpus)

def get_character_count(corpus: str) -> dict:
    split_corpus = list(corpus.lower())
    freq = dict()
    for char in split_corpus:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq

def sort_dict_list(freq: dict) -> dict:
    char_list = []
    for char, count in freq.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    def sort_on(item):
        return item["count"]

    char_list.sort(key=sort_on, reverse=True)
    return char_list