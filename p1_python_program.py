def difference_between_first_and_last_digit(number: int) -> int:
    """Return the absolute difference between the first and last digits."""
    digits = [int(ch) for ch in str(abs(number))]
    if not digits:
        return 0
    return abs(digits[0] - digits[-1])


def print_pattern_1_to_n(n: int) -> None:
    """Print the sequence 1, 12, 123, ..., 123...n."""
    for i in range(1, n + 1):
        print(''.join(str(j) for j in range(1, i + 1)))


def is_harshad_number(number: int) -> bool:
    """Return True if a number is divisible by the sum of its digits."""
    if number <= 0:
        return False
    digit_sum = sum(int(ch) for ch in str(number))
    return number % digit_sum == 0


def list_harshad_numbers(limit: int) -> list[int]:
    """Return all Harshad numbers from 1 to limit."""
    return [num for num in range(1, limit + 1) if is_harshad_number(num)]


def main() -> None:
    print("Choose an option:")
    print("1. Difference between first and last digit")
    print("2. Print pattern 1, 12, 123, ...")
    print("3. List Harshad numbers")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print(f"Difference between first and last digit = {difference_between_first_and_last_digit(num)}")

    elif choice == 2:
        n = int(input("Enter the value of n: "))
        print_pattern_1_to_n(n)

    elif choice == 3:
        limit = int(input("Enter a number to find Harshad numbers up to: "))
        values = list_harshad_numbers(limit)
        print(f"Harshad numbers up to {limit}: {values}")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
