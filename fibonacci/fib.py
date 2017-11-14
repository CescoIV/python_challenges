def fib(x):
  # Your code here
  start = [1,1]
  while x > 2:
   start = [start[1]] + [start[0] + start[1]]
   x-=1

  print(start[1])
 
