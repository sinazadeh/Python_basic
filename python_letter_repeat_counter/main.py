import funcs

letter = "i"
word = "Mississippi"
text = "Mississippi Mississippi"

# The number of repeated word in a text
print(funcs.word_counter(text, word))
# The number of repeated letter in a word
print(funcs.letter_counter(word, letter))
# The number of repeated letter in a text
print(funcs.letter_counter(text, letter))