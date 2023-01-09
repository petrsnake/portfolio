#smajlíkoanalyzátor
a = input('zadej smajlíka')
if a.endswith(')'):
    print('smajlík je veselý')
elif a.endswith('('):
    print('naštvaný')
elif a.endswith('P'):
    print('smajlík je zlobivý')
else:
    print('neznám')