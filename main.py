import argparse
from app.calculator import add, sub


def main():
    parser = argparse.ArgumentParser(description="Simple calculator demo with add and sub.")
    parser.add_argument("operation", choices=["add", "sub"], help="Operation to perform")
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.a, args.b)
    else:
        result = sub(args.a, args.b)

    print(f"Result: {result}")
    print("change something")


if __name__ == "__main__":
    main()
