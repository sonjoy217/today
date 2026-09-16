def sum_of_odds_from_id(student_id):
    # Convert input to string and remove all whitespace
    sanitized = "".join(str(student_id).split())

    # Empty input or invalid characters
    if not sanitized or not sanitized.isdigit():
        return 0

    # Sum of individual digit values
    total = sum(int(digit) for digit in sanitized)

    # Cumulative sum of all odd integers from 1 to total
    odd_sum = sum(
        number for number in range(1, total + 1)
        if number % 2 != 0
    )

    return odd_sum