# Write a Python program to find the list of words that are longer than n from a given list of words.

def function(n,str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

print(function(3, "The quick brown fox jumps over the lazy dog"))