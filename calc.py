import sys
num1=float(input("Type that number!"))
operator=input("""Choose this operator!
+
-
x
/ """)
num2=float(input("Type that second number."))

if operator == "+":
    answer = num1+num2
    print(f"The answer is {answer}!")

elif operator == "-":
    answer = num1-num2
    print(f"The answer is {answer}!")

elif operator == "x":
    answer = num1*num2
    print(f"The answer is {answer}!")

elif operator == "/":
    answer = num1/num2
    print(f"The answer is {answer}!")

else:
    print("That's not an operator nerd.")
    sys.exit()
