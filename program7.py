# Write a python program to sum all the numbers in a list.


def fun(list):
  i=0
  for x in list:
    i+=x
  return i

list=[2,4,7,2]
print(fun(list))