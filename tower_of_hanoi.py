"""
Tower of Hanoi Implementation
Data Structures and Algorithms Project

This program demonstrates recursion
by solving the Tower of Hanoi problem.
"""


def tower_of_hanoi(number_of_disks, source, auxiliary, destination):

    # Base case:
    # If there is only one disk, move it directly
    if number_of_disks == 1:
        print(
            f"Move disk 1 from {source} to {destination}"
        )
        return


    # Step 1:
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(
        number_of_disks - 1,
        source,
        destination,
        auxiliary
    )


    # Step 2:
    # Move the largest disk to destination
    print(
        f"Move disk {number_of_disks} from {source} to {destination}"
    )


    # Step 3:
    # Move remaining disks from auxiliary to destination
    tower_of_hanoi(
        number_of_disks - 1,
        auxiliary,
        source,
        destination
    )



# Main Program

print("===== Tower of Hanoi =====")

disks = int(input("Enter number of disks: "))


print("\nSteps to solve Tower of Hanoi:\n")


tower_of_hanoi(
    disks,
    "A",
    "B",
    "C"
)