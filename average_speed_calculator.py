def average_speed_calculator():
    print("Welcome to the Average Speed Calculator!")

    while True:
        print("\nPlease choose the distance unit:")
        print("1. Miles")
        print("2. Kilometers")
        distance_choice = input("Enter the number corresponding to the distance unit: ")

        if distance_choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue

        distance = float(input("Please type the distance: "))

        print("\nPlease choose the time unit:")
        print("1. Hours")
        print("2. Minutes")
        time_choice = input("Enter the number corresponding to the time unit: ")

        if time_choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue

        time = float(input("Please type the travel time: "))

        # Convert time to hours if it is in minutes
        if time_choice == '2':
            time /= 60  # Convert minutes to hours

        # Calculate the average speed
        average_speed = distance / time

        # Determine the unit for the average speed
        if distance_choice == '1':  # Miles
            if time_choice == '1':  # Time in hours
                unit = "mph"
            else:  # Time in minutes
                unit = "mpm"  # miles per minute
        else:  # Kilometers
            if time_choice == '1':  # Time in hours
                unit = "km/h"
            else:  # Time in minutes
                unit = "kpm"  # kilometers per minute

        # If the time was in minutes, calculate the speed in miles per minute or kilometers per minute
        if time_choice == '2':
            average_speed = distance / (time * 60)  # Calculate the speed for minutes

        print(f"The average speed was {average_speed:.2f} {unit}.")

        another_calculation = input("Would you like to calculate another average speed? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("Thank you for using the Average Speed Calculator and don't forget: don't drink and drive! Goodbye!")
            break

if __name__ == "__main__":
    average_speed_calculator()


