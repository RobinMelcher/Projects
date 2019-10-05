import random

def NSidedDie(n):
    # finish this function
    randomNumber = random.randint(1, n)
    return randomNumber
    
def DiceRoller(n, t):
    # finish this function
    sum = 0
    for i in range(t):
       sum = sum + NSidedDie(n)
    return sum
       
    
    
    
####TESTS - DO NOT MODIFY###    
def TestDie(n):
    sum = 0
    for i in range(100):
        sum = sum + NSidedDie(n)
    sum /= 100
    print("Average for " + str(n) + " sided die: " + str(sum))
    return abs(sum - (n/2)) <= 1
    
def RunTests():
    print("Test 1: ", "succeded" if TestDie(6) else "failed")
    print("Test 2: ", "succeded" if TestDie(12) else "failed")
    print("Test 3: ", "succeded" if TestDie(20) else "failed")
    
#RunTests()
input_t = int(input("how many die?:"))

print(DiceRoller(20, input_t)/ input_t)
