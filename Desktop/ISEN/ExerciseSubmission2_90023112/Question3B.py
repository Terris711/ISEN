def discount(age, ticketPrice):
    if age < 0:
        print("Invalid age!")
        price = 0.0
        return price
    elif age >= 1 and age <= 5:
        price = ticketPrice*(1-5/100)
        return price
    elif age >= 6 and age <= 16:
        price = ticketPrice*(1-15/100)
        return price
    elif age >= 17 and age <= 35:
        price = ticketPrice*(1-0/100)
        return price
    elif age >= 36 and age <= 49:
        price = ticketPrice*(1-30/100)
        return price
    elif age >= 50:
        price = ticketPrice*(1-50/100)
        return price

#age = int(input("Enter age: "))
#ticketPrice = float(input("Enter ticket price: "))
#print(discount(age, ticketPrice))
