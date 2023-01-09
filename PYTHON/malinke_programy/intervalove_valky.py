#intervalové války
pl = int(input('Zadejte levou mez 1. intervalu: '))
pp = int(input('Zadejte pravou mez 1. intervalu: '))
dl = int(input('Zadejte levou mez 2. intervalu: '))
dp = int(input('Zadejte pravou mez 2. intervalu: '))
print(pl,pp,dl,dp)
for j in range(pl, pp):
    for i in range(dl, dp):
        if j + i >= pl and j + i <= pp:
            print(f'[{j};{i}]')
        elif j + i >= dl and j + i <= dp:
            print(f'[{j};{i}]')
        else:
            pass