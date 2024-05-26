def swap(a, b):
    num_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    a_word = num_to_word.get(a, str(a))
    b_word = num_to_word.get(b, str(b))

    return a_word, b_word