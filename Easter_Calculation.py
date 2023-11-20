import math

def calculate_easter_date(year):
    C = year // 100
    Y = year % 100

    m = (15 + C - (C // 4) - ((8 * C + 13) // 25)) % 30
    n = (4 + C - (C // 4)) % 7

    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = (19 * c + m) % 30
    e = (2 * a + 4 * b + 6 * d + n) % 7

    date = 22 + d + e

    if (d == 29 and e == 6) or (d == 28 and e == 6 and (m == 2 or m == 5 or m == 10 or m == 13 or m == 16 or m == 21 or m == 24 or m == 39)):
        date -= 7

    if date > 31:
        # April
        month = "April"
        date -= 31
    else:
        # March
        month = "March"

    return f"Easter in {year} is on {month} {date}"

# Get the user's input
user_year = int(input("Enter a year: "))

# Calculate and print the date of Easter for the entered year
result = calculate_easter_date(user_year)
print(result)
