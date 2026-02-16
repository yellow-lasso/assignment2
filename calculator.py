def prompt_number(prompt_text: str) -> float:
    """Prompt until the user enters a valid number."""
    while True:
        raw = input(prompt_text).strip()
        try:
            return float(raw)
        except ValueError:
            print("That doesn't look like a number. Please enter a numeric value (e.g., 3, -2, 4.5).")


def prompt_operator() -> str:
    """Prompt until the user enters a valid arithmetic operator."""
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input("Enter an operator (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operator. Please enter one of: +, -, *, /")


def prompt_second_number(op: str) -> float:
    """Prompt for the second number; handle divide-by-zero by reprompting if needed."""
    while True:
        num2 = prompt_number("Enter the second number: ")
        if op == "/" and num2 == 0:
            print("Division by zero is not allowed. Please enter a non-zero second number.")
            continue
        return num2


def calculate(num1: float, op: str, num2: float) -> float:
    """Compute the arithmetic result."""
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    return num1 / num2  # Division


def format_number(n: float) -> str:
    """Pretty formatting: show whole numbers without trailing .0."""
    if n.is_integer():
        return str(int(n))
    return str(n)


def main() -> None:
    num1 = prompt_number("Enter the first number: ")
    op = prompt_operator()
    num2 = prompt_second_number(op)

    result = calculate(num1, op, num2)

    print(
        f"The result of {format_number(num1)} {op} {format_number(num2)} is {format_number(result)}."
    )

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
