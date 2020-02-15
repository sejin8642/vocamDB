# delimiter.py

def main():
    # extract text file and dictionary
    fname = input('Enter the txt file name without txt extension: ')
    text = open(fname + '.txt', 'r').read()
    
    # list words from the text file
    text = text.lower()
    for ch in '’‘~!@#$%^&*()_—+-=[]{};:"“,.<>/?\|”0123456789©à':
        text = text.replace(ch, ' ')
    words = text.split()
    words = list(set(words))
    words.sort()
    
    # compare the text to the dictionary words to sift study words
    dictionary = [w for w in words]

    # obtain the new words list as txt file
    with  open('dictionary.new.txt', 'w') as outfile:
         for nw in dictionary:
             print(nw, file=outfile)

main()
