from Maneger import Manager

# while True:
#     ROBOT_NUM_USER = input("Shoos number of players:\n >>>")
#     try:
#         ROBOT_NUM_USER = int(ROBOT_NUM_USER)
#
#         break
#     except:
#         print("Error!!!")
#
# ROBOT_ARRAY = []
# for i in range(ROBOT_NUM_USER):
#     succses = False
#     while succses is False:
#         print("player", i + 1, ":")
#         input_1 = input(" Robot [R] or player [P]?")
#         if input_1 == "P":
#             ROBOT_ARRAY.append(0)
#             succses = True
#             print(" The player saved!")
#         elif input_1 == "R":
#             while True:
#                 input_2 = input(" What is the level? [1, 2, 3]:")
#                 try:
#                     input_2 = int(input_2)
#                     if input_2 > 3 or input_2 < 1:
#                         print(" Error!!!")
#                     else:
#                         break
#                 except:
#                     print(" Error!!!")
#             ROBOT_ARRAY.append(input_2)
#             print(" The player saved!")
#             succses = True
ROBOT_ARRAY = [1, 1, 2, 3, 1, 2, 3]
d = Manager(ROBOT_ARRAY)
t = d.run()
print(t["score"])

