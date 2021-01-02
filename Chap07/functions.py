
def main():
    kitten()


def kitten():
    print('Meow.')



if __name__ == '__main__': main()



def main():
    kitten(5,6,7)


def kitten(a,b,c = 1):
    print('Meow.')
    print(a,b,c)


if __name__ == '__main__': main()


def main():
    x = 5
    kitten(x)
    print (f'in main: x is {x}')


def kitten(a):
    print('Meow.')
    print(a)

if __name__ == '__main__': main()


def main():
    x = 5
    print(id(x))
    kitten(x)
    print (f'in main: x is {x}')


def kitten(a):
    print(id(a)) # id of a is the same as x
    a =  3
    print(id(a)) # id of a is changed
    print('Meow.')
    print(a)

if __name__ == '__main__': main()


def main():
    x = 5
    y = x
    y = 3

    print(id(x))
    print(id(y))
    print(x)
    print(y)



if __name__ == '__main__': main()


def main():
    x = [5]
    y = x
    y [0] = 3 # when i changed it in one place it gets changed in both y and y. Because it is one object

    print(id(x))
    print(id(y))
    print(x)
    print(y)



if __name__ == '__main__': main()



def main():
    x =[5]
    print(id(x))
    kitten(x)
    print (f'in main: x is {x}')


def kitten(a):
    a[0] = 3
    print('Meow.')
    print(a)

if __name__ == '__main__': main()


def main():
    x = kitten()
    print(type(x),x)


def kitten():
    print('Meow.')


if __name__ == '__main__': main()



def main():
    x = kitten()
    print(type(x),x)


def kitten():
    print('Meow.')
    return 42


if __name__ == '__main__': main()



def main():
    x = kitten()
    print(type(x),x)


def kitten():
    print('Meow.')
    return [42,43]


if __name__ == '__main__': main()



def main():
    x = kitten()
    print(type(x),x)


def kitten():
    print('Meow.')
    return dict(x = 42, y = 43)


if __name__ == '__main__': main()