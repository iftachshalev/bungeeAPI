from Maneger import Manager
import numpy as np

num_users = 3
N = 1000
win_count = [0] * num_users
scores = np.zeros((N, num_users))

for i in range(N):
    manager = Manager()
    manager.OUTPUT_TO_FILE = True
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
print(f'Winning Count: {win_count}')




