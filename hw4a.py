def is_palindrom_no_helper(st):
    """
    gets a string a checks if it is a palindrome by comparing two letters from the beginning and end of the string

    palindrome-> string which reads the same backward as forward

    :param st: string to be checked (str)
    :return: if it is a palindrome -> returns True, if not-> False (bool)
    """
    # enter your answer here
    if st == "" or not st:  # base case: went over all pairs in the list
        return True
    if st[0] != st[-1]:
        return False
    return is_palindrom_no_helper(st[1:-1])


def is_palindrom_with_helper(st):
    """
    gets a string an checks if its a palindrome
    palindrome-> string which reads the same backward as forward

    :param st: string to be checked (str)
    :return: if it is a palindrome -> returns True, if not-> False  (bool)
    """
    # enter your answer here
    return pilandrom_helper(st, 0, len(st) - 1)  # calls helper function


def pilandrom_helper(st, first_index, last_index):
    """
    gets a string and two indexes to evaluate if they are the same

    :param st: string to check (str)
    :param first_index: index from beginning of string (starts at 0, then 1..) (int)
    :param last_index: index from end of string (starts at len(st)-1 and continues down) (int)
    :return: if all the pairs are the same -> returns True, if not-> False  (bool)
    """
    if first_index * 2 >= len(st):  # base case, went over half of the string
        return True
    if st[first_index] != st[last_index]:
        return False
    return pilandrom_helper(st, first_index + 1, last_index - 1)


def is_palindrom_no_spaces(st):
    """
    checks to see if the string is a palindrome without counting the spaces
    palindrome-> string which reads the same backward as forward

    :param st: text to be checked (str)
    :return: if the text is a palindrome -> True, if not-> False  (bool)
    """
    # enter your answer here
    return pilandrom_no_spaces_helper(st, 0, len(st) - 1, len(st))


def pilandrom_no_spaces_helper(st, first_index, last_index, stop_criteria):
    """
    compares the values in given index, without comparing spaces

    :param st: text ot be checked (str)
    :param first_index: index of value with a char, not space to be checked (from beginning to end) (int)
    :param last_index: index of value with a char, not space to be checked (from end to beginning) (int)
    :param stop_criteria: length of text to be checked (without spaces) (int)
    :return: if the text is palindrome -> True, if not-> False  (bool)
    """
    if first_index * 2 >= stop_criteria:  # base case-> gone over half of the string, not counting spaces
        return True
    if st[first_index] == " ":  # checks for spaces from the beginning of the string
        stop_criteria += 1
        return pilandrom_no_spaces_helper(st, first_index + 1, last_index, stop_criteria)
    if st[last_index] == " ":  # checks for spaces from the end of the string
        stop_criteria -= 1
        return pilandrom_no_spaces_helper(st, first_index, last_index - 1, stop_criteria)
    if st[first_index] != st[last_index]:
        return False
    return pilandrom_no_spaces_helper(st, first_index + 1, last_index - 1, stop_criteria)


def weighted_average(grades):
    """
    gets a list of tuples and calculates the weighted average.
    tuple in list: first index of tuple-> grade
                   second index of tuple -> weight
    weighted average formula ->
    sum of: (grade * weight in each tuple) / sum of: weight in each tuple

    :param grades: list of grades and weights (list(tuple(grade, weight)))
    :return: returns the average with no more than 2 number after the decimal, rounded (int/float)
    """
    # enter your answer here
    if len(grades) == 0 or len(grades[0]) == 0:  # empty list, or empty tuple
        return 0
    return round(weighted_average_helper_get_grades_sum(grades, 0) / weighted_average_helper_get_weight_sum(grades, 0),
                 2)  # two helping functions for this calculation


def weighted_average_helper_get_grades_sum(grades, index):
    """
    sums the solution of the grades times the weight in each tuple.

    :param grades: list of tuples(grade, weight) (list(tuple))
    :param index: which tuple in list to add to the calculation (int)
    :return: sum of the solution of: grades * weight in each tuple (int)
    """
    if index == len(grades):  # base case: end of the list
        return 0
    return (grades[index][0] * grades[index][1]) + weighted_average_helper_get_grades_sum(grades, index + 1)


def weighted_average_helper_get_weight_sum(grades, index):
    """
    sums the weights of the list (values of the second index in tuple)

    :param grades: list of tuples(grade, weight) (list(tuple))
    :param index: which tuple in list to add to the calculation (int)
    :return: sum of all the weights in the tuples from list (int)
    """
    if index == len(grades):  # base case: end of the list
        return 0
    return (grades[index][1]) + weighted_average_helper_get_weight_sum(grades, index + 1)


def is_prime(num):
    """
    gets a number and checks if its a prime number.
    the numbers are whole and bigger than 1
    prime number-> the number can only be divided by itself and 1 with no remainder

    :param num: number to be checked (int)
    :return: if the number is a prime number -> True, if not-> False  (bool)
    """
    # enter your answer here
    if 1 < num <= 3:  # if the number is 3 or smaller then it is a prime number, no calculations required
        return True
    if num == 1:
        return False
    return is_prime_helper(num, 2)  # function helper


def is_prime_helper(num, divider):
    """
    checks if dividing a number by another has a remainder.

    :param num: number checked (int)
    :param divider: number to divide the input number with (int)
    :return: if there is no remainder then -> True, if not-> False  (bool)
    """
    if divider == num:  # base case: if the number and divider are the same then the answer has no remainder
        return True
    if num % divider == 0:  # checks if there is a remainder
        return False
    return is_prime_helper(num, divider + 1)


def is_perfect(num):
    """
    checks if sum of all the given numbers dividers equal the number itself

    :param num: number to be checked (int)
    :return: if the sum of the dividers equal the number -> True, if not-> False  (bool)
    """
    # enter your answer here
    if num == 1:  # if the input number is one
        return True
    elif num == is_perfect_helper(num, 1, 0):  # function helper
        return True
    return False


def is_perfect_helper(num, divider, sum_of_dividers):
    """
    gets a number and sums all its dividers

    :param num: get a number and calculates its dividers (int)
    :param divider: number to divide the input number with (int)
    :param sum_of_dividers: sums the dividers (int)
    :return: sum of dividers (int)
    """
    if num == divider:  # base case: if the number an divider are the same
        return sum_of_dividers
    if num % divider == 0:
        sum_of_dividers += divider
    return is_perfect_helper(num, divider + 1, sum_of_dividers)


def is_7_boom(num):
    """
    gets a number and checks if it has the digit 7 or can be divided by 7 with no remainder

    :param num: number to be checked (int)
    :return: if there is the number 7 or can be divided by 7 -> True, if not-> False  (bool)
    """
    # enter your answer here
    if num % 7 == 0:  # if the number can be divided by 7
        return True
    return is_7_bool_helper_has_7(num)  # function helper


def is_7_bool_helper_has_7(num):
    """
    checks if the digit 7 is in the number

    :param num: number to be checked (int)
    :return: if the digit 7 is in the number -> True, if not-> False  (bool)
    """
    if not num:
        return False
    if num % 10 == 7:
        return True
    return is_7_bool_helper_has_7(num // 10)
