import random

first=['eri','feri','sub','dis','tyu']
mid=  ['Zeus', 'Poseidon', 'Hera', 'Hestia','Hades', 'Apollo','Hermes', 'Athena', 'Aphrodite','Ares']
last=['blue','cyan','green','black','magenta','red','white','yellow']

print("Password Generator")
print("=================")
while True:
    try:
        num_pw=int(input("\nEnter the number of needed passwords: "))

        if num_pw <=0 or num_pw>24:
            print("\nEnter a number between 1 and 24.")
            continue
   
        for i in range(num_pw):
            x=random.choice(first)
            y=random.choice(mid)
            z=random.choice(last)
            random_password=x+y+z
            print(f"{i+1}-->",random_password)
        break

    except ValueError:
        print("please enter a number.")