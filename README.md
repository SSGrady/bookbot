# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! 

bookbot returns the word and character count of a book of your choosing given the complete body of text.

## Requirements
Must have some version of python 3.x

## Clone with SSH
Run the following commmand to clone the repo
```
git clone git@github.com:SSGrady/bookbot.git
```

## Running bookbot
bookbot requires 2 command line arguments. It follows that a user should upload their own corpus of a book if they want to use bookbot for data analysis.

E.g. onboarding workflow,
 - Create a `books/` directory
 - Go to [Project Gutenberg](https://www.gutenberg.org/) and save the plain text UTF-8 of a book in their library
 - Say we picked mobydick and added it to `books/`
 - Run:
 
 `python3 main.py books/mobydick.txt`


 ## Example Output
 Continuing the moby dick example:

 ```py
 ============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 215838 total words
--------- Character Count -------
e: 119351
t: 89874
a: 79226
o: 70809
n: 66782
i: 66675
s: 65138
h: 63769
r: 53593
l: 43351
d: 38840
u: 27205
m: 23626
c: 23319
w: 22557
g: 21287
f: 21252
p: 17873
y: 17244
b: 17203
v: 8725
k: 8228
q: 1581
j: 1178
x: 1064
z: 636
æ: 23
œ: 5
é: 5
è: 3
ח: 1
ו: 1
ϰ: 1
η: 1
τ: 1
ο: 1
ς: 1
â: 1
============= END ===============
 ```
