# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
f1= lambda x, y: x+y

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*numbers):
    if len(numbers) == 1 and type(numbers[0]) is list:
        numbers = numbers[0]   #to make 'a' work below. check for single arg and if arg type is list, set index for single arg

    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
   

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(arg1, *arg2):
    if len(arg2) == 0:  #check condition if only arg1 is present and return arg1 val + 1
        return arg1 + 1
    else:  #if arg 1 and arg2 present, sum
        return arg1 + arg2[0]


print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(*regarg, **keyarg):
    if len(regarg) == 1 and type(regarg[0]) is dict: #same check as aboev fort list. check len & type, get 1st index arg, item from index to loop
        keyvals = regarg[0].items()
    else:
        keyvals = keyarg.items()

    for key, value in keyvals:
        print(f'key: {key}, value: {value}')    
# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(d)
