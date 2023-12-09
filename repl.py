from parser import parser
from interp import interp

env = {}
def repl(prompt='lambda> '):
    while True:
        tree = parser.parse(input(prompt))
        val = interp(tree, env)
        print(val)
