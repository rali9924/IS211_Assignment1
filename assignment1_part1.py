def listDivide(numbers, divide = 2):
    count = 0
    for n in numbers:
        if n % divide == 0:
            count = count + 1
    return count

class ListDivideException(Exception):
    def init(self):
         default_message = 'Test Has Failed!'
         super().init(default_message)


def testListDivide():
    if (listDivide([1,2,3,4,5]) != 2):
        raise ListDivideException
    else:
        print(listDivide([1,2,3,4,5]))

    if (listDivide([2,4,6,8,10]) != 5):
        raise ListDivideException
    else:
        print(listDivide([2,4,6,8,10]))

    if (listDivide([30,54,63,98,100], divide=10) != 2):
        raise ListDivideException
    else:
        print(listDivide([30,54,63,98,100], divide=10))

    if (listDivide([]) != 0):
        raise ListDivideException
    else:
        print(listDivide([]))

    if (listDivide([1,2,3,4,5], 1) != 5):
        raise ListDivideException
    else:
        print(listDivide([1,2,3,4,5], 1))
testListDivide()