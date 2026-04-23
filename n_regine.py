import copy
from time import time

class Regina():
    def __init__(self, riga, col):
        self.riga = riga
        self.col = col

class NRegine():
    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []

    #=======================================APPROCCIO 2=================================
    '''Rappresentiamo soluzione come un vettore di N regine,
    # ognuno rappresentante una regina come riga e colonna (Riga, colonna) della posizione della reg.'''
    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0 # conto le soluzioni che trovo e le chiamate alla ricorsiva che faccio
        self.soluzioni = []
        self._ricorsione2([], N) # rappresento il parziale iniziale come una lista vuota

    # parziale è un vettore di coppie (riga, colonna) che rappresentano ognuno la pozione della regina
    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1

        #caso terminale: ho messo N regine
        if len(parziale) == N:
            # if self._is_soluzione(parziale): #mi dice se la soluzione a cui sono arrivato è valida o no (ma potrebbero esserci duplicati)
            #     self.n_soluzioni += 1
            #     print(parziale)
            if self._is_nuova_soluzione(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            # print(parziale)
        #caso ricorsivo: ho messo < N regine
        else:
            for riga in range(N):
                for col in range(N):
                    # verifico già qua se la nuova regina sia ammissibile
                    nuova_regina = (riga, col)
                    if self._step_is_valid(nuova_regina, parziale):
                        # aggiungi pezzetto di soluzione in parziale
                        parziale.append(nuova_regina)
                        # andare avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        # backtracking
                        parziale.pop()

    '''
    Senza questa funzione nelle soluzioni vengono ammesse soluzioni con la stessa configurazione
    della scacchiera ma scritte in ordine diverso, quindi molte delle soluzioni saranno duplicati.
    Per risolvere confrontiamo la soluzione potenziale con tutte quelle già trovate
    # se è diversa, restituiamo True, altrimenti False'''
    def _is_nuova_soluzione(self, soluzione_potenziale) -> bool:
        N = len(soluzione_potenziale)
        for soluzione in self.soluzioni:
            counter = 0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                    counter += 1
            if counter == N:
                return False
        return True

    '''Funzione che controlla se la nuova regina da inserire sia ammissibile rispetto alla
    # soluzione parziale costruita finora. In questo modo diminuisco il tempo di esecuzione, 
    ma ammetto lo stesso i duplicati'''
    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale: #confronto la nuovaregina con tutte quelle che ho in parziale
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True


    ''' Funzione che prende due regine e restituisce True se non si possono posizionare insieme, 
    perchè si mangerebbero, altrimenti, restituisce False'''
    def _is_pair_admissible(self, regina1, regina2) -> bool: #regina 1 è quella che ho,
        ## voglio verificare che la posizione dell'altra non sia in corrispondenza delle mosse dell'altra
        #1) verifico la riga. Se non va bene, return False
        if regina1[0] == regina2[0]:
            return False
        #2) verifico la colonna. Se non va bene, return False
        if regina1[1] == regina2[1]:
            return False
        #3) verifico diagonale 1. Se non va bene, return False
        '''Ricorda che una diagonale verso il basso in  una scacchiera ha (indiceColonna - indiceRiga = costante)'''
        # per fare questa verifica devo controllare che:
        # colonna di regina1 - riga di regina1 == colonna di regina2 - riga di regina 2
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False
        #4) verifico diagonale 2. Se non va bene, return False
        '''Ricorda che una diagonale verso l'alto ha (indiceColonna + indiceRiga = costante)'''
        # per fare questa verifica devo controllare che:
        # colonna di regina1 + riga di regina1 ==  colonna di regina2 + riga di regina2
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False
        #5) Ho passato tutti i controlli, return True
        return True

    ''' Metodo che data una possibile soluzione (lista con N regine) verifica se sia ammissibile
     e restituisce True se ammissibile, False se non ammissibile. Il problema è che:
     in questo modo abbasso il numero di soluzioni ma resta invariato il numero di esecuzione, 
     perchè questa funzione controlla l'ammissibilità solo alla fine. 
     Si può trovare un modo per vederlo già da prima infatti per farlo ho scritto _step_is_valid e uso quello'''
    def _is_soluzione(self, soluzione_possibile) -> bool:   #-> bool non è obblig. metterlo
        for i in range(len(soluzione_possibile)-1): #ottimizzazione del ciclo annidato, si scrive cosi
            for j in range(i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False
        return True

if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    nreg.solve2(6)
    end_time = time()

    print(f"Elapsed time = {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")
    print(nreg.soluzioni)