from nodes import Exps

def flatten_exps(node):
    expressions = []
    match node:
        case Exps(e):
            return flatten_exps(e)
            
        case [*exps]:
            for exp in exps:
                expressions.extend(flatten_exps(exp))
        
        case _:
            expressions.append(node)

    return expressions
