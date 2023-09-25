# this function analyze code submissions.
# this function takes code represented as a string as its only parameter

def validate(s):
    
    if 'def' not in s:
        return 'missing def'
    elif ':' not in s:
        return 'missing :'
    elif '(' and ')' not in s:
        return 'missing paren'
    elif '('+')' not in s:
        return 'missing param'
    elif '    ' not in s:
        return 'missing indent'
    elif 'validate' not in s:
        return 'wrong name'
    elif 'return' not in s:
        return 'missing return'
    else:
        return True


a=validate(
    "def validate(s):\nif 'def' not in s:\n return 'missing def'\n elif ':' not in s:\n return 'missing :'\n elif '(' and ')' not in s:\n return 'missing paren'\n elif '()' in s:\n return 'missing param'\n elif '    ' not in s:\n return 'missing indent'\nelif 'validate' not in s:\nreturn 'wrong name'\nelif 'return' not in s:\nreturn 'missing return'\nelse:\nreturn True"
    )

