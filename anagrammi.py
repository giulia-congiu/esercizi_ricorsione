import copy
from functools import lru_cache


def anagrammi(parola):
    soluzioni = []
    ricorsione([], parola, soluzioni) #alla ricorsione passo un parziale e le soliuzioni
    return soluzioni

#definisco la funzione ricorsiva
def ricorsione(parziale: list, rimanenti: str, soluzioni: list) -> list:
    #il fatto che io per ogni argomento dico cosa mi aspetto che sia, è solo un indicazione, non obbligatorio in python
    #caso terminale
    if len(rimanenti) == 0:
        soluzioni.append(copy.deepcopy(parziale))
    #caso ricorsivo
    else:
        for i in range(len(rimanenti)): #rimanenti = DOG
            parziale.append(rimanenti[i]) #parziale = D
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:] #nuovi_rimanenti = OG
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop() #essendo liste mi serve il pop perchè parziale risulta sempre lo stesso ogetto che devo andare a modificare di volta in volta


'''altro modo che mi permette di evitare anagrammi ripetuti. 
(casa ad esempio avrà due volte 'casa' col metodo precedente)'''
def anagrammi_str(parola):
    soluzioni = set()
    ricorsione_str("", parola, soluzioni)
    return soluzioni

def ricorsione_str(parziale: str, rimanenti: str, soluzioni):
    #caso terminale
    if len(rimanenti) == 0:
        soluzioni.add(copy.deepcopy(parziale)) #la add di un set mi permette di avere oggetti unici
    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str(parziale+rimanenti[i], nuovi_rimanenti, soluzioni)
'''RICORDA: LE LISTE NON SONO HASHABLE, NON POSSO METTERLE NEL SET!!!'''


'''Con questa funzione invece che salvarmi le soluzioni con soluzioni = ... voglio
 solo stamparle'''
def anagrammi_str2(parola):
    ricorsione_str2("", parola)

@lru_cache(maxsize=None)
def ricorsione_str2(parziale: str, rimanenti: str):
    #caso terminale
    if len(rimanenti) == 0:
        print(parziale)
    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str2(parziale+rimanenti[i], nuovi_rimanenti)


if __name__ == '__main__':
    # print(anagrammi('casa'))
    #
    # print(anagrammi_str('casaaaaa'))

    anagrammi_str2('aaaa')