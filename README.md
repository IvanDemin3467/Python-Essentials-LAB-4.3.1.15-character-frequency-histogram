# Python-Essentials-LAB-4.3.1.15-character-frequency-histogram
**Objectives**

•	improving the student's skills in operating with files (reading)

•	using data collections for counting numerous data.
**Scenario**

A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

•	asks the user for the input file's name;

•	reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)

•	prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:
```
aBc
```
samplefile.txt

the expected output should look as follows:
```
a -> 1
b -> 1
c -> 1
```

#Python-Essentials-LAB-4.3.1.15-character-frequency-histogram

**Objectives**

•	improve the student's skills in operating with files (reading/writing)

•	using lambdas to change the sort order.
**Scenario**

The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

•	the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)

•	the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:
```
cBabAa
```
*samplefile.txt*

the expected output should look as follows:
```
a -> 3
b -> 2
c -> 1
```
*output*

Tip: Use a lambda to change the sort order.
