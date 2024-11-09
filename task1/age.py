age = int(input("enter your age: "))
is_student = input("r u  a stud (yes/no): ").strip().lower() == "yes"

if age < 18:
    if is_student:
        ticket_price = 5
    else:
        ticket_price = 7
elif age >= 18 and age <= 60:
    if is_student:
        ticket_price = 8
    else:
        ticket_price = 10
else:
    ticket_price = 6

print(f"The ticket price is: ${ticket_price}")
