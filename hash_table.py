# hash function maps strings(any kind of data) to numbers
# hash tables are good to use when you want to:
# -model relationships from one thing to another
# -look something up
# -filter out duplicates (voting example)
# -caching data instead of making the server do work
# DNS resolution (mapping web adresses to IP adresses), phonebook
#
# collision is when two keys have been assigned the same slot in the bucket (bucket can be linked list, array, tree etc.)
# low collision = better performance
# a good hash function distributes values in the array evenly
# load factor = (number of items / number of slots), if load factor > 0.7 ===> resize
# time complexity: O(1) at average case, O(n) at worst case
#
# dictionaries in python are hast tables
