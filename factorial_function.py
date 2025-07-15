def factorial(n):
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    number = int(input("Enter a number:"))
    fact = factorial(number)
    print(f'factorial of {number} is {fact}')
    
    
if __name__ == '__main__':
    main()
    