#!/home/sepseel/anaconda3/bin/python
##!/usr/bin/env python

from spel import Spel
import cgitb
import os
import json

# geef meer informatie weer bij een request,
# zoals error boodschappen
#cgitb.enable()

def new_game(size=5):
    """
    start een niew spel met de opgegeven grootte
    """
    game = Spel(0, None, size, new=True)
    print(json.dumps(game.state()))

def do_move(status, zet, coord=(0, 0)):
    """
    maakt een zet op de opgegeven status met de gegeven kleur,
    en geeft de nieuwe status trug
    """
    game = Spel(status["score"], status["board"], 5, status["vlek"])
    game.druppel(zet)
    print(json.dumps(game.state()))

def parse_query(query):
    """
    vertaald de query string naar een uitvoerbare functie, 
    en voert deze uit
    """
    for func in query.split('&'):
        f = func.split('=')[0]
        try:
            args = func.split('=')[1]
        except:
            args = ''
        args = args.replace('%22', '"').replace("%27", "'").replace('+', ', ') if isinstance(args, str) else args
        eval(f + '(' + args + ')')

def print_bord(status):
    """
    print het spelbord uit naar de console 
    (voor debugging)
    """
    for lijn in status['board']:
        print(lijn)

print("Content-type: text/json\nAccess-Control-Allow-Origin: *\n")
query = os.environ.get("QUERY_STRING")
parse_query(query)
