# Defining global variable
x = 10  # Global variable
def test_scope():
    # Defining a local variable
    x = 20  # Local variable
    print("Inside the function, local x =", x)
print("Outside the function, global x =", x)
test_scope()
print("Outside the function, global x after function call =", x)
