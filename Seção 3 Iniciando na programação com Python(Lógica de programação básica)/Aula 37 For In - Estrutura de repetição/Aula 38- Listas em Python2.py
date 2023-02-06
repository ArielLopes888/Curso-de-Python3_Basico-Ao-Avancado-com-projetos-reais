"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [l1 + l2]
l4 = ['A', 'R', 'I', 'E', 'L']
l5 = ['A', 'M', 'O', 'R']
l6 = ['Flamengo', 'Fluminense', 'Vasco', 'Botafogo']
l1.extend(l2)
l2.append('xxx')
l4.insert(1, 'banana')
l5.pop()
del (l6[1:4])

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(max(l1))
print(min(l1))

Cliente = ['Ariel', True, 25, 1.80]

for elem in Cliente:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
