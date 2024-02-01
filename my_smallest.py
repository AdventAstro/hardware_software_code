def get_smallest(smallest,value):
    if smallest is None:
        snakkest = value
    elif value < smallest:
        smallest = value
    return get_smallest

def main():
    smallest = None
    while True:
        num = input("Enter a number: ") .lower()
        if num == "done":
            break
        smallest = get_smallest(smallest, num)
        print("Smallest number is:", smallest)

if __name__ == "__main__":
    main()
