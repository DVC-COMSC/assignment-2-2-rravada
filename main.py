def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = int(input('Enter the celcius here: '))
    fahrenheit = (celcius*9/5)+32
    print(fahrenheit)
    print("Average %.2f" % fahrenheit)
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
