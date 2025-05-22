import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Define colors per depth level
DEPTH_COLORS = [
    Fore.GREEN,   # Level 0 - parent
    Fore.MAGENTA, # Level 1 - child
    Fore.YELLOW,  # Level 2 - "video" or deep child
    Fore.CYAN,    # Level 3+
    Fore.RED,
    Fore.BLUE
]

def get_color_by_depth(depth):
    if depth < len(DEPTH_COLORS):
        return DEPTH_COLORS[depth]
    else:
        return Style.DIM  # Default for deep levels

def list_folders(directory, depth=0):
    try:
        items = sorted(os.listdir(directory))
        for item in items:
            path = os.path.join(directory, item)
            if os.path.isdir(path):
                color = get_color_by_depth(depth)
                print('  ' * depth + color + item + Style.RESET_ALL)
                list_folders(path, depth + 1)
    except PermissionError:
        print('  ' * depth + Fore.RED + "[Permission Denied]")

if __name__ == "__main__":
    # Change this to your target directory
    target_directory = "/home/mouse/Documents/elHacker"
    list_folders(target_directory)
