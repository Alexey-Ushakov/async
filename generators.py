# def gen_1(word):
#     for i in word:
#         yield print(i)
#
#
# def gen_2(i: int):
#     while i != 0:
#         yield print(i)
#         i -= 1
#
#
#
#
# def loop(f, i):
#     red = []
#     red.append(f)
#     red.append(i)
#     while True:
#         try:
#             step = red.pop(0)
#             next(step)
#             red.append(step)
#         except StopIteration:
#             print('Done')
#             break
#
#
# loop(gen_1('HELLO'), gen_2(5))


