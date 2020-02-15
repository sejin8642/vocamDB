# to update dictinoary.txt

def main():
    # extract text file, dictionary, and studied words
    fname = input('Enter the txt file name without txt extension to add to update: ')
    text = open(fname + '.txt', 'r').read()
    text = text.split()
    fdict = open('dictionary.txt', 'r').read()
    fdict = fdict.split()
    
    combined = text + fdict
    combined.sort()
    
    # obtain the new words list as txt file
    with open('dictionary.new.txt', 'w') as newD:
        for word in combined:
            print(word, file=newD)

main()
