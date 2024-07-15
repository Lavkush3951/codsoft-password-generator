import random
import array
max_len=12
digit = ['0','1','2','3','4','5','6','7','8','9']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','$','%','&','*','=',':','?','#','/','.','|','\'>','<','~']
combined_list = digit + upper_case + lower_case + symbols
rand_digit = random.choice(digit)
rand_upper = random.choice(digit)
rand_lower = random.choice(digit)
rand_symbols = random.choice(digit)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbols
for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(combined_list)
    temp_pass_list = array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
    password = ""
for x in temp_pass_list:
    password = password + x
print(password)
    
