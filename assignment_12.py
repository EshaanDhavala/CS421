#A12: Halloween Candy
# Your code should only be between BEGIN and END.
# Please do not touch or change any other code.
# See the sample output your should try to get after your implementation.

# prints a dictionary; Prints both the keys and values
# try to sort the dictionary by keys
# output will be user friendly
def print_dictionary(d):
    # BEGIN your code
    print(d)
    # END your code

# prints a dictionary; Prints both the keys and values
# try to sort the dictionary by keys
# output will be user friendly
def add_dictionaries(d1,d2):
    # BEGIN your code
   from collections import Counter
   x = Counter(d1) + Counter(d2)
   return(x)
    # END your code

# test data for my_candy_bag
my_candy_bag = {    
   "snickers" : 5,
   "butterfinger" : 3,
   "candycorn" : 10,
   "skittles" : 6,
   "twix" : 7
}

# test data for my_sisters_bag
my_sisters_bag = {
   "starburst" : 5,
   "kitkat" : 6,
   "twix" : 8,
   "butterfinger" : 6,
   "candycorn" : 10
   }
  
  # derive our_combined_bag
print("")
print("[1] Our combined bag:")
print("=====================")
our_combined_bag  = add_dictionaries(my_candy_bag, my_sisters_bag)
print_dictionary(our_combined_bag)

# print my_candy_bag
print("")
print("[2] My Candy Bag:")
print("=====================")
print_dictionary(my_candy_bag)

# print sisters_bag
print("")
print("[3] My Sister's Bag:")
print("=====================")
print_dictionary(my_sisters_bag)
