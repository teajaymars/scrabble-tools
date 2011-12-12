import os

def load_dictionary():
    f = file('dict')
    out = f.readlines()
    # Strip the newlines
    out = map(lambda x: x[:-1], out)
    # Strip the acronyms
    out = filter(lambda x: not x==x.upper(), out)
    # Strip the long words
    out = filter(lambda x: len(x)<=8, out)
    return out

def uniqueletters(chars):
    x=1
    while x<len(chars):
        chars=chars[:x] + chars[x:].replace(chars[x-1],'')
        x+=1
    return chars

def intersect(word, charlist):
    '''How many characters do these two strings have in common?'''
    word = uniqueletters(word)
    count = 0
    for key in word:
        if key in charlist: count+=1
    return count

def create_mneumonic(charlist, wordlist):
    '''Return an array of words from wordlist which covers all characters in charlist.'''
    out = []
    while len(charlist):
        best=0
        bestword = ''
        for word in wordlist:
            score = intersect(word,charlist)
            if score > best:
                best = score
                bestword = word
        if not len(bestword):
            raise ValueError, 'the mneumonic cannot be completed.'
        out.append(bestword)
        # Subtract the bestword from the remaining characters to cover
        for key in bestword:
            charlist = charlist.replace(key,'')
    return out


def get_subset_words(dictionary, charlist):
    out = []
    for word in dictionary:
        for letter in word:
            if not letter in charlist: break
        else:
            out.append(word)
    return out


def main(charlist):
    charlist = charlist.lower()
    charlist = uniqueletters(charlist)
    print "==> MemoryAid v1.0"
    print "--> Loading dictionary..."
    dictionary = load_dictionary()
    print "--> Search string:", charlist
    words = get_subset_words(dictionary, charlist)

    # Sort words by length
    def comparator(a,b):
        return len(a)-len(b)

    # Process the word list
    words.sort(cmp=comparator)

    # Build some mneumonics
    print '--> Generating...'
    while True:
        mneumonic = create_mneumonic(charlist, words)
        print "--> Mneumonic:", mneumonic
        words = filter(lambda x: x not in mneumonic, words)

if __name__=='__main__':
    import sys
    try:
        charlist = sys.argv[1]
    except:
        print "Usage:", sys.argv[0],"collection_of_letters"
    else:
        main(charlist)

