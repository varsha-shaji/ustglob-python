# def foo(val,lst=[]):
#     lst.append(val)
#     return lst
# print(foo(1))  # Output: [1]
# print(foo(2,[]))
# print(foo(3))


# x=[1,2,3]
# #y=x[:]
# #y.append(4)
# #print(x)
# y=x
# y+=[4,5]
# print(x)

x=5
x = (x + 1) + (x + 1)
print(x)

# def foo(n):
#     if n == 0:
#         return []
#     else:
#         return [n] + foo(n-1)


# print(foo(3))

# a=(1,2,[3,4])
# a[2].append(5)
# print(a)


# x = [1, 2, 3]
# y = x
# y += [4, 5]
# print(x)


# def foo(val, lst=[]):
#     lst.append(val)
#     return lst


# print(foo(1))
# print(foo(2, []))
# print(foo(3))



def foo(n):
    if n == 0:
        return []
    else:
        return [n] + foo(n-1)


print(foo(3))