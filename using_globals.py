# --------------------------------------------------
# This Code Has a scope error
# We will fix it
# --------------------------------------------------

a = 4
b = 9

# it is OK referencing GLOBAL variables
def fun1():
    return a + b

# it is NOT OK to modify them in a local context
def fun2():
    print (a,b) # python thinks you mean the b below
    b = 123     # this is a LOCAL variable b
    print(b)

# Step 1
# --------------------------------------------------
#  1. Comment out fun2()
#  2. Uncomment out fun2_corrected() until Step1-END
#  3. Uncomment the call to fun2_corrected() at the end
# def fun2_corrected():
#     global a, b # tells python we''ll use the GLOBALS
#     print (a,b)
#     b = 123     # this is modifying the GLOBAL variable b
#     print(b)
# Step1-END ----------------------------------------

fun1()
fun2()
# fun2_corrected()