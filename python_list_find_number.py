# import the randint function from the random module
from random import randint

# create a function to generate a list of "size" random integers
# up to a maximum of "largest"

def random_list(largest,size):
  # create an empty list
  l = []
  # add a random number to the list the appropriate number of times
  for i in range(size):
    n = randint(0,largest-1)
    l.append(n)
  #print the list to check
  return(l)
#call the function
l = random_list(10,10)

print(l)

repeated = input("Choose a number from the list to see how many times it is repeated: ")

def find_number(l, repeated):
  x = 0
  for i in l:
    if(int(repeated) == i):
      x+=1
  return x

x = find_number(l, repeated)


print(x)
