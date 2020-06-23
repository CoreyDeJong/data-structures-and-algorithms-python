

def repeater(phrase):
    phrase_list = phrase.split(" ")
    # phrase_list = (phrase_mix.lower())
    dictionary = dict.fromkeys(phrase_list,0)

    # dictionary has all words in it
    # if word

    for word in phrase_list:
        if word in dictionary:
            dictionary[word] += 1
        if dictionary[word] == 2:
            return word



if __name__ == "__main__":
    phrase = "Why are shipments on why cargo and cargo in ships ..."
    print(repeater(phrase))
