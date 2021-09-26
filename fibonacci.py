print ('DE RIJ VAN FIBONACCI!')
a = int(input('HOEVEEL GETALLEN IN DE RIJ WIL JE?: '))

def fibonacci(n):
    a, b = 0, 1
    for getallen in range(n):
        yield a                 #vervang RETURN met YIELD, het geeft een generator object terug en exit de function niet!
        a, b = b, a + b         # het geeft je een lijst met nummers terug die een loop is

print(list(fibonacci(a)))