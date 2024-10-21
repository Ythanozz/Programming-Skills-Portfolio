def check_even_odd(number):           #defined the function to check if a number is odd or even
    
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd"
    #equation for a number to check if it is odd, it will print "it is odd" and if its even, it will print its even"


def main():
    question = (input("Insert a number, I will determine if it is odd or even: "))    #defined the function where user inputs number
    
    try:                    #defined try function to handle exceptions if number is valid for checking for odd or even
        number = int(question)
        
        result = check_even_odd(number)
        
        print(result)
        # if user inputs something that isnt a number, this will send the message below
    except ValueError:
        
        print("This is not a valid number.")
    
main()