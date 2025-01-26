import os

def execute_shell_command(command):
    os.system(command)  # Command Injection vulnerability

def redundant_function():
    print("This is a redundant function.")
    return True
