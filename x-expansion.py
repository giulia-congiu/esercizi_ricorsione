import copy

class XExpansion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    # QUI ho definito la soluzione parziale come una STRINGA
    def calcola(self, input):
        self.soluzioni = [] #stai attenta a rimettere a 0 le soluzioni altrimenti ogni volta le salva e le aggiunge
        self._ricorsione("", input) #stringa

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            self.soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])


    # QUI ho definito la soluzione parziale come una LISTA
    def calcola_list(self, input):
        self.soluzioni_list = []
        self._ricorsione_list([], input) # lista

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione_list(self, parziale: list, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0: #controllo finale per vedere se è finito
            # print(parziale)
            self.soluzioni_list.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X': #se il rimanente è x
                for c in ["0", "1"]: #ciclo sui valori possibili
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop() #tolgo 0 per metterci 1
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])

        '''quando il parziale è implementato come una lista invece che come una stringa,
        bisogna stare attenti che quando si va a inserire la soluzione parziale nelle soluzioni (soluzioni_list) e
         a fare poi il pop di parziale per creare l'altra soluzione con 1, non si crea un altra istanza ma queste operazioni 
         operano tutte sullo stesso oggetto in memoria. Quindi è come se stessi continuando sempre a modificare lo stesso parziale.
         Per risolvere questo problema al posto di ( soluzioni.append(parziale) ) devo fare ( self.soluzioni_list.append(copy.deepcopy(parziale)) )
         Esso prende la lista parziale e ne crea una uguale IN MEMORIA e salva quella nelle soluzioni
        '''

#======================================================================
#======================================================================
#======================================================================
#posso scrivere la stessa cosa in modo diverso con la stringa
def x_expansion2(input):
    soluzioni = []

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale: str, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            soluzioni.append(parziale)
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                ricorsione(parziale + '0', rimanenti[1:])
                ricorsione(parziale + '1', rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni


if __name__ == '__main__':
    sequenza = "01X"
    xexp = XExpansion()

    #metodo con soluzioni parziali rappresentate come stringhe
    xexp.calcola(sequenza)
    print(xexp.soluzioni)

    #metodo con soluzioni parziali rappresentate come liste
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)