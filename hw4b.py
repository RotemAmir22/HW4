def subset_sum_count_helper(ls, sm, current_sum_of_digits, index):
    """
    gets a list of numbers and a sum. checks if there is a inner combination of numbers that add up to the
    given number.

    :param ls: list of numbers (list[int])
    :param sm: wanted sum (int)
    :param current_sum_of_digits: sum of current added values (int)
    :param index: specific number to be checked (int)
    :return: number of combinations (int)
    """
    if index == len(ls):
        # reach value at end of list
        return 0
    if ls[index] + current_sum_of_digits == sm and index == len(ls) - 1:
        # current value added to current sum adds up to num and at the end of the list
        return 1
    if current_sum_of_digits == sm and index == len(ls) - 1:
        # reached wanted sum (without additional values) and reached the end of the list
        return 1
    if current_sum_of_digits + ls[index] > sm:
        # current sum is lagers than the wanted number
        return subset_sum_count_helper(ls, sm, current_sum_of_digits, index + 1)

    option1 = subset_sum_count_helper(ls, sm, current_sum_of_digits + ls[index], index + 1)
    # add the current number to the current sum
    option2 = subset_sum_count_helper(ls, sm, current_sum_of_digits, index + 1)
    # without the current number to the current sum

    return option1 + option2


def subset_sum_count(ls, sm):
    """
        gets a list of numbers and a number. checks if there is a inner combination of numbers that add up to the
        given number.

        :param ls: list of numbers (list[int])
        :param sm: wanted sum (int)
        :return: number of combinations (int)
        """
    if len(ls) == 0:
        # if the list has no numbers
        if sm == 0:  # from an empty list, can only get to the sum 0
            return 1
        return 0
    return subset_sum_count_helper(ls, sm, 0, 0)


def subset_sum_create_combination(ls, sm, index, temp_sum, combination, list_of_combinations):
    """
    goes over a list of numbers and finds different combinations that add up to a given sum.

    :param ls: list of number (list[int])
    :param sm: given sum
    :param index: place of specific number in list (int)
    :param temp_sum: temporary sum of specific numbers (int)
    :param combination: combination bering valued (list)
    :param list_of_combinations: list of final combinations (list[list])
    :return: updates list outside of function -> return none
    """
    if sm == temp_sum:  # if the temporary sum equals the desired sum
        list_of_combinations.append(combination)
        return
    if index == len(ls):  # if reached the end of the list
        return

    temp_combinations = [] + combination  # save combinations created during the recursion
    temp_combinations.append(ls[index])  # starts observing the list from given index
    subset_sum_create_combination(ls, sm, index + 1, temp_sum + ls[index], temp_combinations, list_of_combinations)
    # with the first number
    subset_sum_create_combination(ls, sm, index + 1, temp_sum, combination, list_of_combinations)
    # without the first number


def subset_sums(ls, sm):
    """
    gets a list of numbers and a sum and returns combination of numbers that add up to the sum.

    :param ls: list of number (list[int])
    :param sm: desired sum (int)
    :return: list of combination (list[list])
    """
    list_of_combinations = []  # empty list of final combination
    combination = []  # combination currently observed
    subset_sum_create_combination(ls, sm, 0, 0, combination, list_of_combinations)  # function helper
    return list_of_combinations


def subset_sum_memo_helper(ls, sm, index, temp_sum, memo):
    """
    gets a list of numbers and a sum and returns true if there is at least one combination of number that ad up to
    the given sum
    uses memoization, key is the current sum and index

    :param ls: list of numbers (list[int])
    :param sm: given sum (int)
    :param index: current place in list (int)
    :param temp_sum: current sum from specific number from list (int)
    :param memo: dictionary that stores if there is or isn't a combination with key: current sum and index (dict)
    :return: True if there is a combination, and False if there isn't (bool)
    """
    key = (index, temp_sum)
    if key not in memo:  # checks if there all ready is an answer to this specific combination of index and temp sum
        if index == len(ls):  # reached last index in list
            if temp_sum == sm:
                return True
            return False
        if temp_sum == sm:  # reach the sum goal
            return True
        if temp_sum > sm:
            return False
        option1 = subset_sum_memo_helper(ls, sm, index + 1, temp_sum + ls[index], memo)
        # with current number
        option2 = subset_sum_memo_helper(ls, sm, index + 1, temp_sum, memo)
        # without current number
        memo[key] = option1 or option2
        # update key
    return memo[key]


def subset_sum_memo(ls, sm):
    """
    gets a list of numbers and a sum and returns true if there is at least one combination of number that ad up to
    the given sum

    :param ls: list of numbers (list[int])
    :param sm: given sum (int)
    :return: if there is at least on combination -> True, of not False (bool)
    """
    if len(ls) == 0:
        # if the list has no numbers
        if sm == 0:  # from an empty list, can only get to the sum 0
            return True
        return False
    return subset_sum_memo_helper(ls, sm, 0, 0, {})  # function helper


