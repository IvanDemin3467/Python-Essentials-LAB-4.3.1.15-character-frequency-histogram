# This is the Python Essentials 2 LAB 4.3.1.15 character-frequency-histogram
# A text file contains some text (nothing unusual)
# but we need to know how often (or how rare) each letter appears in the text.
# Such an analysis may be useful in cryptography,
# so we want to be able to do that in reference to the Latin alphabet.

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
        if ch not in characters:
            characters[ch] = 1  # If we got new char - add it to dict
        else:
            characters[ch] += 1 # If we got duplicate character - increment value in a dict

    # Sorting is here
    characters = {k: v for k, v in sorted(characters.items(), key=lambda item: item[0])}

    # Printing to cmd is here
    for entry in characters.items():
        print(entry[0] + " -> " + str(entry[1]))


if __name__ == "__main__":
    frequency_histogram("samplefile.txt")
    frequency_histogram("text.txt")
