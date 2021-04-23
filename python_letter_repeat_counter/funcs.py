def slicer(text):
    list = []
    for i in range(len(text)):
        list.append(text[i])
    return list

def word_counter(text, word):
    list = text.split()
    number_of_repeated_word = list.count(word)
    return number_of_repeated_word

def letter_counter(text, letter):
    list = slicer(text)
    number_of_repeated_letter = list.count(letter)
    return number_of_repeated_letter