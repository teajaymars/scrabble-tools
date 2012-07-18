import os
from string import ascii_lowercase

def load_dictionary(min_word_len, max_word_len, filename='/usr/share/dict/american-english'):
    lower = set(ascii_lowercase)
    with open(filename) as f:
        outiter = (line.rstrip() for line in f)
        loweriter = (word for word in outiter if all(c in lower for c in word))
        return [word for word in loweriter if min_word_len <= len(word) <= max_word_len]


def create_mnemonic(charlist, wordlist):
    '''Return an array of words from wordlist which covers all characters in charlist.'''
    def word_score(word):
        '''How many characters do these two strings have in common?'''
        return len(set(word).intersection(charlist))
    out = []
    wordlist = set(wordlist)
    while charlist:
        try:
            bestword = max(wordlist, key=word_score)
        except ValueError:
            print 'No further mnemonics can be found.'
            return []
        out.append(bestword)
        # Subtract the bestword from the remaining characters to cover
        charlist = charlist - set(bestword)
        wordlist = wordlist - set([bestword])
    return out


def get_subset_words(dictionary, charlist):
    return [word for word in dictionary if set(word).issubset(charlist)]


def main(charlist, min_word_len, max_word_len, dictfile):
    print "==> MnemonicFinder v1.0"
    print "--> Loading dictionary..."
    dictionary = load_dictionary(min_word_len, max_word_len, dictfile)
    print "--> Search string:", charlist
    charlist = set(charlist.lower())
    words = sorted(get_subset_words(dictionary, charlist), key=len)

    # Build some mnemonics
    print '--> Generating...'
    while True:
        mnemonic = create_mnemonic(charlist, words)
        if not mnemonic: break
        print "--> Mnemonic:", mnemonic
        i = words.index(mnemonic[0])
        words = words[:i] + words[i+1:]


if __name__ == '__main__':
    import argparse, sys
    parser = argparse.ArgumentParser(description='Search the dictionary for mnemonic strings of words used to memorize a set of characters.')
    parser.add_argument('charlist', type=str, help='List of characters to memorize'),
    parser.add_argument('--dict', default='./dict', dest='dictfile', type=str, help='Dictionary file to use'),
    parser.add_argument('--maxlen', default=8, type=int, help='Longest permitted length of word'),
    parser.add_argument('--minlen', default=1,  type=int, help='Shortest permitted length of word'),
    arg = parser.parse_args()
    main(arg.charlist, arg.minlen, arg.maxlen, arg.dictfile)
