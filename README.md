# Project_Yakir
Project for lerning DevOps

This project provides a basic structure for provisioning virtual machines with specified configurations. It allows users to input machine details, manage machine objects, run setup scripts, and log activities.Table of Contents
User Input & Validation
Class Structure for Machine Representation
Running Bash Scripts from Python
Logging & Error Handling
Project Structure
Next Steps
User Input & ValidationThe get_user_input function collects user input for machine configurations. It prompts the user to enter the machine name, operating system (OS), CPU, and RAM. The entered data is stored in a list and saved to a JSON file.