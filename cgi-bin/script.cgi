#!/home/sepseel/anaconda3/bin/python
import spel
import os
import sys
import json

def new_game(size=5):
    status = {}
    status["board"] = spel.maakRooster(size)
    status["vlek"] = [tuple([0, 0])]
    status["moves"] = spel.zetten(status['board'])
    status["score"] = 0
    print(json.dumps(status))

def do_move(status, zet, coord=(0, 0)):
    board = spel.Spel(status)
    board.druppel(zet)
    print(json.dumps(board.status()))

def parse_query(query):
    for func in query.split('&'):
        f = func.split('=')[0]
        try:
            args = func.split('=')[1]
        except:
            args = ''
        args = args.replace('+', ', ') if isinstance(args, str) else args
        eval(f + '(' + args + ')')

def print_bord(status):
    for lijn in status['board']:
        print(lijn)


print("Content-type: text/json\nAccess-Control-Allow-Origin: *\n")
#query = os.environ.get("QUERY_STRING")
query = sys.argv[1]
parse_query(query)
