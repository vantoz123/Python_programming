#Function to generate fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
#prompt the user for number of times
num_terms = int(input('Enter the number of fibonacci terns to generate: '))

#check if input is valid
if num_terms <=0:
    print('please enter a positive number')
else:
#Generate and print the Fibonacci sequence
    fibocci_sequence = generate_fibonacci(num_terms)
    print('Fibonacci sequence: ')
    for term in fibocci_sequence:
        print(term)
