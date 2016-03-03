def boil():
    pass

def cutting():
    pass

def mix():
    pass

def put():
    pass

def prepare(order="борщ украинский"):
    if not isinstance(order, str):
        return None
    elif order[:4] == 'борщ':
        return [cutting, put, boil]
    else:
        return None

assert prepare("борщ украинский")  == [cutting, put, boil]
assert prepare("борщ")  == [cutting, put, boil]
assert prepare("чай")  == None
assert prepare(4)  == None

