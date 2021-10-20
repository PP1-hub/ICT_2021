food = float(input('\nCost of meal: '))  #Tax and Tip

TIP_PERCENTAGE = .18
SALES_TAX = .05

tip = (food * TIP_PERCENTAGE)
sales_tax = (food * SALES_TAX)
grand_total = (food + tip + sales_tax)

print('Tip = $', format(tip, ',.2f'), sep='')
print('Tax = $', format(sales_tax, ',.2f'), sep='')
print('Total amount = $', format(grand_total, ',.2f'), sep='')