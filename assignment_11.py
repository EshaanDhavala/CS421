# Assignment 11: Exploring Sets
# You will pick yourself and one other family member.
# You identify 10 favorite words (sets) for each
# You will then compute the union, intersection, difference,
# and symmetric_difference between these sets.
# You print out results.



# TODO: You need to implement these four methods

# union method
def set_union(x,y):
    our_union = my_words.union(mom_words)
    return our_union

# intersection method
def set_intersection(x,y):
    our_intersection = my_words.intersection(mom_words)
    return our_intersection

# my difference method
def my_set_difference(x,y):
    me_mom_difference = my_words.difference(mom_words)
    return me_mom_difference

# mom difference method  
def mom_set_difference(x,y):
    mom_me_difference = my_words.difference(mom_words)
    return mom_me_difference


# symmetric_difference method
def set_symmetric_difference(x,y):
    our_symmetric_difference = my_words.symmetric_difference(mom_words)
    return our_symmetric_difference

# we will setup the test cases here
# TODO: fill in the sets with 10 words in each set
my_words = {"young", "boy", "gamer", "nice", "smart", "funny", "musical", "unathletic", "Indian", "small"}
mom_words = {"adult", "woman", "worker", "nice", "smart", "funny", "intuitive", "athletic", "Indian", "small"}  

#Now call the methods and print the results
our_union = set_union(my_words, mom_words)
our_intersection = set_intersection(my_words, mom_words)
me_mom_difference = my_set_difference(my_words, mom_words)
mom_me_difference = mom_set_difference(mom_words,my_words)
our_symmetric_difference = set_symmetric_difference(my_words,mom_words)

# Now print the output/results
print("UNION: List of words that exists in my set or my mom's set")
print(our_union)

print("INTERSECTION: List of words that exists both sets")
print(our_intersection)

print("DIFFERENCE 1: List of words that are exclusive to me")
print(me_mom_difference)

print("DIFFERENCE 2: List of words that are exclusive to my mom")
print(mom_me_difference)

print("SYMMETRIC DIFFERENCE: List of words that do not have any overlap")
print(our_symmetric_difference)
