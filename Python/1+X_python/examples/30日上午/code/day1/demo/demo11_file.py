
# f = open('aa.txt')
# print(f.readlines())
#
# f.close()
with open('aa.txt') as f:
    # print(f.readlines())
    for line in f:
        print(line)
