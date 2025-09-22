def myPrint(n):
    
    print("hello", n)
    if n == 5: return 'Done'       
    myPrint(n + 1)

print(myPrint(1))
   # Recurssions need some for of ending/stopping statement 

def recur_sum(n):
    if n == 0:
        return 0
    else: n + recur_sum(n - 1)

print(recur_sum(5))

    