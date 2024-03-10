
# Function to check if a number is in binary format
def is_it_binary(num) :
    # Check every bit in the number
    for char in num:
        if char not in ['0', '1']:
            return False
    return True
# Function to check if a number is in decimal format
def is_it_decimal(num):
    # Check every bit in the number
    for char in num:
        if char not in ['0','1','2','3','4','5','6','7','8','9']:
            return False
    return True
# Function to check if a number is in Octal format
def is_it_Octal(num):
    # Check every bit in the number
    for char in num:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            return False
    return True
# Function to check if a number is in deciHexadecimal format
def is_it_hexadecimal(num):
    # Check every bit in the number
    for char in num:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A','B','C','D','E','F']:
            return False
    return True
# Function to convert a decimal number to octal
def convert_from_decimal_to_binary(num):    #  decimal(16) = binary(10000)
    num = str(num) # Set the number to string
    binary_list=[] # Creat an empty list to store binary digits
    binary_number='' # Creat an empty string to store the final binary number
    while int(num)>0: # Loop until the number becomes zero
        the_remainder = int(num) % 2 # Calculate the remainder when divided by 2
        the_quotient = int(num) / 2 # Calculate the quotient when divided by 2
        binary_list.append(the_remainder) # Append the remainder to the list
        num = int(the_quotient) # Update the number to the quotient
    binary_list.reverse() # Reverse the list to get binary digits in correct order
    length_of_binary_list=len(binary_list) # Get the length of the binary list
    # Convert the list of binary digits to a string representing the binary number
    for digit_place in range(length_of_binary_list):
        binary_digit=binary_list[digit_place]
        binary_number=binary_number+str(binary_digit) # Append each binary digit to the binary number
    return binary_number # Return the final binary number as a string
# Function to convert a decimal number to octal
def convert_from_decimal_to_Octal(num):  # decimal(28) =  binary(34)
    num = str(num) # Set the number to string
    octal_list=[] # Creat an empty list to store octal digits
    octal_number= '' # Creat an empty string to store the final octal number
    while int(num)>0: # Loop until the number becomes zero
        the_remainder= int(num) % 8 # Calculate the remainder when divided by 8
        the_quotient= int(num) / 8 # Calculate the quotient when divided by 8
        octal_list.append(the_remainder) # Append the remainder to the list
        num=int(the_quotient) # Update the number to the quotient
    octal_list.reverse() # Reverse the list to get octal digits in correct order
    length_of_octal_list=len(octal_list) # Get the length of the octal list
    # Convert the list of octal digits to a string representing the octal number
    for digit_place in range(length_of_octal_list):
        octal_digit=octal_list[digit_place]
        octal_number= octal_number + str(octal_digit) # Append each octal digit to the octal number
    return octal_number # Return the final octal number as a string
