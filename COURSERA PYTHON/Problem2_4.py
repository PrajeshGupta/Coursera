import random

def problem2_4():
    lis=[]
    random.seed(70)
    for i in range(10):    
        n = 30 + (35-30)*random.random()
        lis.append(n)
    print(lis)    