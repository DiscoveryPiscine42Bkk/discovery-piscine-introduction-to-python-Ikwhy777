def main():
    try:
        num = int(input("Enter a number to display its multiplication table: "))
        print(f"\nMultiplication table for {num}:")
        for i in range(1, 13):  # You can change 13 to 11 or 21 depending on the desired range
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
