# We have created a bunch of objects uptil now. Now, what we can do with them in our programs.
# We can combine them into expressions

# <object> + <operator> + <object> --- syntactic valid expression in Python

print(3+2);
print(type(3+2));

# Python, doesn't store the expressions in the memory, what it does it reads the expression evaluates it to one single value. And then it stores the result value in the memory.
print(type(5/2));



# BIG IDEA
# Replace complex expressions by ONE value

# It solves the expression from Left -> Right --- like in classical Math (same case for & in parenthesis).

print((4+2) * 6 -1);
print(float((4+2) * 6 - 1));


# The result of 'type' function is also returned and stored in the memory.



# Exercise
print((13-4) / (12 * 12));
print(type(4*3));
print(type(4.0*3));     #multiplication with float --- results in float too (not in int)
print(int(1/2));
