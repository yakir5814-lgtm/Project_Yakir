import json

def get_user_input():
    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")

        instance_data = {"name": name, "os": os, "cpu": cpu, "ram" : ram}

        # Validate input (to be implemented by the student)
        # Example: validate_instance_input(instance_data)
        machines.append(instance_data)

    return machines
