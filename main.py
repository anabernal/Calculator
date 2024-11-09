from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations = {
    "+":add,
    "-": subtract,
    "*":multiply,
    "/":divide
}
#print(operations["*"](4,8))
answer="n"
print(logo)
while answer=="y" or "n":
    if answer=="y":
        n1=result
    else:
        n1=float(input("What's the first number?:"))
    for symbol in operations:
        print(symbol)
    oper=input("Pick an operation")
    n2=float(input("What's the second number?:"))
    result=operations[oper](n1,n2)
    print (n1,oper ,n2 , "=" ,result)
    answer=input(f"Type 'y' if you want to continue calculating with {result}, or type 'n' to start a new calculation")



