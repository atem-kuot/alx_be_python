monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses
total_interest_rate = MonthlySavings * 12 * 0.05
ProjectedSavings = MonthlySavings + int(total_interest_rate)

print(f"Your monthly savings are ${MonthlySavings}.")
print(f"Projected savings after one year , with interest, is: ${ProjectedSavings}.")
