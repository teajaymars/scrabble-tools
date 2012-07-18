
Scrabble Tools
==============

mnemonicfinder.py
------------------
    usage: mnemonicfinder.py [-h] [-v] [--dict DICTFILE] [--maxlen MAXLEN]
                             [--minlen MINLEN]
                             charlist

    Search the dictionary for mnemonic strings of words used to memorize a set of
    characters.

    positional arguments:
      charlist         List of characters to memorize

    optional arguments:
      -h, --help       show this help message and exit
      -v               Allow mnemonics to optionally use any vowels
      --dict DICTFILE  Dictionary file to use
      --maxlen MAXLEN  Longest permitted length of word
      --minlen MINLEN  Shortest permitted length of word

Example
-------
Using the tool to memorise the list "abdeghilmnrstwxy", which are all the valid letters to place after an A on the Scrabble board.

    $ python mnemonicfinder.py abdeghilmnrstwxy
    ==> MnemonicFinder v1.0
    --> Loading dictionary...
    --> Search string: abdeghilmnrstwxy
    --> Generating...
    --> Mnemonic: timberlands highway axe
    --> Mnemonic: disenthral bigamy wax
    --> Mnemonic: abridgment sixthly awe

Example: Free Vowels Mode
-------------------------
Using the tool to memorise the list "bdfhmnprswxy", which are all the *consonants* that can come after O on the Scrabble board. 

    $ python mnemonicfinder.py bdfhmnprswxy -v --dict dictcommon
    ==> MnemonicFinder v1.0
    --> Loading dictionary...
    --> Search string: bdfhmnprswxy
    --> Generating...
    --> Mnemonic: friends why box map
    --> Mnemonic: finished army box power
    --> Mnemonic: birds why fun map box
    --> Mnemonic: brown pushed may suffix
    --> Mnemonic: fresh body woman express

 * The `-v` option allows free use of vowels when searching for words.
 * This example uses the **dictcommon** word list, limiting the search to simple English words.

Results
-------

My first attempt is [documented here](https://gist.github.com/3137931) for postereity. I had limited success finding mnemonics for small word lists because of the lack of vowels; this led to the development of the later versions of the algorithm which include the `-v` option for free vowel use. (Obviously this requires a different system of memorisation; one that treats consonants and vowels separately).


