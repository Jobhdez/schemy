
from parser import (
    parser,
    Program,
    Nil,
    Exps,
    Exp,
    Prim,
    If,
    Bool,
    Begin,
    While,
    Let,
    SetBang,
    Int,
    Op,
    Binding,
    Var,
)
def interp(exp, env):

    match exp:
        case Exps(e):
            result = None
            for i in e:
                result = interp(i, env)
            return result
        
        case Exp(e):
            return interp(e, env)
        
        case Bool(b):
            return b
        
        case If(cnd, thn, els):
            match interp(cnd, env):
                case "#t":
                    return interp(thn, env)
                case "#f":
                    return interp(els, env)
                
        case Prim(Op(oper), e, e2):
            match oper:
                case 'and':
                    match interp(e, env):
                        case '#t':
                            match interp(e2, env):
                                case '#t':
                                    return '#t'
                                case '#f':
                                    return '#f'
                        case '#f':
                            return '#f'
                        
                case 'or':
                    match interp(e, env):
                        case '#t':
                            return '#t'
                        case '#f':
                            match interp(e2, env):
                                case '#t':
                                    return '#t'
                                case '#f':
                                    return '#f'
                                
                case '+':
                    return interp(e, env) + interp(e2, env)
                
                case '-':
                    return interp(e, env) - interp(e2, env)
        case Int(n):
            return n
        
        case Var(e):
            return env[e]
        
        case Let(Binding(Var(var), e), body_exp):
            env[var] = interp(e, env)
            return interp(body_exp, env)
        
        case SetBang(var, e):
            env[var.var] = interp(e, env)
            
        case Begin(Exps(exps)):
            expressions = exps[:-1]
            length = len(exps)
            last_exp = exps[length-1]
            for i in expressions:
                interp(i, env)

            return interp(last_exp, env)
        
        case _:
            raise ValueError(f'Parse node {exp} is not valid node.')
        
        
            
def repl(prompt='lambda> '):
    while True:
        tree = parser.parse(input(prompt))
        val = interp(tree, {})
        return val 
        
