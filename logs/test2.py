## **1. User Input & Validation**
# Sample structure to collect user input and validate it.
import json

def collect_user_input():
    machines_list = []
    while True:
        machine_name = input("Enter machine name (or 'done' to finish): ")
        if machine_name.lower() == 'done':
            break
        operating_system = input("Enter OS (Ubuntu/CentOS): ")
        cpu_cores = input("Enter CPU (e.g., 2vCPU): ")
        ram_size = input("Enter RAM (e.g., 4GB): ")
        
        machine_details = {
            "name": machine_name,
            "os": operating_system,
            "cpu": cpu_cores,
            "ram": ram_size
        }
        # Validate input (to be implemented by the student)
        # Example: validate_instance_input(machine_details)
        machines_list.append(machine_details)
    
    return machines_list

# Save to file
machine_instances = collect_user_input()
with open("configs/instances.json", "w") as file:
    json.dump(machine_instances, file, indent=4)

## **2. Class Structure for Machine Representation**
# Basic class structure for managing machine objects
class Computer:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        print(f"Provisioning {self.name}: {self.os}, {self.cpu}, {self.ram}")

# Example usage:
example_machine = Computer("web-server", "Ubuntu", "2vCPU", "4GB")
example_machine.log_creation()

## **3. Running Bash Scripts from Python**
import subprocess

def execute_setup_script():
    try:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        print("[INFO] Nginx installation completed.")
    except subprocess.CalledProcessError as error:
        print(f"[ERROR] Failed to install Nginx: {error}")

# Example call:
# execute_setup_script()

## **4. Logging & Error Handling**
import logging

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(message, level="info"):
    if level == "error":
        logging.error(message)
    else:
        logging.info(message)
    print(message)

# Example usage:
log_message("Provisioning started.")
log_message("Provisioning failed due to network issue.", level="error")

## **5. Structuring the Project for Modularity**
# Example of how to split the project into multiple files and import them.
# src/__init__.py (empty file to make this a package)

# src/machine.py
class Computer:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

# src/logger.py
import logging

def configure_logging():
    logging.basicConfig(
        filename='logs/provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

logger = configure_logging()

# Example of using the logger
# logger.info("This is a log message")

# main.py (Example integration)
from src.machine import Computer
from src.logger import logger

def main():
    database_machine = Computer("db-server", "CentOS", "4vCPU", "8GB")
    logger.info(f"Provisioning {database_machine.name}")
    print(database_machine.to_dict())

if __name__ == "__main__":
    main()

## **Next Steps**
# - Extend validation logic
# - Integrate more services
# - Replace mock provisioning with AWS/Terraform when those modules are learned