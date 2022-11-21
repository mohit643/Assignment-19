# Write a python program to multiply all the numbers in a list

def fun(list):
  i=1
  for x in list:
    i*=x
  return i 

list=[int(x) for x in input("enter a no ").split(",")]

print(list)
print(fun(list))  