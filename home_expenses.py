from loan import Loan

target_home_cost = 195000
downpayment_percentage = .10

base_loan = 237500
base_principle = 1033.62
base_hazard = 133.34
base_phi = 104.90
base_taxes = 133.34

target_down_payment = downpayment_percentage * target_home_cost
print(f'Down payment: {target_down_payment}')
target_loan = target_home_cost - target_down_payment
target_no_phi = .8 * target_home_cost

interest_rate = .035
monthly_rate = .035/12
additional_loan_payment = 200

# Use proportions to scale expense feature
def convert_to_target(loan, feature, t_loan): return t_loan/(loan/feature)


target_principle = convert_to_target(base_loan, base_principle, target_loan)
target_harzard = convert_to_target(base_loan, base_hazard, target_loan)
target_phi = convert_to_target(base_loan, base_phi, target_loan)
target_taxes = convert_to_target(base_loan, base_taxes, target_loan)




#print(target_principle, target_harzard, target_phi, target_taxes)
if downpayment_percentage >= .2:
    total_expenses = target_principle + target_harzard + target_taxes
    print(f'No PHI. Monthly payment is {total_expenses}')
else:
    total_expenses = target_principle + target_harzard + target_taxes + target_phi
    print(f'Monthly payment: {total_expenses}')


mortgage = Loan(target_loan, interest_rate, target_no_phi)

payments = 0
for i in range(1000):
     percentage_paid = mortgage.monthly_payment(target_principle, 1000)
     if percentage_paid and i == 0:
         break
     elif percentage_paid:
         print(f'20 percent met at payment {i}')
         payments = i + 1
         break

if payments != 0:
    print(f'Total amount paid in PHI {(payments * target_phi) + 400}')




