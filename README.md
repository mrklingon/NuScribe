# NuScribe
Microbit programs for a simple translation of Bible verses.

Originally coded in Makecode: https://makecode.microbit.org/_bpsPKrA7dRa8

## Program description
The program has two Bible verses, Isaiah 26:3 and John 3:16 from the King James version.
Clicking "A" steps through five modes (below). Clicking on "B" initiates the mode action.

* SI - Show the Isaiah text
* SJ - Show the John text
* MX - refresh the "translation matrix"
* TI - Show the "translated" text of Isaiah 26:3
* TJ - Show the "translated" text of John 3:16

## Relexification process
When the program starts, an array of generated words is created, one for each of the English words in the two verses. When called to "translate" the program goes word-by-word through the verse providing the generated word. **Important:** This is not a real translation, but more of a coded-English approach.

## Creating the words
The mkWrd() uses three inputs

```
 rules = ["CVC", "CV", "CVCVC"]
 cons = "tdkp"
 vow = "aeiouy"
 ```

To create a word, it chooses at random a "rule", then replaces each C in the rule with a random consonant and each V with a random vowel. This function can be updated with different or more rules. Also the vowels and consonants can be edited. For example if you added a string of "eeee" to the vowels, it would increase the likelihood of "e" being a vowel used.

## Re-Coding in Python
To rewrite the progam in Python, I changed the Makecode to display the Makecode version in Python. Then I went to https://python.microbit.org and copied pieces from Makecode to the Python editor. *Note:* the Python displayed by Makecode needed editing to get the program to work. One bonus of the python.microbit IDE is the scrolling of text can be sped up, making it less tedious.

### Bonus Python Feature
The python.microbit editor has a "speech" library! That lets you have the device "speak" your text. I added a toggle to turn it on/off (default = off). Touching the microbit logo toggles the feature - briefly showing a "butterfly" icon for "ON" and "sleepy face" for "OFF"

