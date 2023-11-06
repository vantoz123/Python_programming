from ecommerce.shipping import calc_shiping

calc_shiping()
def FindMax(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number>maximum:
            maximum=number
    return maximum
numbers = [2,6,3,10]
print(FindMax(numbers))