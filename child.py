# Child Vaccination Management System - Console Based

class Child:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.vaccinations = []

    def __str__(self):
        return f"Child: {self.name}, Birth Date: {self.birth_date}, Vaccinations: {[v.name for v in self.vaccinations]}"

class Vaccination:
    def __init__(self, name, description, recommended_age):
        self.name = name
        self.description = description
        self.recommended_age = recommended_age

    def __str__(self):
        return f"Vaccination: {self.name}, Recommended Age: {self.recommended_age} months"

class Appointment:
    def __init__(self, child, vaccination, appointment_date):
        self.child = child
        self.vaccination = vaccination
        self.appointment_date = appointment_date
        self.status = 'Scheduled'

    def __str__(self):
        return f"Appointment for {self.child.name} - {self.vaccination.name} on {self.appointment_date}, Status: {self.status}"

class VaccinationManagementSystem:
    def __init__(self):
        self.children = []
        self.vaccinations = []
        self.appointments = []

    def add_child(self, name, birth_date):
        child = Child(name, birth_date)
        self.children.append(child)
        print(f"Added child: {child}")

    def list_children(self):
        if not self.children:
            print("No children registered.")
        else:
            for i, child in enumerate(self.children, 1):
                print(f"{i}. {child}")

    def add_vaccination(self, name, description, recommended_age):
        vaccination = Vaccination(name, description, recommended_age)
        self.vaccinations.append(vaccination)
        print(f"Added vaccination: {vaccination}")

    def list_vaccinations(self):
        if not self.vaccinations:
            print("No vaccinations available.")
        else:
            for i, vaccination in enumerate(self.vaccinations, 1):
                print(f"{i}. {vaccination}")

    def schedule_appointment(self, child_index, vaccination_index, appointment_date):
        try:
            child = self.children[child_index - 1]
            vaccination = self.vaccinations[vaccination_index - 1]
            appointment = Appointment(child, vaccination, appointment_date)
            child.vaccinations.append(vaccination)
            self.appointments.append(appointment)
            print(f"Scheduled: {appointment}")
        except IndexError:
            print("Invalid child or vaccination selection.")

    def list_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for i, appointment in enumerate(self.appointments, 1):
                print(f"{i}. {appointment}")

def main():
    system = VaccinationManagementSystem()

    while True:
        print("\nChild Vaccination Management System")
        print("1. Add Child")
        print("2. List Children")
        print("3. Add Vaccination")
        print("4. List Vaccinations")
        print("5. Schedule Appointment")
        print("6. List Appointments")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            birth_date = input("Enter child's birth date (YYYY-MM-DD): ")
            system.add_child(name, birth_date)

        elif choice == '2':
            system.list_children()

        elif choice == '3':
            name = input("Enter vaccination name: ")
            description = input("Enter vaccination description: ")
            recommended_age = int(input("Enter recommended age (in months): "))
            system.add_vaccination(name, description, recommended_age)

        elif choice == '4':
            system.list_vaccinations()

        elif choice == '5':
            system.list_children()
            child_index = int(input("Select a child by number: "))
            system.list_vaccinations()
            vaccination_index = int(input("Select a vaccination by number: "))
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            system.schedule_appointment(child_index, vaccination_index, appointment_date)

        elif choice == '6':
            system.list_appointments()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
