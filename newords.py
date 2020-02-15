# newords.py

def main():
    # extract text file, dictionary, and studied words
    fname = input('Enter the txt file name without txt extension: ')
    text = open(fname + '.txt', 'r').read()
    fdict = open('dictionary.txt', 'r').read()
    fdict = fdict.split()
    fstd = open('studied.txt', 'r').read()
    fstd = fstd.split()
    
    # list words from the text file
    text = text.lower()
    for ch in """'`’‘~!@#$%^&*()_—+-=[]{};:"“,.<>/?\|”0123456789©à•■▪♦‹""":
        text = text.replace(ch, ' ')
    words = text.split()
    words = list(set(words))
    words.sort()
    
    # compare the text to the dictionary words to sift study words
    study = [w for w in words if w not in fdict]
    
    # compare the study words to the studied to sift new and review words
    newords = [w for w in study if w not in fstd]
    studied = [w for w in study if w in fstd]
    
    # obtain the new words list as txt file
    vocab = open(fname + '.Vocab.txt', 'w')
    for nw in newords:
        print(nw, file=vocab)
    vocab.close()
    
    # obtain the review words list as txt file
    review = open(fname + '.Review.txt', 'w')
    for nw in studied:
        print(nw, file=review)
    review.close()

main()
