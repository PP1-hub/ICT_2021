drink1 = float(input("For 0.10: "))  #Bottle Deposits
drink2 = float(input("For 0.25: "))

output = round((drink1 * 0.10) + (drink2 * 0.25), 2)
print("Refund for Bottles: $",output)