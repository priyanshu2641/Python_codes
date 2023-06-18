# if we want to run a sleep function for just 1 time and not other times, then we use this caching.

import time
from functools import lru_cache

@lru_cache(maxsize=5)          #it gives the number of last calls that you want to save.
def somework(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

print("Now running some work")
somework(3)
somework(1)
somework(2)
somework(5)
somework(4)
print("Done........ Calling again")
somework(3)
print("Called again")

#############################################################################################
import time
from functools import lru_cache

@lru_cache(maxsize=5)          #it gives the number of last calls that you want to save.
def somework(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

print("Now running some work")
somework(3)
somework(1)
somework(2)
somework(5)
somework(4)
print("Done........ Calling again")
input("Enter any key")
somework(3)
print("Called again")