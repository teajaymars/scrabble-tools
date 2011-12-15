import os

def load_dictionary(min_word_len, max_word_len, filename='/usr/share/dict/american-english'):
    with open(filename) as f:
        out = [line.rstrip() for line in f]
        # Strip the acronyms
        out = filter(lambda x: not x==x.upper(), out)
        # Strip the long words
        if max_word_len < 0:
            max_word_len = 8
        out = filter(lambda x: len(x)<=max_word_len, out)
        if min_word_len > 1:
            out = filter(lambda x: len(x)>=min_word_len, out)
        return out


def create_mnemonic(charlist, wordlist):
    '''Return an array of words from wordlist which covers all characters in charlist.'''
    def word_score(word):
        '''How many characters do these two strings have in common?'''
        return len(set(word).intersection(charlist))
    out = []
    while charlist:
        bestword = max(wordlist, key=word_score)
        if not bestword:
            print 'No further mnemonics can be found.'
            return []
        out.append(bestword)
        # Subtract the bestword from the remaining characters to cover
        charlist = charlist - set(bestword)
    return out


def get_subset_words(dictionary, charlist):
    return [word for word in dictionary if set(word).issubset(charlist)]


def main(charlist, min_word_len, max_word_len):
    charlist = set(charlist.lower())
    print "==> MnemonicFinder v1.0"
    print "--> Loading dictionary..."
    dictionary = load_dictionary(min_word_len, max_word_len)
    print "--> Search string:", charlist
    words = sorted(get_subset_words(dictionary, charlist), key=len)

    # Build some mnemonics
    print '--> Generating...'
    while True:
        mnemonic = create_mnemonic(charlist, words)
        if not mnemonic: break
        print "--> Mnemonic:", mnemonic
        words = filter(lambda x: not x==mnemonic[0], words)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Search the dictionary for mnemonic strings of words used to memorize a set of characters.')
    parser.add_argument('--charlist', metavar='characters', type=str, help='List of characters to memorize')
    parser.add_argument('--maxlen', dest='maxlen', default=-1, type=int, help='Longest permitted length of word')
    parser.add_argument('--minlen', dest='minlen', default=1,  type=int, help='Shortest permitted length of word')

    args = parser.parse_args()
    main(args.charlist, args.minlen, args.maxlen)
