from helpers import get_words, save_counts

def main():
    counts = {}
    words = get_words("address.txt")
    words = [word.lower() for word in words if len(word) > 4]

    # words = []
    # words_lst = []
    # for word in words:
    #     lower_word = word.lower()
    #     words_lst.append(lower_word) 

    for word in words: 
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)

main()