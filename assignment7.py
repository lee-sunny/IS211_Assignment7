#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment7
Game: Pig
"""

import argparse
import random
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IS211_Assignment7
Game: Pig
"""


class Die:
    def __init__(self):
        self.rolled = 0
        self.values = [1, 2, 3, 4, 5, 6]
        random.seed(0)
    def roll_die(self):
        self.rolled = random.choice(list(range(1, 7)))
        return self.rolled
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hold = False
        self.roll = False
        self.score = 0
    def hold_or_roll(self):
        choice = input('\nIf you want to roll, enter "r". If you want to hold, enter "h": ')
        if choice.lower() == 'h':
            self.hold = True
            self.roll = False
        elif choice.lower() == 'r':
            self.roll = True
            self.hold = False
        else:
            print('\n\tPlease enter either"r" or "h". All other entries are invalid.')
            self.hold_or_roll()
    def win(self):
        if self.score >= 100:
            return True

class Pig:
    def __init__(self, total_players):
        self.total_players = total_players
        self.players = []
        self.die = Die()
        self.highest_score = 0
        self.running_score = 0
        for num in range(1, total_players + 1):
            self.players.append(Player('Player {}'.format(num)))
        self.counter = 0
        self.current_player = self.players[self.counter]
        while not self.current_player.win():
            print('=======================')
            print('\n{}\'s turn'.format(self.current_player.name))
            print('=======================')
            print('SCORES:')
            print('Points for this turn: {}'.format(self.running_score))
            for player in self.players:
                print('\n   {}\'s Score: {}'.format(player.name, player.score))
            self.current_player.hold_or_roll()
            if self.current_player.roll:
                self.die.roll_die()
                print('\n\n\n{} ROLLED A {}! '.format(self.current_player.name, self.die.rolled))
                if self.die.rolled == 1:
                    self.running_score = 0
                    self.counter += 1
                    if self.counter < len(self.players):
                        self.current_player = self.players[self.counter]
                        print('YOUR TURN ENDED BECAUSE YOU ROLLED A ONE!'.format(self.current_player.name))
                    else:
                        self.counter = 0
                        self.current_player = self.players[self.counter]
                        print('YOUR TURN ENDED BECAUSE YOU ROLLED A ONE!'.format(self.current_player.name))
                else:
                    self.running_score += self.die.rolled
                    print('IF YOU HOLD NOW, YOU CAN ADD {} TO YOUR SCORE.'.format(self.running_score))
            else:
                self.current_player.score += self.running_score
                self.running_score = 0
                if self.current_player.score > self.highest_score:
                    self.highest_score = self.current_player.score

                if self.current_player.win():
                    print('\n\tGAME OVER, {} WINS!!'.format(
                        self.current_player.name))
                    exit()
                else:
                    self.counter += 1
                    if self.counter < len(self.players):
                        self.current_player = self.players[self.counter]
                    else:
                        self.counter = 0
                        self.current_player = self.players[self.counter]


def main():
    parser = argparse.ArgumentParser(description='total number of players')
    parser.add_argument('--numPlayers', default=2, type=int, help='total number of players')
    args = parser.parse_args()
    if args.numPlayers < 2:
        print('\nThe game of Pig requires at least two players.')
    else:
        Pig(args.numPlayers)

if __name__ == '__main__':
    main()
