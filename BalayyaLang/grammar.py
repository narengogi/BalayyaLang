import re


class Grammar:
    PREPOSITIONS = re.compile('(tho)|(loninchi)|(loki)')
    PLUS = re.compile('jo+din?c+hu|k(u|o)+dinc+hu')


class Tokens:
    NUM = 'NUM'
    PLUS = 'PLUS'
    MULTIPLY = 'MULTIPLY'
    MINUS = 'MINUS'
    DIVIDE = 'DIVIDE'
