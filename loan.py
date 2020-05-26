class Loan:
    def __init__(self, principle, interest_rate, target_principle,  interest=0):
        self.interest = interest
        self.principle = principle
        self.target_principle = target_principle
        self.monthly_interest = interest_rate/12
        self.total_paid = 0

    def monthly_payment(self, payment, extra_payment = 0):
        # Mortgage interest is calculated strictly on principle vs a general loan that is calculated on principle + interest
        self.interest += self.principle * self.monthly_interest
        if payment >= self.interest:
            payment -= self.interest
            self.interest = 0
            self.principle -= payment
        else:
            self.interest -= payment
        # Extra monthly payments are applied directory to principle
        self.principle -= extra_payment
        #print(f'Current interest {self.interest}')
        #print(f'Current principle {self.principle }')
        if self.target_principle >= self.principle:
            #print(f'Target principle met. Total paid is {self.total_paid}')
            return True
        else:
            return False




