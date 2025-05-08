from random import randint

#create list
pack =[[21, 2],
       [19, 26],
       [27, 23],
       [3, 6],
       [24, 19],
       [30, 9],
       [6, 8],
       [13, 20],
       [2, 11],
       [21, 1],
       [26, 17],
       [26, 21],
       [24, 7],
       [1, 20],
       [10, 11] ]
#
def encoding():
    codir.clear()
    for i in range(0, L):
        codir.insert(i, str(randint(0, 1)))
    return codir
#
def verification():
    Pver = 0
    Cver = 0
    codir = encoding()
    for i in range(0, L):
        if int(codir[i]) == 1:
            Pver += int(pack[i][1])
            Cver += int(pack[i][0])
    if Pver <= P:
        codir = ''.join(map(str, codir))
        return codir, Cver
    else:
        return verification() 
#
def B():
    M = 0
    ver = verification()
    M = int(ver[0], 2)
    return M, ver[0], ver[1]
#
def Monte_Carlo():
    #max = 0
    maxS = None
    maxPrice = 0
    for i in range(0, N):
        answer = B()
        print(f'Step number {i+1}')
        #print('max = ' + str(max))
        print(f'maxS = {maxS}')
        print(f'maxPrice = {maxPrice}')
        if i < N:
            if maxPrice < answer[2]:
                #print('max = ' + str(max) + ' changes to ' + str(answer[0]))
                print(f'maxS = {maxS} changes to {answer[1]}')
                print(f'maxPrice = {maxPrice} changes to {answer[2]}')
                #max = answer[0]
                maxS = answer[1]
                maxPrice = answer[2]
        print("#################################################")
#
N = 10
P = 80
L = 15
codir = []
Si = 0
#
for i in range(0, 32):
    print(verification())
print('#')
Monte_Carlo()
