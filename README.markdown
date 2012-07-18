
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

Results
-------

My first attempt is [documented here](https://gist.github.com/3137931) for postereity. I had limited success finding mnemonics for small word lists because of the lack of vowels; this led to the development of the later versions of the algorithm which include the `-v` option for free vowel use. (Obviously this requires a different system of memorisation; one that treats consonants and vowels separately).


