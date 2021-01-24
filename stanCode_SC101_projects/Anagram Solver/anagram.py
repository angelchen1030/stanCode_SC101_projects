"""
File: anagram.py
Name: Angel Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dict_list = []


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')

    while True:
        read_dictionary()
        s = input("Find anagrams for: ").lower()
        if s == EXIT:
            break
        else:
            letter = []
            for item in s:
                letter.append(item)
            find_anagrams(letter)


def read_dictionary():
    """
    To read every letter from dictionary.
    """
    with open(FILE, 'r') as f:
        for line in f:
            dict_list.append(line.strip())


def find_anagrams(s):
    """
    :param s: (list) The word input by user
    """
    final_lst = []
    anagram_helper(s, [], final_lst)
    print(str(len(final_lst)) + " anagrams: " + str(final_lst))


def anagram_helper(lst, current_lst, final_lst):
    """
    :param lst:          (list) The word input by user
    :param current_lst:  (list) The permutations of the word
    :param final_lst:    (list) All the anagram(s) for the word
    """
    if len(lst) == len(current_lst):  # Base case
        letter = ""
        for num in current_lst:
            index = int(num)
            letter += lst[index]
        if letter in dict_list:
            if letter not in final_lst:
                print("Searching...")
                final_lst.append(letter)
                print("Found: " + letter)
    else:
        for i in range(len(lst)):
            if i in current_lst:
                pass
            else:
                # Choose
                current_lst.append(i)

                # Explore
                anagram_helper(lst, current_lst, final_lst)

                # Un-choose
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:(list)
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for item in dict_list:
        if item.startswith("".join(sub_s)):
            return True


if __name__ == '__main__':
    main()
