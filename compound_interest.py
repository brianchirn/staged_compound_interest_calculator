def interest_rate_calc(principal, interest_rate, num_years, yearly_addition):
    if num_years == 0:
        return principal
    else:
        return interest_rate_calc((yearly_addition + principal) * (1 + interest_rate / 100), interest_rate,
                                  num_years - 1, yearly_addition)

def stages (num_stages):
    interest_rate = []
    num_years = []
    yearly_addition = []
    for x in range(1,num_stages + 1):
        user_interest = input("Enter interest rate for stage %s " % x )
        interest_rate.append(user_interest)
    for x in range(1,num_stages + 1):
        user_num_years = input("Enter num years for stage %s " % x)
        num_years.append(user_num_years)
    for x in range(1,num_stages + 1):
        user_yearly_addition = input("Enter yearly addition for stage %s " % x)
        yearly_addition.append(user_yearly_addition)
    return (interest_rate, num_years, yearly_addition)


user_stages = input("Enter number of career stages:")
info = stages(int(user_stages))
user_principal = int(input("Enter starting principal:"))

for i in range(int(user_stages)):
    user_principal = interest_rate_calc(user_principal, int(info[0][i]), int(info[1][i]), int(info[2][i]))
print("Final Principal: ")
print(user_principal)
