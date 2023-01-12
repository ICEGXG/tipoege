print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(x) and y) or (z and not(y)) or (not(z) and w)) == False:
                    print(x, y, z, w)
  # условие в этой задаче надо брать в скобки, иначе программ неправильно определяет приоритет выполнения операций