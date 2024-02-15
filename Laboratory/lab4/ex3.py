
def three_consecutive(a,b):
    cnt=0
    for i in a:
        if i in b:
            cnt+=1
            b.remove(i)
        else:
            cnt=0
        if cnt == 3:
            return True
    return False


a=[1, 10, 9, 10, 8]
b=[2,10, 0, 10, 7, 6]
c=[2,10, 9, 10, 7, 6]
print(three_consecutive(a,b))
print(three_consecutive(a,c))