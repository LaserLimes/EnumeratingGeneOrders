# given a positive int k, print how many permutations followed by all the permutations.

from itertools import permutations

# first generate a list of length k 1-k

k = 5
n = 1
generatedList = []

# create an empty list to append all our permutations
# this makes it easy to count them and print them in the desired format
appendList = []

while k > 0:
    generatedList.append(n)
    n += 1
    k -= 1

for i in permutations(generatedList):
    appendList.append(i)

# return the desired output. I used the * function to unpack the tuple

print(len(appendList))
for item in appendList:
    print(*item)
