#FizzBuzz Game
user_range=int(input("Enter your range: "))
for x in range(1,user_range+1):
  if x%3==0 and x%5==0:
    print("FizzBuzz")
  elif x%3==0:
    print("Fizz")
  elif x%5==0:
    print("Buzz")
  else:
    print(x)
