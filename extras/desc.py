def descend_numbers_in_words(num):
    num_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    print("Natural descending order of {} is:".format(num), end=" ")
    while num >= 0:
        print(num_to_word.get(num, str(num)), end=" ")
        num -= 1