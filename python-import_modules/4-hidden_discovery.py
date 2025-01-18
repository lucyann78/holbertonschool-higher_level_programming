import pkgutil
import types

def print_hidden_names():
    # Load the compiled module
    module_name = 'hidden_4'
    module = __import__(module_name)

    # Get all names defined in the module
    names = dir(module)

    # Filter names that do not start with '__' and sort them
    filtered_names = sorted(name for name in names if not name.startswith('__'))

    # Print each name on a new line
    for name in filtered_names:
        print(name)

# This code will not run if the module is imported
if __name__ == "__main__":
    print_hidden_names()
