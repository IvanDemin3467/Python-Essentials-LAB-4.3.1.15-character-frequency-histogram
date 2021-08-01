# This is the Python Essentials 2 LAB 4.3.1.16 sorted-character-frequency-histogram
# A text file contains some text (nothing unusual)
# but we need to know how often (or how rare) each letter appears in the text.
# The previous code needs to be improved. It's okay, but it has to be better.
# Your task is to make some amendments, which generate the following results:
# •	the output histogram will be sorted based on the characters' frequency
#       (the bigger counter should be presented first)
# •	the histogram should be sent to a file with the same name as the input one,
#       but with the suffix '.hist' (it should be concatenated to the original name)


from os import strerror

def frequency_histogram(file):
    # This function opens file and creates character frequency histogram
    print(file)
    characters = {}             # A dict to store histogram
    # File open is here
    try:
        s = open(file, "rt")
        content = s.read()
        s.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

    # Histogram creation is here
    for ch in content:
        ch = ch.lower()
        if not ch.isalpha():
            continue
        if ch not in characters:
            characters[ch] = 1  # If we got new char - add it to dict
        else:
            characters[ch] += 1 # If we got duplicate character - increment value in a dict

    # Sorting is here
    # It returns dictionary, sorted by value
    # "key" is a function that serves as a key for the sort comparison
    # "lambda item: item[1]" - function that returns value of dict item
    # "reverse = True" - enables reverse sorting
    characters = {k: v for k, v in sorted(characters.items(),
                                          key = lambda item: item[1],
                                          reverse = True)}

    # Printing to cmd is here
    for entry in characters.items():
        print(entry[0] + " -> " + str(entry[1]))
        

    # Printing to file is here
    try:
        s = open(file+".hist", "wt")
        for entry in characters.items():
            s.write(entry[0] + " -> " + str(entry[1]) + "\n")
        s.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))


def user_input():
    # This function prompts user to input name of file
    return input("Input name of file to process: ") 
    


if __name__ == "__main__":
    frequency_histogram("samplefile.txt")
    frequency_histogram("text.txt")
