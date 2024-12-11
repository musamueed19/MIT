
# -----------------------------
# Some Many Objects, Now What to do with them?!

# Programs usually use these object to automate those complex things, time saving us hours of time - repeatable or situtational based tasks Like --- expert systems (ES)


# So, we at end - reach on conclusion to start assigning names to these object. So, we can refer to them later in many different places. Instead, of copy and place in my different places like i.e.,

# PI = 3.1415

# We now don't need to  write PI = 3.1415 in every place. We can just use PI in every place.
# This is called variable assignment.

# DIFFERENCE BETWEEN MATH VARIABLES & CS VARIABLES

# Math variables - Abstract, can represent many values , can be used in many different places, can be used in many different equations, can be used. Like --- x * x = y (Where x represents all square roots)

# CS variables - It is bound to one single value at a given time, can be bound to an expression (but expressions evaluate to one value)
# Like m = 10;
# F = m * 9.98;


# In variable assignment - if RHS has an expression - we first evaluate RHS, then  assign the value to LHS. binds a value to a name

# Like - a = 10 + 20;  # 30

# Variable Naming - Rules
# 1. Must start with a letter or underscore
# 2. Can contain letters, digits, and underscores
# 3. Must not start with a digit
# 4. Must not contain any special characters except underscore
# 5. Must not be a reserved keyword (like if, else, for, while,
# 6. Must be descriptive and meaningful
# 7. Must be in lowercase (Python is case sensitive)
# 8. Must not be too long (Python has a limit of 255 characters for variable names)
# 9. Must not be too short (Python has a limit of 1 character for variable names)
# 10. Must not be a duplicate (Python does not allow duplicate variable names)
# -----------------------------

# Exercise - Identify valid and invalid variable names
# x = 6
# 6 = x
# x-y = 3+4
# xy = 3+4

xy = 3 + 4
print(xy)  # Output: 7
print(xy+1)  # Output: 8