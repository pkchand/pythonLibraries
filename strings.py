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
    words=str.split(" ")
    new_str=""
    for i in range(len(words)-1,-1,-1):
        new_str=new_str+" "+words[i]
    print(new_str.strip())

def occurance_of_Char(str, char):
    """take a string and a charachter then find how many time that character repeated in that string"""

def reverse_string_without_space_location(str):
    """takes a string and reverse it without tthe position of space"""

def string_subset(str1, str2):
    """takes a string and checks if that string contains a separately given string"""


def swap_case(s):
    str=""
    for i in s:
        if i.isalpha():
            if i.islower():
                i=i.upper()
            else:
                i=i.lower()
        str+=i
            
    print(str)


def split_and_join(line):
    # write your code here
    spilted=line.split(" ")
    result=""
    for i in spilted:
        result=result+i+"-"
    print(result.strip("-"))

split_and_join("This is my country")

#swap_case("ok Bye")

#reverse_words_in_sentense("sly fox jumps over the fence")
#reverse_string("determined")
#count_vowels("jump over the building")


