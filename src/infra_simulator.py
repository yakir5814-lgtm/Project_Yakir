# infra_simulator.py

from src.machine import Machine

def main():
    # Create an instance of Machine
    machine1 = Machine(name="Excavator", model="CAT 320", serial_number="123456789")
    
    # Get dictionary representation
    machine_info = machine1.to_dict()
    print(machine_info)

if __name__ == "__main__":
    main()