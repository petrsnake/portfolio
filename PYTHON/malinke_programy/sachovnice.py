sach = []
count = 0
for i in range(8):
    radek = []
    for j in range(4):
        radek.append('█')
        radek.append(' ')
    if count == 1:
        radek.reverse()
        count -= 2
    else: pass
    sach.append(radek)
    count += 1

