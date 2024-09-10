# Declare and Call a function

def average(a: int, b: int) -> float:
    c = 0.0             # declare variable c
    c = (a + b) / 2.0
    return c

x, y = 3, 8
z = 0.0           # declare variable z
z = average(x, y) # varaible c is assigned to variable z

# Declare and Call a function

def calculateWinner(team1: str, score1: int, team2: str, score2: int) -> str:
    print("LOOK AT THIS: ", score1 - score2)
    global giraffe
    giraffe = "Very big"
    if score1 > score2:
        return team1
    elif score2 > score1:
        return team2
    else:
        return 'Tied'
    
t1 = input("Team 1's name: ")
s1 = int(input("Team 1's score: "))
t2 = input("Team 2's name: ")
s2 = int(input("Team 2's score: "))


winner = calculateWinner(team2=t1, score2=s1, team1=t2, score1=s2) # keyword: swaps variables
winner2 = calculateWinner(t1, s1, t2, s2)                          # positional: maintains variables

print("The Winner is ")
print('a')
print(giraffe)
