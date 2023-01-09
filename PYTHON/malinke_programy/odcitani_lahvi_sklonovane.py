#odčítání lahví se skloŇováním
for i in range(10,0,-1):
    if i >= 5:
        lahve = 'zelených lahví'
    elif i >= 2 and i < 5:
        lahve = 'zelené lahve'
    else:
        lahve = 'zelená láhev'
    print(f'{i} {lahve} stojí na stole a jedna spadne')