# Function to convert a decimal number to hexadecimal
def convert_from_decimal_to_Hexadecimal(num): #decimal(314) = hexadecimal(13A)
    num = str(num) # Set the number to string
    hexadecimal_list=[] # Creat an empty list to store hexadecimal digits
    hexadecimal_number= '' # Creat an empty string to store the final hexadecimal number
    while int(num)>0: # Loop until the number becomes zero
        # Dictionary to map remainders to hexadecimal values
        convertion_dictionary={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        the_remainder= int(num) % 16 # Calculate the remainder when divided by 16
        the_quotient= int(num) / 16 # Calculate the quotient when divided by 16
        hexadecimal_list.append(convertion_dictionary[the_remainder]) # Append the remainder mapped to its hexadecimal representation
        num=int(the_quotient) # Update the number to the quotient
    hexadecimal_list.reverse() # Reverse the list to get hexadecimal digits in correct order
    length_of_hexadecimal_list=len(hexadecimal_list) # Get the length of the hexadecimal list
    # Convert the list of hexadecimal digits to a string representing the hexadecimal number
    for digit_place in range(length_of_hexadecimal_list):
        hexadecimal_digit=hexadecimal_list[digit_place]
        hexadecimal_number= hexadecimal_number + str(hexadecimal_digit)# Append each hexadecimal digit to the hexadecimal number
    return hexadecimal_number # Return the final hexadecimal number as a string
# Function to convert a binary number to decimal
def convert_from_binary_to_decimal(num): #binary(11001) = decimal(25)
    num = str(num) # Set the number to string
    # Convert the binary number string to a list of individual digits and reverse it
    number_in_list = [num] # Put the binary number in list
    list_number_digits = list(map(int, number_in_list[0])) # Sperate every digit in the binary number
    list_number_digits.reverse() # Reverse the list to get binary digits in correct order
    decimal_number=0 # Creat the decimal equivalent to 0
    length_of_list_number_digits = len(list_number_digits) # Get the length of the binary list
    for counter in range(length_of_list_number_digits): # Loop through each digit in the binary number list
        # Calculate the decimal value of the digit based on its position in the binary number
        # Multiply the digit value by 2 raised to the power of its position
        the_digit_as_decimal=( 2 ** counter)*(list_number_digits[counter])
        decimal_number= decimal_number + the_digit_as_decimal # Add the decimal values
    return decimal_number # Return the final decimal value
# Function to convert a Octal number to binary
def convert_from_binary_to_Octal(num): #binary(1101101)=octal(155)
    num = str(num) # Set the number to string
    if len(num) % 3==0: # Check if the length of the binary number is divisible by 3
        complete_three_digits = (len(num) % 3)
    else:
        complete_three_digits = 3-(len(num) % 3)
    # Pad the binary number to ensure it's divisible by 3
    the_new_num= (complete_three_digits * '0') + num
    octal_list=[] # Creat a list to store octal digits
    octal_number=''  # Creat the final octal number
    digits_of_octal_number=int(len(the_new_num) / 3) # Calculate the number of groups of 3 digits in the binary number
    # Dictionary for binary to octal conversion
    convertion_dictionary={'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
    for conuter in range(digits_of_octal_number): # Split the binary number into groups of 3 digits and convert to octal
        # Define the starting and ending indexes for each group of 3 binary digits
        start_index= conuter * 3
        end_index= start_index + 3
        # Get each group of 3 binary digits and convert to octal using the conversion dictionary
        octal_list.append(the_new_num[start_index:end_index])
    length_of_octal_list=len(octal_list) # Get the length of the Octal list
    for counter in range(length_of_octal_list): # Convert each group of binary digits to its octal representation
        hexadecimal_digit = convertion_dictionary[octal_list[counter]]
        octal_number = octal_number + str(hexadecimal_digit) # link the octal digits
    return int(octal_number) # Return the final octal number
# Function to convert a binary number to hexadecimal
def convert_from_binary_to_Hexadeciml(num): #binary(100111)=hexadecimal(27)
    num=str(num) # Set the number to string
    if len(num) % 4==0: # Check if the length of the binary number is divisible by 4
        complete_four_digits = (len(num) % 4)
    else:
        complete_four_digits =  4 - (len(num) % 4)
    # Pad the binary number to ensure it's divisible by 4
    the_new_num= (complete_four_digits * '0') + num
    Hexadeciml_list=[] # Creat a list to store hexadecimal digits
    Hexadeciml_number= '' # Creat the final hexadecimal number
    # Dictionary to map binary digits to their corresponding hexadecimal equivalents
    convertion_dictionary={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7',
                           '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    digits_of_hexaecimal_number = int(len(the_new_num) // 4)  # Calculate the number of groups of 4 digits in the binary number
    # Convert the binary number into hexadecimal groups of 4 bits eac
    for conuter in range(digits_of_hexaecimal_number):
        # Calculate the beginning and ending index of each 4-bit group
        start_index= conuter * 4
        end_index= start_index + 4
        # Get each group of 4 binary digits and convert to hexadecimal using the conversion dictionary
        Hexadeciml_list.append(the_new_num[start_index:end_index])
    length_of_octal_list=len(Hexadeciml_list) # Get the length of the hexadecimal list
    for conuter in range(length_of_octal_list): # Convert each group of binary digits to its octal representation
        hexadecimal_digit = convertion_dictionary[Hexadeciml_list[conuter]]
        Hexadeciml_number = Hexadeciml_number + str(hexadecimal_digit) # link the hexadecimal digits
    return Hexadeciml_number # Return the final hexadecimal number
# Function to convert a octal number to decimal
def convert_from_octal_to_decimal(num): #cotal(147) = decimal(103)
    num = str(num) # Set the number to string
    # Convert the octal number string to a list of individual digits and reverse it
    the_number_in_list = [num] # Put the Octal number in list
    list_the_number_digits = list(map(int, the_number_in_list[0])) # Sperate every digit in the Octal number
    list_the_number_digits.reverse() # Reverse the list to get Octal digits in correct order
    decimal_number = 0 # Creat the decimal equivalent to 0
    length_of_list_the_number_digits = len(list_the_number_digits) # Get the length of the Octal list
    # Iterate through the list of octal digits to convert to decimal
    for counter in range(length_of_list_the_number_digits):
        digit_of_the_octal_number=list_the_number_digits[counter]
        # Calculate the decimal value of the digit based on its position in the Octal number
        # Multiply the digit value by 8 raised to the power of its position
        the_digit_as_decimal = (8 ** counter)*digit_of_the_octal_number
        decimal_number = decimal_number + the_digit_as_decimal
    return decimal_number # Return the decimal equivalent
# Function to convert octal number to binary
def convert_from_octal_to_binary(num): #octal(354)=binary(011101100)
    num = str(num) # Set the number to string
    # Dictionary to map binary digits to their corresponding Octal equivalents
    convertion_dictionary = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110',
                             '7': '111'}
    # Convert the input octal number to a list of individual digits
    the_number_in_list = [num] # Put the Octal number in list
    list_the_number_digits = list(map(int, the_number_in_list[0])) # Sperate every digit in the Octal number
    the_binary_number='' # Reverse the list to get Octal digits in correct order
    length_of_list_the_number_digits = len(list_the_number_digits) # Get the length of the Octal list
    # Iterate through each octal digit and convert it to its binary representation
    for counter in range(length_of_list_the_number_digits ):
        the_octal_digit=str(list_the_number_digits[counter])
        the_binary_number=the_binary_number+str(convertion_dictionary[the_octal_digit])
    return int(the_binary_number) # Return the final binary number
# Function to convert a octal number to hexadecimal
def convert_from_octal_to_hexahecimal(num): #octal(1345) = hexadecimal(2E5)
    num = str(num) # Set the number to string
    the_number_in_binary= convert_from_octal_to_binary(num)
    the_number_in_hexadecimal= convert_from_binary_to_Hexadeciml(the_number_in_binary)
    return the_number_in_hexadecimal # Return the final hexadeciaml number
# Function to convert a hexadecimal number to decimal
def convert_from_hexadecimal_to_decimal(num): #hexadecimal(134A)=decimal(4938)
    num = str(num) # Set the number to string
    # Dictionary to map binary digits to their corresponding hexadecimal equivalents
    convertion = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',  'A':'10','B':'11',
                  'C':'12' , 'D':'13' , 'E':'14' , 'F':'15'}
    # Convert the hexadecimal number string into a list of individual digits and reverse it
    the_number_in_list = [num] # Put the hexadecimal number in list
    list_the_number_digits = list(map(str, the_number_in_list[0])) # Sperate every digit in the Hexadecimal number
    list_the_number_digits.reverse() # Reverse the list to get hexadecimal digits in correct order
    decimal_number = 0 # Creat the decimal equivalent to 0
    length_of_list_the_number_digits = len(list_the_number_digits)  # Get the length of the hexadecimal list
    for counter in range(length_of_list_the_number_digits): # Loop through each digit of the hexadecimal number
        # Get the decimal value of the current hexadecimal digit from the conversion dictionary
        digit_of_the_octal_number = int(convertion[list_the_number_digits[counter]])
        # Calculate the decimal equivalent by multiplying the digit's value by the power of 16
        # corresponding to its position in the hexadecimal number
        the_digit_as_decimal = (16 ** counter) * digit_of_the_octal_number
        # Add the calculated decimal value to the result
        decimal_number = decimal_number + the_digit_as_decimal
    return decimal_number # Return the decimal equivalent
# Function to convert a hexadecimal number to binary
def convert_from_hexadecimal_to_binary(num): # hexadecimal(F17) = binary(111100010111)
    num = str(num) # Set the number to string
    # Dictionary to map binary digits to their corresponding hexadecimal equivalents
    convertion_dictionary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                             '7': '0111' ,'8':'1000' ,'9':'1001' ,'A':'1010' ,'B':'1011' ,'C':'1100' ,'D':'1101' ,'E':'1110' ,'F':'1111'}
    # Convert the hexadecimal number string into a list of individual digits
    the_number_in_list = [num] # Put the hexadecimal number in list
    list_the_number_digits = list(map(str, the_number_in_list[0])) # Sperate every digit in the Hexadecimal number
    the_binary_number='' # Creat an empty string to store the final binary number
    length_of_list_the_number_digits = len(list_the_number_digits) # Get the length of the hexadecimal list
    # Loop through each digit of the hexadecimal number
    for counter in range(length_of_list_the_number_digits ):
        the_octal_digit=str(list_the_number_digits[counter])
        the_binary_number=the_binary_number+str(convertion_dictionary[the_octal_digit])
    return int(the_binary_number) # Return the final binary number
