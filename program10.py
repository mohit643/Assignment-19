"""Write a python program to create a function to check whether a given number is even
or odd."""

def fun(num):
  if num%2==0:
    print("even")
  else:
    print("odd") 

num=int(input("enter a no "))
fun(num)