def plusOne(digits):
    """
    Adds one to the number represented by digits array
    using reverse traversal.
    """
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all digits were 9
    return [1] + digits


# Example usage
if __name__ == "__main__":
    print(plusOne([1, 2, 3]))   # [1, 2, 4]
    print(plusOne([9, 9, 9]))   # [1, 0, 0, 0]
