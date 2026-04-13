from time import sleep

def countdown(n):
    while n >= 0:
        print(n)
        sleep(1) #fa una pausa di 1 secondo
        n -= 1

def countdown_recursive(n):
    #condizione terminale
    if n==0:
        print("Stop")
    #condizione non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)

if __name__ == '__main__':
    N = 4
    print("countdown_recursive")
    countdown_recursive(N)
