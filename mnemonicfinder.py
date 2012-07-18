import os
from string import ascii_lowercase

def load_dictionary(min_word_len, max_word_len, filename):
    lower = set(ascii_lowercase)
    check_range = lambda(word) : min_word_len <= len(word) <= max_word_len
    check_lowercase = lambda(word) : all(c in lower for c in word)
    with open(filename) as f:
        all_words = (line.rstrip() for line in f)
        return filter(check_lowercase, filter(check_range, all_words) )

def create_mnemonic(charset, wordlist):
    '''Return an array of words from wordlist which covers all characters in charset.'''
    # Inner function: How many characters do these two strings have in common?
    word_score = lambda(word) : len(set(word).intersection(charset))
    out = []
    while charset:
        try:
            bestword = max(wordlist, key=word_score)
        except ValueError:
            print 'No further mnemonics can be found.'
            return []
        out.append(bestword)
        # Subtract the bestword from the remaining characters to cover
        charset = charset - set(bestword)
    return out

def subset_words(dictionary, charlist, use_vowels):
    if use_vowels:
        charlist = charlist.union( set('aeiou') )
    is_subset = lambda(word) : set(word).issubset(charlist)
    return filter(is_subset, dictionary)

def main(charlist, min_word_len, max_word_len, dictfile, use_vowels):
    print "==> MnemonicFinder v1.0"
    print "--> Loading dictionary..."
    dictionary = load_dictionary(min_word_len, max_word_len, dictfile)
    print "--> Search string:", charlist
    charset = set(charlist.lower())
    words = sorted( subset_words(dictionary, charset, use_vowels) , key=len)
    # Build some mnemonics
    print '--> Generating...'
    while True:
        mnemonic = create_mnemonic(charset, words)
        if not mnemonic: break
        print '--> Mnemonic:', ' '.join(mnemonic)
        i = words.index(mnemonic[0])
        words = words[:i] + words[i+1:]

if __name__ == '__main__':
    import argparse, sys
    parser = argparse.ArgumentParser(description='Search the dictionary for mnemonic strings of words used to memorize a set of characters.')
    parser.add_argument('charlist', type=str, help='List of characters to memorize'),
    parser.add_argument('-v', dest='use_vowels', action="store_true", default=False, help='Allow mnemonics to optionally use any vowels')
    parser.add_argument('--dict', default='./dict', dest='dictfile', type=str, help='Dictionary file to use'),
    parser.add_argument('--maxlen', default=8, type=int, help='Longest permitted length of word'),
    parser.add_argument('--minlen', default=1,  type=int, help='Shortest permitted length of word'),
    arg = parser.parse_args()
    main(arg.charlist, arg.minlen, arg.maxlen, arg.dictfile, arg.use_vowels)