def subset_sum_with_repeats_helper(ls, sm, index, combination, list_of_combinations):
    """
    gets a list of numbers and returns combinations of number that their sum reaches given sum.
    the combinations can have repetitions of the same specific number.
    e.g [1],5 -> 1+1+1+1+1 = 5

    :param ls: list of given numbers (lst[int])
    :param sm: given sum (int)
    :param index: current place in lst (int)
    :param combination: specific combination to reach sum (list[int])
    :param list_of_combinations: list that has all the combinations possible (list[list])
    :return: final list of combinations (list[list])
    """
    if index >= len(ls):  # if the index is not in range
        return []
    if sm == 0:  # reached goal of sum
        list_of_combinations.append(combination)  # adds current combination to list
        return
    if sm < 0:  # combination exceeds sum
        return []

    for index in range(len(ls)):  # want with repetitions of specific number - same index
        if sm < 0 or ls[index] == 0:  # if the number is 0 then no way possible to achieve sum
            index += 1  # only continues to next index if able to reach sum with current index
            break
        subset_sum_with_repeats_helper(ls, sm - ls[index], index, combination + [ls[index]], list_of_combinations)
        # with number in index

    subset_sum_with_repeats_helper(ls, sm, index + 1, combination, list_of_combinations)
    # without number in index


def subset_sum_with_repeats(ls, sm):
    """
    gets a list of numbers and returns combinations of number that their sum reaches given sum.
    the combinations can have repetitions of the same specific number.
    e.g [1],5 -> 1+1+1+1+1 = 5

    :param ls: list of numbers (list[int])
    :param sm: wanted sum (int)
    :return: list of combinations (list[list])
    """
    list_of_combinations = []
    combination = []
    subset_sum_with_repeats_helper(ls, sm, 0, combination, list_of_combinations)
    return list_of_combinations


def create_words(last_created, num, last_word):
    """
    creates a new word in range: last created -> last word.
    the letter in the new word are 'a,b,c'.
    to make the word the functions replaces the letters in turn starting from the last,
    then moves its way to the first letter while changing from the last letter in turn.
    eg: aaa -> change last letter -> aab
    or abc -> if change last letter we are out of range of letter so function changes one letter before -> aca

    :param last_created: first word in list (str)
    :param num: length of word, used as an index (int)
    :param last_word: last word in final list (str)
    :return: new word created (str)
    """
    new_word = ""  # starts with empty word
    if last_created == last_word:  # if it is te final word to create
        return last_created
    if last_created[num - 1] == "c":  # if the last letter is c, need to change X letters before it
        temp_word = list(last_created)  # create a temporary word to change 2 letters
        temp_word[num - 1] = "a"  # changes the last letter to be 'a'
        last_created = new_word.join(temp_word)  # updates the first word to be checked
        return create_words(last_created, num - 1, last_word)  # changes X letters before the last
    temp_word = list(last_created)
    if temp_word[num - 1] == "a":  # updates last letter
        temp_word[num - 1] = 'b'
    else:
        temp_word[num - 1] = 'c'  # if last letter is c -> handled before
    return new_word.join(temp_word)


def create_list_of_words(num, last_word, list_of_new_words):
    """
    creates a list of new word that their length is num and add them to a list.
    ends creating the words once it reaches the last word.
    the new words are made up of 'a,b,c' and are in lexicographic order

    :param num: length of word (int)
    :param last_word: last word in final list (str)
    :param list_of_new_words: adds to here all the new words (list[str])
    :return: list of new words (list[str])
    """
    last_created = list_of_new_words[-1]  # the last word created -> last word in list
    new_word = create_words(last_created, num, last_word)  # function helper-> creates new word
    if new_word == last_created:  # no additional words required
        return list_of_new_words
    list_of_new_words.append(new_word)  # adds the new words to the list
    return create_list_of_words(num, last_word, list_of_new_words)


def abc_words(num):
    """
    gets number of characters in a word and creates new words using 'a,b,c'.
    the length of the word is num.
    returns a list of words in lexicographic ways

    :param num: length of new words (int)
    :return: list of new words (list[str])
    """
    list_of_new_words = []  # list of new words- empty at first
    first_word = "a" * num  # easy to create first word
    last_word = "c" * num  # easy to create last word
    list_of_new_words.append(first_word)  # add the first word to the new list
    create_list_of_words(num, last_word, list_of_new_words)  # function helper -> creates list of words
    return list_of_new_words


