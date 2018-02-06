# Ryan Mottahed – Chapter 2 – Exercise 3 – 020518

# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate

print("Pay: " + str(pay))
