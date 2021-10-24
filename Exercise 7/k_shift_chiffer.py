import math

def create_alphabet():

    table = []

    for i in range(0, 26):
        table[chr(ord("A") + i)] = i