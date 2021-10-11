
#print('ola')

a = 'string'
b = 1
c = '1111'
d = []
e = [1, 'o', 'pp']
f = {'key': 90, 'b': 80}
g = (1, 1)

# --------- if
#if 0 == b:
#    print(e)
#if 1 == b:
#    print(g)
#    print(e)

# --------- if-else
#if '1' == c:
#    print(c)
#elif '11' == c:
#    print(d)
#else:
#    print('ups')


# --------- FOR
#for i in e:
#    print(i)
    
#for i in range(1,6):
#    print(i)
    
#for k,v in f.items():
#    print(k,v)


# --------- LISTAS
#print(e)
#e.append('lll«')
#j = [1,2,3]
#print(e)
#print(j)
#e.append(j)
#print('>', e)
#e.extend(j)
#print('>', e)


# --------- FUNCTION
#def my_function(nbr):
#    nbr += 1
#    return nbr
    
#nbr = 1
#add = my_function(nbr)
#temp = 'Se eu adicionar 1 ao {pp} vou ter o resultado {pp}'

#print(temp.format(pp=add))


# --------- CLASS
#class Meca():
#    MECA = 1
#    _LALA = 1
    
#    def __init__(self):
#        self.mi = 1
#        
#    def f1(self, nbr):
#        print(nbr+1)
#    
#    def variaveis(self):
#        print('MECA', self.MECA)
#        print('mi', self.mi)

#a = Meca()
#a.variaveis()
#a.MECA = 2
#print(a.MECA)

#a._LALA = 3
#print(a._LALA)


# --------- DOCKSTRING
def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum
    
    
help(add_binary)