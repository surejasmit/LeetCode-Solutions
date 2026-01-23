def plusOne(digits):
    """
    Converts digit array to number, adds one,
    then converts back to digit array.
    """
    num = int("".join(map(str, digits)))
    num += 1
    return list(map(int, str(num)))


# Example usage
if __name__ == "__main__":
    print(plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
