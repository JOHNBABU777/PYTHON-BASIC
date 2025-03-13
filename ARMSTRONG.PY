num = int(input("Enter a number: "))

original_num = num

sum_of_digits = 0
num_of_digits = len(str(num))  

while num > 0:
    digit = num % 10  
    sum_of_digits += digit ** num_of_digits  
    num = num // 10  

if original_num == sum_of_digits:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")