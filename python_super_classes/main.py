import funcs

# Super Dict
dct = funcs.SuperDict({1: "a", 2: "b"})
print(dct[2])
print(dct[10])

# Super List
lst = funcs.SortedList([3,1,2])
lst.append(4)
print(lst)

lst = funcs.SortedList([3,1,2])
lst+4
print(lst)

lst = funcs.ReversedList([3,1,2])
lst.append(4)
print(lst)

lst = funcs.ReversedList([3,1,2])
lst+4
print(lst)

lst = funcs.RevSortedList([3,1,2])
lst.append(4)
print(lst)

lst = funcs.RevSortedList([3,1,2])
lst+4
print(lst)

lst = funcs.PlusList([3,1,2])
lst + 5
print(lst)

lst = funcs.PlusList([3,1,2])
lst + "5"
print(lst)