# Function to convert a hexadecimal number to Octal
def convert_from_hexadecimal_to_octal(num): # hexadecimal(1256) = Octal(11126)
    num = str(num) # Set the number to string
    the_number_in_binary= convert_from_hexadecimal_to_binary(num)
    the_number_in_octal= convert_from_binary_to_Octal(the_number_in_binary)
    return the_number_in_octal # Return the final octal number
while True: # repeat the system
    '''print the first menu'''
    print('** numbering system converter **') #show the user the name of the system
    print(' A) insert a new number \n B) Exit program')
    frist_menu=input('Please enter your choice (A/B) : ').upper() #get if the user want to exit & make the input in the upper case
    if frist_menu == 'B': #check if the user want's to exit
        break # exit the system
    elif frist_menu == 'A': #check if the user want's to use the system
        num= input('Please insert a number : ').upper() #get the number from the user that want to be converted
        print('** Please select the base you want to convert a number from**') #expline to the user to enter the base he want's to convert from , Menu 2
        convert_from= input(' A) Decimal \n B) Binary \n C) Octal \n D) Hexadecimal \n please choice (A/B/C/D) : ').upper() # get from the user the base he wants to convert from and convert it to the upper case
        if convert_from == 'A' and is_it_decimal(num) ==True : # chech if the user enter a valid way means the base to convert from
            print('** Please select the base you want to convert a number to **') # show the user Menu 3 to explain to him to choise the base he wants the system to convert to
            convert_to= input(' A) Decimal \n B) Binary \n C) Octal \n D) Hexadecimal \n please choice (A/B/C/D) : ').upper() # get from the user the base he wants to convert to and convert it to the upper case
            if convert_to == 'A' : # to check all the cases that the user convert from the same base to itself
                print(num) # converting from the same base to itself means the number doesn't change
            elif convert_to == 'B' : # check if the user wants to convert from Decimal to Binary
                print(convert_from_decimal_to_binary(num))
            elif convert_to == 'C' : # check if the user wants to convert from Decimal to Octal
                print(convert_from_decimal_to_Octal(num))
            elif convert_to == 'D' : # check if the user wants to convert from Decimal to Hexadecimal
                print(convert_from_decimal_to_Hexadecimal(num))
            else: # if the user enter a non valid way means the base
                print('Please Enter a valid Choice') # tell the user to enter a valid way to mean the base
        elif convert_from == 'B' and is_it_binary(num) ==True: # chech if the user enter a valid way means the base to convert from
            print('** Please select the base you want to convert a number to **') # show the user Menu 3 to explain to him to choise the base he wants the system to convert to
            convert_to= input(' A) Decimal \n B) Binary \n C) Octal \n D) Hexadecimal \n please choice (A/B/C/D) : ').upper() # get from the user the base he wants to convert to and convert it to the upper case
            if convert_to == 'A':  # to check all the cases that the user convert from the same base to itself
                print(convert_from_binary_to_decimal(num))
            elif convert_to == 'B':  # check if the user wants to convert from Decimal to Binary
                print(num)  # converting from the same base to itself means the number doesn't change
            elif convert_to == 'C':  # check if the user wants to convert from Decimal to Octal
                print(convert_from_binary_to_Octal(num))
            elif convert_to == 'D':  # check if the user wants to convert from Decimal to Hexadecimal
                print(convert_from_binary_to_Hexadeciml(num))
            else: # if the user enter a nonvalid way means the base
                print('Please Enter a valid Choice') # tell the user to enter a valid way to mean the base
        elif convert_from == 'C' and is_it_Octal(num) == True:  # chech if the user enter a valid way means the base to convert from
            print('** Please select the base you want to convert a number to **')  # show the user Menu 3 to explain to him to choise the base he wants the system to convert to
            convert_to = input(' A) Decimal \n B) Binary \n C) Octal \n D) Hexadecimal \n please choice (A/B/C/D) : ').upper()  # get from the user the base he wants to convert to and convert it to the upper case
            if convert_to == 'A':  # to check all the cases that the user convert from the same base to itself
                print(convert_from_octal_to_decimal(num))
            elif convert_to == 'B':  # check if the user wants to convert from Decimal to Binary
                print(convert_from_octal_to_binary(num))
            elif convert_to == 'C':  # check if the user wants to convert from Decimal to Octal
                print(num)  # converting from the same base to itself means the number doesn't change
            elif convert_to == 'D':  # check if the user wants to convert from Decimal to Hexadecimal
                print(convert_from_octal_to_hexahecimal(num))
            else:  # if the user enter a nonvalid way means the base
                print('Please Enter a valid Choice')  # tell the user to enter a valid way to mean the base
        elif convert_from == 'D' and is_it_hexadecimal(num) == True:  # chech if the user enter a valid way means the base to convert from
            print('** Please select the base you want to convert a number to **')  # show the user Menu 3 to explain to him to choise the base he wants the system to convert to
            convert_to = input(' A) Decimal \n B) Binary \n C) Octal \n D) Hexadecimal \n please choice (A/B/C/D) : ').upper()  # get from the user the base he wants to convert to and convert it to the upper case
            if convert_to == 'A':  # to check all the cases that the user convert from the same base to itself
                print(convert_from_hexadecimal_to_decimal(num))
            elif convert_to == 'B':  # check if the user wants to convert from Decimal to Binary
                print(convert_from_hexadecimal_to_binary(num))
            elif convert_to == 'C':  # check if the user wants to convert from Decimal to Octal
                print(convert_from_hexadecimal_to_octal(num))
            elif convert_to == 'D':  # check if the user wants to convert from Decimal to Hexadecimal
                print(num)  # converting from the same base to itself means the number doesn't change
            else:  # if the user enter a nonvalid way means the base
                print('Please Enter a valid Choice')  # tell the user to enter a valid way to mean the base
        else:  # if the user enter a not programmed input
            print('Please select a valid Choice')  # ask from the user to enter the base in way the system can understand
    else: # if the user enter something not in the choices
        print('please select a valid choice')

