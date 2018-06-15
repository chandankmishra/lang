###########################################################
# Problem : Print all permutations of a string, array
###########################################################


def pertmutation(nlst, start):
    if start == len(nlst) - 1:
        print(nlst)
        return

    for i in range(start, len(nlst)):
        nlst[start], nlst[i] = nlst[i], nlst[start]
        pertmutation(nlst, start + 1)
        nlst[start], nlst[i] = nlst[i], nlst[start]


nlst = [1, 2, 3]
pertmutation(nlst, 0)

###########################################################
# Problem: There is an array with half even and half odd integers.
#           Print permutation with odd and even as alternative start from odd.
###########################################################
'''
STEP #1 First normalize the array in the form of alternative odd and even (starting with odd)
STEP #2 Boundry conditions when i == n-1 print and return
STEP #3
        1. Check if the start position and the loop variable is valid. if valid index & value then
        2. swap the start index with the loop variable
        3. call permutation with start+ 1 index
        4. Restore the array
'''


def odd_even_value_ok_at_position(val, index):
    if (val % 2 == 0 and index % 2 == 1) or (val % 2 == 1 and index % 2 == 0):
        return True
    return False


def pertmutation_odd_even(nlst, start):
    if start >= len(nlst) - 1:
        print(nlst)
        return

    for i in range(start, len(nlst)):
        if odd_even_value_ok_at_position(nlst[i], start):
            nlst[start], nlst[i] = nlst[i], nlst[start]
            pertmutation_odd_even(nlst, start + 1)
            nlst[start], nlst[i] = nlst[i], nlst[start]


nlst = [1, 2, 3, 4]
#pertmutation_odd_even(nlst, 0)

###########################################################
# Problem: There is an array with half even and half odd integers.
#           Print permutation with odd and even as alternative start even odd.###########################################################


def even_odd_value_ok_at_position(val, index):
    if (val % 2 == 1 and index % 2 == 1) or (val % 2 == 0 and index % 2 == 0):
        return True
    return False


def pertmutation_even_odd(nlst, start):
    if start >= len(nlst) - 1:
        print(nlst)
        return

    for i in range(start, len(nlst)):
        if even_odd_value_ok_at_position(nlst[i], start):
            nlst[start], nlst[i] = nlst[i], nlst[start]
            pertmutation_even_odd(nlst, start + 1)
            nlst[start], nlst[i] = nlst[i], nlst[start]


nlst = [1, 2, 3, 4]
#pertmutation_even_odd(nlst, 0)

###########################################################
# Problem: Assume that the input is an array of characters.
#          Print any one permutation that is also a word in the dictionary.
###########################################################


def print_dictionary_word_pertmutation(nlst, start):
    if start >= len(nlst) - 1:
        if IsValidDictionaryWord(nlst):
            print(nlst)
            return True
        else:
            return False

    for i in range(start, len(nlst)):
        if even_odd_value_ok_at_position(nlst[i], start):
            nlst[start], nlst[i] = nlst[i], nlst[start]
            # Note here we first add swap the start with j and then check
            # if the prefix is valid. We do not check for prefix witout
            # swapping the charactor!!!
            if ValidWordPrefix(nlst, start + 1):
                if print_dictionary_word_pertmutation(nlst, start + 1):
                    return True
            nlst[start], nlst[i] = nlst[i], nlst[start]
