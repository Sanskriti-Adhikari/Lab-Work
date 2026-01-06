import csv

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    with open("info.csv", "r") as file:
        first_line = file.readline().strip()
    with open("info.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["roll", "name"])
        if first_line == "":
            writer.writeheader()
        writer.writerow({"roll": roll, "name": name})

def remove_student():
    roll_remove = input("Enter roll number to remove: ")
    with open("info.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for s in reader:
            if s["roll"] != roll_remove:
                rows.append(s)
    with open("info.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["roll", "name"])
        writer.writeheader()
        for s in rows:
            writer.writerow(s)

def update_student():
    roll_update = input("Enter roll number to update: ")
    with open("info.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for s in reader:
            if s["roll"] == roll_update:
                print("Current name:", s["name"])
                new_name = input("Enter new name: ")
                s["name"] = new_name
            rows.append(s)
    with open("info.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["roll", "name"])
        writer.writeheader()
        for s in rows:
            writer.writerow(s)

def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

main()