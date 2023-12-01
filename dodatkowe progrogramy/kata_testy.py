"""beats = {
        'scissors' : 'paper',
        'paper' : 'rock',
        'rock' : 'scissors'
    }


keys1 = beats.keys()
print(keys1)
print(type(keys1))

print(beats.items())
x = beats.items()
print(type(x))
#beats[p1] == p2
      

aaa = beats ['scissors']
print(aaa)
print(type(aaa))"""

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]



result = rps('rock', 'scissors')
print(result)









def prs(p1, p2):
    list1 = { 
        'scissors' : 0,
        'rock' : 1,
        'paper' : 2
    }

    scores = {
        0 : 'Draw!',
        1 : 'Player 1 won!',
        2 : 'Player 2 won'
    }

    zmienna = scores[list[p1] - list[p2]]
    return zmienna

result = rps('rock', 'scissors')
print(result)