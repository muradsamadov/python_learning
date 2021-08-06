#  Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def function(lst):
    max_str = lst[0]

    for x in lst:
        if len(x) > len(max_str):
            max_str = x

    print(max_str)
    print(len(max_str))
    

function(["php", "exercises", "backend"])