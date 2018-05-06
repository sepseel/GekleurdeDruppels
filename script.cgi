#!/usr/bin/env python
import spel
import os

def new_game(size=5):
    status = {}
    status['board'] = spel.maakRooster(size)
    status['vlek'] = [(0, 0)]
    status['moves'] = spel.zetten(status['board'])
    status['score'] = 0
    return status


def do_move(status, zet, coord=(0, 0)):
    board = spel.Spel(status)
    board.druppel(zet)
    return board.status()


def print_bord(status):
    for lijn in status['board']:
        print(lijn)
#status = new_game()
#print_bord(status)
#for i in range(10):
#    print('*'*20)
#    print('zet: ', status['moves'][0])
#    status = do_move(status, status['moves'][0])
#    print_bord(status)


print("Content-type: text/plain\n")
querys = os.environ.get("QUERY_STRING")
querys = querys.split('&')
print(querys)
