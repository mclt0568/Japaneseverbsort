# Japaneseverbsort
Sorts verbs of japanese that is in ます form into group 1,2 and 3(三段五段etc)

### Recommanded using Linux/Mac
Because the 'clear' command is executed to clear the terminal
for windows users: change `system("clear")` to `system("cls")` at line 5 will do.

### Try it online!
Try it online! [Click Here](https://repl.it/@Mclt0568/JapaneseVerbSort?language=python3&folderId=) brings you to the repl.it page of this project.

### How to use?
After running the script, you will need to input the japanese verb and press enter
**please dont put any spaces after/before/in between the verb**
**it has to be all in Hiragana**

### Word list?
Instead of input the japanese vocabs, it can also import a file **under the same directory** that contains a list of vocabs and sort them all in one shot. just type `#` and following with the filename.
**DO NOT** put empty lines in the wordlist file
you can put commant and it will ignore the line by putting `//` before the word
each line is one vocab

### Errors
If there is an Error, usually because you have entered a empty line.
But in other cases, it will show up like this:
```error occured on '(word you put in)'
due to the following reason
Reason of the error
```
and the python script will automatically stop after having an Error.
