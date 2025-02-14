# -------------------------------------------
# INFO: This code is incomplete
#  We will work on this to understand:
#   * the main
# -------------------------------------------#

def fun1(n):
  print("I will return", n, "+ 1")
  return n+1

def fun2(m):
  print("I will return", m, "squared")
  return m**2

# Step 1: (when done, comment out until "Step1-END")
# --------------------------------------------------
# Calling from General Context:
num = 5
num = fun1(num)
print("fun1 returned",num)
num = fun2(num)
print("fun2 returned",num)
# Step1-END ----------------------------------------



# Step 2: (select and uncomment until "step2-END")
# --------------------------------------------------
# # Calling a main function
# def main():
#   num = 5
#   num = fun1(num)
#   num = fun2(num)
#   print ("the final number is:",num)

# # still always calling main from the general context
# main()
# Step2-END ----------------------------------------

# Step 3: (full fix after the next exercise)