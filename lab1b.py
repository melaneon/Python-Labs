# Melaniia Frolova
# A01391948


#   Task 3.A
#user name promt
user_name = input("Enter your name:")
print("Hello, ", user_name)

#two numbers promt
x_value = input("Enter an integer value:")
y_value = input("Enter a second integer value:")

#changing the input to integer
x_value = int(x_value)
y_value = int(y_value)

#finding a sum
xy_sum = x_value + y_value
print(x_value, "+", y_value, "=", xy_sum)


#   Task 3.C
a_value = 10.5
b_value = 4.0
c_value = a_value * b_value

print(a_value, "*", b_value, "=", c_value)


#   Task 3.D
print(int(c_value) - xy_sum)

# Q: How is the output different if you don’t convert c_value to an int?
# A: If we don't concert c_value to an integer, the result will be calculated in float by default


#   Task 3.E
print("The program is done.")