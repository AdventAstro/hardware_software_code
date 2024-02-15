def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal_to_binary

def decimal_to_binary(decimal_num):
    binary = bin(decimal_num)[2:]
    return binary

def main():
    print "My Binary Conversion Calculator"
    print("1.Binary to Decimal")
    print("2.Decimal to Binary")

    choice = in:(input("Enter your choice (1 or 2: "))

    if choice == 1:
        binary_input = input("Enter binary number ")
        decimal_result = binary_to_decimal(binary_input)
        print(f"Decimal equivalent: {decimal_result} )

    elif choice == 2
        decimal_input = int(input("Enter decimal number: "))
        binary_result = decimal_to_binary(decimal_input)
        print(f"Binary equivalent: {binary_result} )

    else:
        print("Invalid choice. Please enter 1 or 2.")

if__name__ = "__main__":
            main()
