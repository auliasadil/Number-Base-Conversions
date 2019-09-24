#This Program is created by Muhammad Aulia Adil

def validate_the_number(source_base,destination_base,value): #this function will validate the number.
    for i in range(0,len(value)):
        convert_value = value[i]
        if value[i] == 'A':
            convert_value = '10'
        if value[i] == 'B':
            convert_value = '11'
        if value[i] == 'C':
            convert_value = '12'
        if value[i] == 'D':
            convert_value = '13'
        if value[i] == 'E':
            convert_value = '14'
        if value[i] == 'F':
            convert_value = '15'
        if eval(source_base) <= eval(convert_value) or eval(convert_value)<0 or value[i]<'0' or '9'<value[i]<'A' or value[i]>'F':
            #If one character of the number entered is more higher than the source base, it returns false
            #If the number entered is a negative number, it returns false
            #If one character of the number entered is not 0 to 9 or A to F, it returns false
            return False
    return True

def convert_the_number(source_base,destination_base,value): #this function will convert the number entered
    number = 0
    value = str(value)
    length_of_value = len(value)
    source_base = eval(source_base)
    for i in range(0,length_of_value):
        convert_value = value[i]
        if value[i]=='A':
            convert_value = '10'
        if value[i]=='B':
            convert_value = '11'
        if value[i]=='C':
            convert_value = '12'
        if value[i]=='D':
            convert_value = '13'
        if value[i]=='E':
            convert_value = '14'
        if value[i]=='F':
            convert_value = '15'
        convert_to_decimal = eval(convert_value)*(source_base**(length_of_value-(i+1)))
        number = number + convert_to_decimal
        the_decimal_number = number
    result=''
    while True: 
        total1 = the_decimal_number % eval(destination_base)
        if total1==10:
            total1='A'
        if total1==11:
            total1='B'
        if total1==12:
            total1='C'
        if total1==13:
            total1='D'
        if total1==14:
            total1='E'
        if total1==15:
            total1='F'
        result=str(total1)+result
        the_decimal_number = the_decimal_number//eval(destination_base)
        if the_decimal_number==0:
            break
    print('The converted number is', result)

    
def main():
    print('BASE CONVERSIONS')
    print('--- We only support base 2 to base 16 conversions ---')
    source_base = input('What is the source base? ')
    destination_base = input('What is the destination base? ')
    if 2 <= eval(source_base) <= 16 and 2 <= eval(destination_base) <= 16:
        value = input('Enter the number that you want to convert: ')
        value = value.upper()
        if validate_the_number(source_base,destination_base,value):
            convert_the_number(source_base,destination_base,value)
        else:
            print('Invalid Number')
    else:
        print('We only support 2 to 16 base')

main()


        
    

            
        
        






    
