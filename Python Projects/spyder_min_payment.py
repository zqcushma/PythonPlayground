b = 320000
i = 0.2
t = 12
e = 0.01

class MinPayment:
    balance = 0.0
    annualInterest = 0.0
    term = 0
    monthlyInterest = 0.0    
    error = 0.0
    
    def __init__(self, balance, annualInterest, term, error):
        self.balance = balance
        self.annualInterest = annualInterest
        self.term = term
        self.error = error
        self.monthlyInterest = annualInterest/12
    def findMinPayment(self):
        return self.balance/self.term
    def findMaxPayment(self):
        return (self.balance * (1 + self.monthlyInterest)**12) / self.term
    
    #calculates the remaining balance after the 12 month period
    def remainingBalance(self, payment):
        newbalance = self.balance
        for month in range(1, self.term+1):
            newbalance -= payment
            newbalance += self.monthlyInterest * newbalance
        return (newbalance)
        
    def calculateMinPayment(self):
        low = self.findMinPayment()
        high = self.findMaxPayment()
        finalAnswer = 0.0
        breaker = 0
        while breaker < 10000:
            guess = (low + high) / 2
            guessBalance = self.remainingBalance(guess)
            if (abs(guessBalance) <= self.error):
                finalAnswer = guess
                break
            elif (guessBalance > 0):
                breaker += 1
                low = guess
            else:
                high = guess
        if finalAnswer == 0.0:
            return "Error"
        else:
            return round(finalAnswer, 2)
        
mp = MinPayment(b, i, t, e)
ans = mp.calculateMinPayment()
print("The minimum payment is " + str(ans))