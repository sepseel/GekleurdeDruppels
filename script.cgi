#!/home/sepseel/anaconda3/bin/python
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


def parse_querry(query):
    for func in query.split('&'):
        f = func.split('=')[0]
        try:
            args = func.split('=')[1]
        except:
            args = ''
        args = args.replace(';', ', ') if isinstance(args, str) else args
        return eval(f + '(' + args + ')')
        


def print_bord(status):
    for lijn in status['board']:
        print(lijn)

print("Content-type: text/plain\n")
query = os.environ.get("QUERY_STRING")


