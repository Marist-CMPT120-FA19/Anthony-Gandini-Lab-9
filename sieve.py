#Anthony Gandini

def main():
    n = int(input("Enter a number to find all prime numbers up to: "))
    numbers = []
    for i in range(2 , n+1):
        numbers.append(i)
        
    while len(numbers) > 0:
        current = numbers.pop(0)
        print(current , "is a prime number.")
        
        for j in numbers:
            if j % current == 0:
                numbers.remove(j)
        
main()