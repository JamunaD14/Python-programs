# Iterators in Python

# An iterator in Python is an object that can be iterated upon. It implements two special methods,
# __iter__() and __next__(), which together form the so-called iterator protocol.

# __iter__() method returns the iterator object itself and is used in for and in statements.
# __next__() method returns the next value from the iterator. If there is no more items to return,
# it should raise StopIteration exception.

# Example of creating an iterator:


class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current


# Using the iterator:
countdown = CountDown(3)
for number in countdown:
    print(number)

# This prints:
# 2
# 1
# 0

# Python's built-in functions like iter() and next() are used to work with iterators.
# iter() function returns an iterator from an iterable,
# next() function fetches the next item from an iterator.

# Example using iter() and next():
my_list = [1, 2, 3]
my_iter = iter(my_list)  # creating an iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# Next call to next(my_iter) will raise StopIteration as there are no more items.

# In a generator during next() the function will pause execution upon a yield and return the corresponding value.
def simple_generator():
    yield "Start"
    yield "Middle"
    yield "End"


# Create a generator
gen = simple_generator()

# Get the first value (execution pauses at the first yield)
print(next(gen))  # Output: Start

# Get the second value (execution resumes and then pauses at the second yield)
print(next(gen))  # Output: Middle

# Get the third value (execution resumes and then reaches the end)
print(next(gen))  # Output: End

# Next call will raise StopIteration as the generator is exhausted
print(next(gen))

for val in simple_generator():
    print(val)
# Prints:
# Start
# Middle
# End

# The countdown as a generator instead of an iterator.
# Remember that the while-loop pauses when encountering an yield.
def countdown_generator(start):
    n = start
    while n >= 0:
        yield n
        n -= 1
