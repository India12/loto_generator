
print ("Welcome to the Lottery numbers generator.")

random_numbers_list = []

while True:
    number_of_num = int(raw_input("Please enter how many random numbers between 1 and 50 would you like to have: "))

    import random

    random_numbers = random.sample(range(1, 51), k = number_of_num)
    random_numbers_list.append(random_numbers)
    print random_numbers

    again = raw_input("Would you like to try again? (yes/no)")
    if again != "yes":
        break

print ("Here are your generated numbers: " + str(random_numbers_list))
print ("END")

# Ta resitev ponavlja stevila
'''while True:
    number_of_num = int(raw_input("Please enter how many random numbers between 1 and 50 would you like to have: "))
 
    import random

    random_numbers = [random.randint(0,50) for n in range(number_of_num)]
    print random_numbers

    again = raw_input("Would you like to try again? (yes/no)" )
    if again != "yes":
        break
print ("END")'''

# Ta resitev vrne zahtevani seznam, vendar se ponavljajo stevila in doloceni deli (se stopnjuje - zadnji izpis je koncen:
'''
random_numbers = []
import random
number_of_num = int(raw_input("Please enter how many random numbers would you like to have: "))
for n in range(number_of_num):
    n = random.randint(0, 50)
    random_numbers.append(n)
    print random_numbers'''



