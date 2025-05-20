MonthlyIncome = int(input("Enter your monthly income:"))
MonthlyExpenses = int(input("Enter your total monthly expenses:"))

MonthlySavings = MonthlyIncome - MonthlyExpenses
ProjectedSavings = int((MonthlySavings * 12) + (MonthlySavings * 12 * 0.05))

print(f"Your monthly savings are ${MonthlySavings}.")
print(f"Projected savings after one year , with interest, is: ${ProjectedSavings}.")
