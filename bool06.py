def main(a):
    """
    check the following statement "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a % 2 == 0
print(main(4))
print(main(7))
print(main(0))