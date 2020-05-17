# # print(ord("b")-ord("a"))

arr = [1, 3, 2, 2,1]


def singleNumber(A):
    x = 0
    for n in A:
        x = x ^ n
        #print(x)
    return x


print(singleNumber(arr))

# a =6
# b=2
# print(a^b)