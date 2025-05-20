MonthlySavings = int(input("Enter your monthly income:"))
MonthlyExpenses = int(input("Enter your total monthly expenses:"))

ProjectedSavings = int((MonthlySavings * 12) + (MonthlySavings * 12 * 0.05))

print(f"Your monthly savings are ${ProjectedSavings}.")
print(f"Projected savings after one year , with interest, is: ${ProjectedSavings}.")
