#!/usr/bin/env python3
def main():
    try:
        total_bottles = int(input("Enter the number of bottles to start counting down from (up to 100): "))
        if total_bottles <= 0 or total_bottles > 100:
            raise ValueError("Invalid input. Please enter a number between 1 and 100.")
    except ValueError as e:
        print(e)
        exit()

    for bottles in range(total_bottles, 0, -1):
        print(f"{bottles} bottles of beer on the wall!")
        print(f"{bottles} bottles of beer! You take one down, pass it around!")
        
        if bottles - 1 != 0:
            print(f"{bottles - 1} bottles of beer on the wall!")
        else:
            print("OUT OF BOTTLES")
           
if __name__ == "__main__":
    main()