from Maneger import Manager
<<<<<<< HEAD
r = 0
s = 0
w = 0
for i in range(10):
    manager = Manager()
    manager.OUTPUT_TO_FILE = True
    manager.OUTPUT_TO_SCREEN = True
    print('--------------')
    print(f'Game Number: {i + 1}')
    dict = manager.run()
    if dict["winner"] == 0:
        r += 1
    if dict["winner"] == 1:
        s += 1
    if dict["winner"] == 2:
        w +=1
    print(f'Winner is {dict}')
if r > s:
    print("1 is the winner!!!!!!!!!!!!!")
elif s > r:
    print("2 is the winner!!!!!!!!!!!!!")
else:
    print("1 & 2 is the winner!!!!!!!!!!!!!")
print(r)
print(s)
print(w)
=======
import numpy as np
import matplotlib.pyplot as plt

num_users = 3
N = 10000
win_count = np.zeros(num_users)
scores = np.zeros((N, num_users))

for i in range(N):
    manager = Manager()
    manager.OUTPUT_TO_FILE = False
    manager.OUTPUT_TO_SCREEN = False
    manager.ROBOT_NUM_USER = num_users

    print('--------------')
    print(f'Game Number: {i + 1}')
    dict = manager.run()

    win_count[dict["winner"]] += 1
    scores[i, :] = dict["score"]

    print(f'Winner is {dict["winner"]}, scores: {dict["score"]}')

print()
print('--------------')
print(f'Winning Count: {(win_count / N) * 100}%')

players = ['Nadav', 'Iftach', 'Idiot1', 'Idiot2']
x = np.arange(N)
# plt.bar(players, win_count)
# plt.show()



fig = plt.figure(figsize=(8, 5)) # create a figure, just like in matlab
ax = fig.add_subplot(1, 1 ,1) # create a subplot of certain size
box = np.ones(20)/20
for i in range(num_users):
    sc = scores[:,i]
    sc = np.convolve(sc, box, mode='same')
    ax.plot(x,sc, label=players[i])
# ax.set_xlabel('index')
# ax.set_ylabel("sin(x)")
# ax.set_title("sin(x)")
ax.grid()
ax.legend()
plt.show()

>>>>>>> 70a3f5221aa9bdfe4a7accebf5bb2a24c98a58b6


