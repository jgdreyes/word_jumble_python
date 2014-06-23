word_jumble_python
==================

Word Jumble Solver written in Python


## How to Run

```
$ ./bin/jumble
Please enter a word like `fruit` to see possible jumbles.

$ ./bin/jumble <word>
Possible Combinations for: <word>
[...]
```


## Implementation Notes
- Filters both input and dictionary values for [a-z]
- Dictionary lookup against scowl-7.1/final

  ```
  $ cat english-words.10 english-words.20 english-words.35 english-words.40 english-words.50 > all_english_words.txt
  ```

## Instructions
Can you create a program to solve a word jumble?  The program should accept a string as input, and then return a list of words that can be created using the submitted letters.  For example, on the input "dog", the program should return a set of words including "god", "do", and "go".
 
Please implement the program in Python but refrain from using any helper
modules or imports (e.g. itertools). In order to verify your words, just
download an English word list (here are a few - http://wordlist.aspell.net/).  Then upload your program to GitHub or Gist, and send it back!
