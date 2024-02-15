def front3(something):
    result = something[0:min(3,len(something))]
    resultx3 = result+result+result
    return resultx3

print(front3("hello"))
print(front3("ab"))


