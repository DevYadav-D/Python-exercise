def random_number():
    import random
    #a=list(range(1,101))       #create the list of range 1 to 100
    result=random.choice(list(range(1,101)))
    return result

def random_int():
    import random
    return random.randint(1,100)
