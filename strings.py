def count_vowels(str):
    count=0
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    print(count)

def reverse_string(str):
    """reverse a given string"""
    rev_str=""
    for i in range(len(str)-1,-1,-1):
        rev_str+=str[i]
    print(rev_str)

def reverse_words_in_sentense(str):
    """takes a string and reverses its words. i.e. hello world is going to be world hello"""
    



reverse_string("determined")
#count_vowels("jump over the building")

