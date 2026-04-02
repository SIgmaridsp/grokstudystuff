
# Use sliding window (two values at a time) to solve it
# sliding window for the input next line check
# for each new pair of word add to dictionary
# OR ADD ONTO EXISTING VALUE
# print out the pairs that occurs more than once

bigrams = {}
# SLIDING WINDOW

a = 0
appear = 0
while a != "":
  ask = input("Line: ")
  if ask == "":
    print(bigrams)
    break
  resp = ask.strip().split()
  print(resp)
  for index, value in enumerate(resp): 
    if(index+1 < len(resp)): # Makes sure not go out of sliding range
      eeee = (resp[index] + " "+ resp[index+1]) # putting stuff together
      print(eeee) 
      bigrams[eeee] = bigrams.get(eeee, 0) + 1 # If same value add to 1 Else set to 0 


print(bigrams)
  #  for a in bigrams:
   #     if a in bigrams:
      #      people[name] += 1
      #  else:
          #  people[name] = 1
  
  
  


    