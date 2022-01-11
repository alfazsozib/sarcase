#!/bin/python3

def staircase(n):
    for i in range(n+1):
        print(i*'#')
        for j in range(n-i):
            print('',end=' ')
    
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
