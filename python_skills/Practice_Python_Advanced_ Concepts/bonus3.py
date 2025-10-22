'''3. Create a small program where invalid user input raises a custom exception,
logs the error, and continues execution instead of crashing.'''

import logging

class InvalidChoiceError(Exception):
    """Raised when input is an integer but not in the allowed range."""

def parse_choice(text: str, low: int = 1, high: int = 5) -> int:
    num = int(text)  # may raise ValueError for non-integers
    if not (low <= num <= high):
        raise InvalidChoiceError(f"Choice must be between {low} and {high}, got {num}")
    return num

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    print("Enter a number from 1 to 5 (or 'q' to quit).")

    while True:
        raw = input("Your choice: ").strip().lower()
        if raw in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        try:
            choice = parse_choice(raw)
        except ValueError:
            logging.error("Non-numeric input received: %r", raw, exc_info=True)
            print("Please enter a valid integer.")
            continue
        except InvalidChoiceError as e:
            logging.error("Invalid choice: %s", e)  # no stack trace needed here
            print(e)
            continue
        else:
            print(f"You picked {choice}. Doing work...\n")
            # ... do something with `choice` and continue loop ...

if __name__ == "__main__":
    main()
