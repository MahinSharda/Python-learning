def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Please enter a valid number ")

number_people = int(input("How many people are there in the group "))
names=[]
for i in range(number_people):
    name=input(f"Enter name {i+1} ").strip()
    names.append(name)

bill=get_float("Enter total bill amount in number only ")

share = round(bill/number_people,2)

print(f"Total bill is {bill} \n")
print(f"Divided share for {number_people} is {share} \n")

for name in names:
    print(f"{name} owes {share} rupees ")