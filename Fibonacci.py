from time import time


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}


    def calcola_elemento_cache(self, n):
        #se ho già la soluzione per questo n la prendo dalla cache
        if self.cache.get(n) is not None: #ottengo un valore oppure none. Se ottengo un valore lo rido
            return self.cache[n]
        #altrimenti devo andare avanti con la ricorsione
        else:
            self.cache[n] =self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2)
            #se non era nella cache me lo metto dentro e lo potrò riusare
            return self.cache[n]

    def calcola_elemento(self, n):
        #caso terminale
        if n== 0:
            return 0
        elif n == 1:
            return 1
        #caso ricorsivo
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

if __name__ == '__main__':
    N = 30
    fib = Fibonacci()

    start_time = time()
    print(f'Sequenza di fibonacci di {N} = {fib.calcola_elemento(N)}')
    end_time = time()
    print(f'Elapsed time - recursion: {end_time - start_time}')

    start_time = time()
    print(f'Sequenza di fibonacci di {N} = {fib.calcola_elemento_cache(N)}')
    end_time = time()
    print(f'Elapsed time - cache: {end_time - start_time}')