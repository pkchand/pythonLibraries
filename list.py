import random
from collections import Counter

friends=["Papri","Pralay", "Sanath", "Prama", "Siva"]
selected_person=random.choice(friends)
#print(selected_person)

randon_index=random.randint(0, len(friends)-1)
#print(friends[randon_index])

def sort_array(arr):
    """sorting array by accending order"""
    arr.sort()
    print(arr)

def sort_by_occurance(arr):
    """sort the array by occurance"""
    arr.sort(key=Counter(arr).get, reverse=True)
    print(arr)
arr1=[4,8,9,6,5,7,2,4,2,2,9,5,5,5]
sort_array(arr1)
sort_by_occurance(arr1)
# arr1.sort()
# print(arr1)