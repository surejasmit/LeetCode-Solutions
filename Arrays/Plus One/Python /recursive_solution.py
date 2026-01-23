def plusOne(digits):
    """
    Recursive approach to handle carry.
    """

    def add_one(index):
        if index < 0:
            digits.insert(0, 1)
            return

        if digits[index] < 9:
            digits[index] += 1
        else:
            digits[index] = 0
            add_one(index - 1)

    add_one(len(digits) - 1)
    return digits


# Example usage
if __name__ == "__main__":
    print(plusOne([9]))       # [1, 0]
    print(plusOne([9, 9]))    # [1, 0, 0]
