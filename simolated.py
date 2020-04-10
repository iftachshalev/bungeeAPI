from Maneger import Manager
r = 0
s = 0
for i in range(10000):
    manager = Manager()
    manager.OUTPUT_TO_FILE = True
    manager.OUTPUT_TO_SCREEN = False
    print('--------------')
    print(f'Game Number: {i + 1}')
    dict = manager.run()
    if dict["winner"] == 0:
        r += 1
    if dict["winner"] == 1:
        s += 1
    print(f'Winner is {dict}')
if r > s:
    print("1 is the winner!!!!!!!!!!!!!")
elif s > r:
    print("2 is the winner!!!!!!!!!!!!!")
else:
    print("1 & 2 is the winner!!!!!!!!!!!!!")
print(r)
print(s)



