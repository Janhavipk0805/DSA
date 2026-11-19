def check_even_odd(number):
    """
    Check if a number is even or odd.

    Parameters:
    number (int): The number to be checked.

    Returns:
    str: A message indicating whether the number is even or odd.
    """

    # Check if the number is even
    if number % 2 == 0:
        # If the remainder is 0 when divided by 2, it's even
        return f"The number {number} is even."
    else:
        # If the remainder is not 0 when divided by 2, it's odd
        return f"The number {number} is odd."

# Example usage
print(check_even_odd(10))  # Output: The number 10 is even.
print(check_even_odd(7))   # Output: The number 7 is odd.