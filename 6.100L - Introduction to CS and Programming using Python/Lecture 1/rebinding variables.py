# We can re-bind variables using new assignment statements

# Previous value may still stored in the memory, but may lose the handle for it. Like
radius = 2.2
print(radius);
# --- lose handle to the float object 2.2, stored in the memory

radius = radius + 1
print(radius);

# We are introducing control flow in our program. Lines are evaluating one after the other

# Exercise
# What are the values of meters & feet at each line.

meters = 100; # meters = 100, none
feet = 3.2808 * meters; # meters = 100, feet = 328.08
meters = 200; # meters = 200, feet = 328.08

# Python tutor - step by step debugger.
# https://pythontutor.com/