def create_words_from_char_to_char(last_created, num, ch1, ch2, last_word):
    """
    creates a new word in range: last created -> last word.
    the letter in the new word are from ch1 to ch2 = alphabet of words
    to make the word the functions replaces the letters in turn starting from the last,
    then moves its way to the first letter while changing from the last letter in turn.
    eg: aaa -> change last letter -> aab
    or abc -> if change last letter we are out of range of letter so function changes one letter before -> aca

    :param last_created: last word in list of new words (str)
    :param num: length of words (int)
    :param ch1: first character in alphabet of words (str)
    :param ch2: last character in alphabet of words (str)
    :param last_word: last word to create (str)
    :return: new words (str)
    """
    new_word = ""  # empty word
    if last_created == last_word:
        return last_created
    if last_created[num - 1] == ch2:  # if last letter is the same as the last letter in alphabet
        temp_word = list(last_created)  # starts to change X letter before last
        temp_word[num - 1] = ch1
        last_created = new_word.join(temp_word)
        return create_words_from_char_to_char(last_created, num - 1, ch1, ch2, last_word)
    temp_word = list(last_created)
    last_letter = temp_word[num - 1]
    if last_letter == ch2:  # checks last letter, and changes it accordingly
        return new_word.join(temp_word)
    temp_word[num - 1] = chr(ord(last_letter) + 1)
    return new_word.join(temp_word)


def create_list_from_char_to_char(num, ch1, ch2, last_word, list_of_new_words):
    """
    creates a list of new words using the specific alphabet -> ch1 to ch2

    :param num: length of new words (int)
    :param ch1: first letter of specific alphabet (str)
    :param ch2: last letter of specific alphabet (str)
    :param last_word: last letter to create (str)
    :param list_of_new_words: list of new words (lst[str])
    :return: list of new words (lst[str])
    """
    last_created = list_of_new_words[-1]  # last word created in list
    new_word = create_words_from_char_to_char(last_created, num, ch1, ch2, last_word)  # function helper
    if new_word == last_created:  # if its the last word to create
        return list_of_new_words
    list_of_new_words.append(new_word)
    return create_list_from_char_to_char(num, ch1, ch2, last_word, list_of_new_words)


def char_to_char_words(ch1, ch2, num):
    """
    creates new words with a specific alphabet (ch1-ch2) that are the length of num.
    returns the words in lexicographic order.

    :param ch1: first letter in alphabet (str)
    :param ch2: last letter in alphabet (str)
    :param num: length of words (int)
    :return: list of new words (lst[str])
    """
    if ch1 == ch2:  # same letter
        return [ch1 * num]
    list_of_new_words = []  # list of new words- empty at first
    first_word = ch1 * num  # easy to create first word
    last_word = ch2 * num  # easy to create last word
    list_of_new_words.append(first_word)  # add the first word to the new list
    create_list_from_char_to_char(num, ch1, ch2, last_word, list_of_new_words)  # function helper
    return list_of_new_words


def valid_box(maze, next_box, current_box):
    """
    checks if the value of the next box is smaller than the current box
    also checks if the next box is in the maze

    :param maze: given maze (list[list])
    :param next_box: indexes of next box (list[row,column])
    :param current_box: value of current box (int)
    :return: if the next box is valid to go to returns True (bool)
    """
    if 0 <= next_box[0] < len(maze) and 0 <= next_box[1] < len(maze[0]):  # in maze
        if maze[next_box[0]][next_box[1]] > current_box:  # bigger than current box
            return True
    return False


def solve_maze_helper(maze, row_index, column_index, path):
    """
    gets a maze, row index and column index and checks if there is a path to get from one edge of maze to the other.
    the path can only advance by going through boxes that their values are larger than the previous
    updates the path into list path.

    :param maze: given maze(list[list])
    :param row_index: row index (int)
    :param column_index: column index (int)
    :param path: path found (list[list])
    :return: returns True if there is a path and False if there isn't (bool)
    """
    if row_index == len(maze) - 1 and column_index == len(maze[0]) - 1:  # reached end of maze
        path.insert(0, [row_index, column_index])
        return True
    if valid_box(maze, [row_index, column_index + 1], maze[row_index][column_index]):  # goes to the right box
        if solve_maze_helper(maze, row_index, column_index + 1, path):
            path.insert(0, [row_index, column_index])
            return True
    elif valid_box(maze, [row_index + 1, column_index], maze[row_index][column_index]):  # goes one box down
        if solve_maze_helper(maze, row_index + 1, column_index, path):
            path.insert(0, [row_index, column_index])
            return True
    elif valid_box(maze, [row_index, column_index - 1], maze[row_index][column_index]):  # goes to the left box
        if solve_maze_helper(maze, row_index, column_index - 1, path):
            path.insert(0, [row_index, column_index])
            return True
    elif valid_box(maze, [row_index - 1, column_index], maze[row_index][column_index]):  # goes one box up
        if solve_maze_helper(maze, row_index - 1, column_index, path):
            path.insert(0, [row_index, column_index])
            return True
    return False


def solve_maze_monotonic(maze):
    """
    get a maze and checks if there is a path that goes from box [0,0] to the left bottom corner box.

    :param maze: given maze (list[list])
    :return: path (list[list])
    """
    path = []
    solve_maze_helper(maze, 0, 0, path)
    return path
