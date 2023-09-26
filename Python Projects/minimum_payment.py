
def f(balance,payment,monthlyInterestRate,term):
     newbalance = balance
     for month in range(1, term+1):
        newbalance -= payment
        newbalance += monthlyInterestRate * newbalance
     return (newbalance)


balance=320000
annualInterestRate=0.2
term=12
epsilon=0.01

n = 1
low=balance / term
monthlyInterestRate=annualInterestRate / 12
high=(balance * (1 + monthlyInterestRate)**12) / term
maxIterations=1000
while n <= maxIterations: # limit iterations to prevent infinite loop
    guess = (low + high)/2 # new midpoint
    residual=f(balance,guess,monthlyInterestRate,term)
    if abs(residual) <= epsilon:
         print(round(guess,2))
         break
    elif residual > 0:
       low=guess
    else:
       high=guess
    n = n + 1 # increment step counter
