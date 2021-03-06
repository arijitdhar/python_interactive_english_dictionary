__author__ = '220152'

import json
import mysql.connector
from difflib import get_close_matches


with open("data.json") as data:
    dictionary = json.load(data)

def get_word_definition(word):
    word = word.lower()

    # Create connection object
    con = mysql.connector.connect(
        user = "root",
        password = "root",
        host = "127.0.0.1",
        database = "arijit_study"
    )


    # Create cursor from connection object
    cur = con.cursor()

    # Execute cursor with a sql
    cur.execute("SELECT COUNT(1) FROM dictionary")




    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    else:
        matches = get_close_matches(word, dictionary.keys(), cutoff=0.8)

        if len(matches) > 0:
            confirmation = input("Did you mean {}? Y/N: ".format(matches[0]))
            if confirmation.upper() == 'Y':
                return dictionary[matches[0]]
            elif confirmation.upper() == 'N':
                return "The word does not exist. Please double check it!"
            else:
                return "We didn't understand your entry"
        else:
            return "The word does not exist. Please double check it!"

word = input("Enter a word: ")
definitions = get_word_definition(word)

if type(definitions) == list:
    for definition in definitions:
        print(definition)
else:
    print(definitions)
