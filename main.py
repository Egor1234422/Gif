from Ytoc import Character

plaplayer1 = Character(name='Vasya', health=100, damage=1,defence=3)
plaplayer2 = Character(name='Petya', health=150, damage=1,defence=3)

print(f'  - Player1 - \n{plaplayer1}')
print(f'  - Player2 - \n{plaplayer2}')

plaplayer1.attack(plaplayer2)
print('Player1 attack Player2')
plaplayer2.attack(plaplayer1)
print('Player2 attack Player1')

print(f' -Player1 - \n{plaplayer1}')
print(f' -Player2 - \n{plaplayer2}')
from Ytoc import Character

plaplayer1 = Character(name='Vasya', health=100, damage=1,defence=3)
plaplayer2 = Character(name='Petya', health=150, damage=1,defence=3)

print(f'  - Player1 - \n{plaplayer1}')
print(f'  - Player2 - \n{plaplayer2}')

plaplayer1.attack(plaplayer2)
print('Player1 attack Player2')
plaplayer2.attack(plaplayer1)
print('Player2 attack Player1')

print(f' -Player1 - \n{plaplayer1}')
print(f' -Player2 - \n{plaplayer2}')
