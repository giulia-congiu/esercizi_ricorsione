def palyndrome(word):
    #terminale
    if len(word) <=1 :
        return True
    #non terminale
    else:
        #controllo se prima e ultima sono uguali
        return word[0] == word[-1] and palyndrome(word[1:-1])

def palyndrome_banale(parola):
    return parola[::-1] == parola

if __name__ == "__main__":
    print(palyndrome('casa')) #dovrebbe dare false
    print(palyndrome('civic')) #dovrebbe dare true

    print(palyndrome_banale('civic'))
    print(palyndrome_banale('casa'))