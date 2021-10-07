
def nested(data, key):
    
    key_bits = key.split('/')
    
    for key_bit in key_bits:
        if key_bit not in data:
            return None

        data = data[key_bit]

    return data


def printing_tests():
    #Case 1: is the normal scenario where you should return 'a'
    obj = {"x": {"y": {"z": "a"}}}
    key = 'x/y/z'

    res = nested(obj, key)
    print(f'Case: obj = {obj}, key: {key}, results is: {res}')

    # Case 2: if the key is wrong it should return 'None'
    obj = {"x": {"y": {"z": "a"}}}
    key = 'x/y/z/w'
    res = nested(obj, key)
    print(f'Case: obj = {obj}, key: {key}, results is: {res}')

    # Case 3: if the object is empty it should return 'None'
    obj = {}
    key = 'a/b/c'
    res = nested(obj, key)
    print(f'Case: obj = {obj}, key: {key}, results is: {res}')

    # Case 4 if the key is empty it should return 'None'
    obj = {"x": {"y": {"z": "a"}}}
    key = ''
    res = nested(obj, key)
    print(f'Case: obj = {obj}, key: {key}, results is: {res}')


def asserting_tests():
    #Case 1: assume key = 'a / b / c' and obj is this
    obj = {"x": {"y": {"z": "a"}}}
    key = 'x/y/z'
    res = nested(obj, key)
    assert res == 'a'

    # Case 2:
    obj = {"x": {"y": {"z": "a"}}}
    key = 'x/y/z/w'
    res = nested(obj, key)
    assert res is None

    # Case 3:
    obj = {}
    key = 'a/b/c'
    res = nested(obj, key)
    assert res is None

    # Case 4
    obj = {"x": {"y": {"z": "a"}}}
    key = ''
    res = nested(obj, key)
    assert res is None


if __name__ == '__main__':

    while True:
        inpt = input('How do you want to test? Printing (1) or Asserting (2)')
        if inpt == '1':
            printing_tests()
            break
        elif inpt == '2':
            asserting_tests()
            break
        else:
            print ("Please enter 1 or 2")
            continue