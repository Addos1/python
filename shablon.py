sh = 'r*t%f*z'
sl = 'rtltрfwbz'
for i in sh.replace('*', ' ').replace('%', ' ').rsplit():
    if i in sl[sh.index(i[0]):len(sl) - len(sh) + sh.index(i[-1]) + 1]:
        Z = True
    else:
        Z = False
        break
print(Z)
