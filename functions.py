# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    return lst.count(element)

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    the=[]
    for x,y in dct.items():
        if y==value:
            the.append(x)
    return the

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    lst1+=lst2
    return sorted(lst1)

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    count=0
    if len(numbers)>1:
        for i in numbers:
            if i==max(numbers):
                count+=1
        if count<2:
            numbers.remove(max(numbers))
            return max(numbers)
        else:
            return None
    else:
            return None
    
    

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    count=0
    if len(str1)==(len(str2)):
        for i in str1:
            if i in str2:
                count+=1
        if count==len(str1):
            return True
    else:
        return False
def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    flat_list=[]
    if len(nested_list)>0:
        try:
            for i in nested_list:
                for x in i:
                    flat_list.append(x)
        except:
            for i in nested_list:
                flat_list.append(i)
    return flat_list


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    the=set(lst)
    return list(the)
def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    count=[]
    for i in lst1:
        if i in lst2:
            count.append(i)
    return count