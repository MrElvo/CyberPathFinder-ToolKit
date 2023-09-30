import subprocess
import os
import base64
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define a list of foreground colors in rainbow order
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# Replace this with your base64-encoded logo
encoded_logo = """
LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyAgX18gICAgIF9fX19fX19fX18gIF9fX19fXwojICBcIFwgICAvIF9fX18vIF9fIFwvIF9fX18vCiMgICBcIFwgLyAvICAgLyAvXy8gLyAvXyAgICAKIyAgIC8gXy8gL19fXy8gX19fXy8gX18vICAgIAojICAvXyhfXF9fX18vXy8gICAvXy8gICAgICAgICAgICAgICAgICAgICAgICAgICAgIAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpXZWxjb21lIHRvIG15IFRvb2xraXQgLSAKTWFkZSBCeSBDeWJlclBhdGhGaW5kZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCg==
"""

# Decode the base64-encoded logo
logo_text = base64.b64decode(encoded_logo).decode('latin-1')

# Split the contents of the logo text by lines
logo_lines = logo_text.splitlines()

# Print each line from the logo text in a different rainbow color
for i, line in enumerate(logo_lines):
    # Use the modulo operator to cycle through the rainbow colors
    color = rainbow_colors[i % len(rainbow_colors)]
    # Print the line in the selected color
    print(Style.BRIGHT + color + line.strip() + Style.RESET_ALL)

# Initialize the target variable
target = ""

def run_nmap(flags):
    command = ["nmap"]
    if flags:
        command.extend(flags.split())
    command.append(target)
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", " ".join(command) + " && sleep 999999"])

def run_dirsearch(flags):
    command = ["dirsearch", "-r", "-u", target]
    if flags:
        command.extend(flags.split())
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", " ".join(command) + " && sleep 999999"])

def run_burp_suite():
    subprocess.Popen(["burpsuite"])

def run_nikto():
    command = ["nikto", "-h", target]
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", " ".join(command) + " && sleep 999999"])

def flag_list_menu(tool_name):
    while True:
        help_choice = input(Style.BRIGHT + f"\nDo you want to see {tool_name} flags? (y/n): ")
        if help_choice.lower() == 'y':
            if tool_name == 'Nmap':
                print(Fore.BLUE + Style.BRIGHT + "\nNmap Flags:\n" + Style.RESET_ALL) 
                print("-v: Increase verbosity level (use -vv or more for higher levels)")
                print("-A: Enable OS detection, version detection, script scanning, and traceroute")
                print("-sV: Attempts to determine the version of the services running on open ports.")
                print("-sS: Performs a SYN scan, which is stealthy and commonly used for initial reconnaissance.")
                print("-O: Enables OS detection, trying to identify the operating system of the target.")
                print("-p: Specifies target ports to scan. For example, -p 80,443 scans ports 80 and 443\n")
                # Add more Nmap flags and descriptions here
            elif tool_name == 'Dirsearch':
                print(Fore.BLUE + Style.BRIGHT + "\nDirsearch Flags:\n" + Style.RESET_ALL)
                print("-r: Enable recursive mode")
                print("-u <URL>: Specify the target URL")
                print("-t <threads>: Sets the number of concurrent threads for the scan. Increasing threads can speed up the scan.")
                print("-w <wordlist>: Specifies a custom wordlist for directory and file brute-force.")
                print("-e <ext>: Specifies file extensions to search for. For example, -e php,html restricts the search to PHP and HTML files.")
                print("-x <exclusions>: Excludes specified status codes from the output. For example, -x 404,403 excludes HTTP 404 and 403 errors.\n")
                # Add more Dirsearch flags and descriptions here
            # Add more tools and their flag descriptions here

            flags = input(Style.BRIGHT + "\nEnter the flags (leave blank for default): ")
            if not flags:
                flags = ""

            if tool_name == 'Nmap':
                run_nmap(flags)
            elif tool_name == 'Dirsearch':
                run_dirsearch(flags)
            # Add more tool-specific flag processing here
            elif tool_name == 'Burp Suite':
                run_burp_suite()
            elif tool_name == 'Nikto':
                run_nikto()
            break
        elif help_choice.lower() == 'n':
            flags = input(Style.BRIGHT + "\nEnter the flags (leave blank for default): ")
            if not flags:
                flags = ""
            if tool_name == 'Nmap':
                run_nmap(flags)
            elif tool_name == 'Dirsearch':
                run_dirsearch(flags)
            # Add more tool-specific flag processing here
            elif tool_name == 'Burp Suite':
                run_burp_suite()
            elif tool_name == 'Nikto':
                run_nikto()
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid choice. Please try again\n" + Style.RESET_ALL)

# Define the run_both function
def run_both(nmap_flags, dirsearch_flags):
    # Run Nmap in a new terminal
    nmap_command = ["nmap"]
    if nmap_flags:
        nmap_command.extend(nmap_flags.split())
    nmap_command.append(target)
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", " ".join(nmap_command) + " && sleep 999999"])

    # Run dirsearch in a new terminal
    dirsearch_command = ["dirsearch", "-r", "-u", target]
    if dirsearch_flags:
        dirsearch_command.extend(dirsearch_flags.split())
    dirsearch_command = " ".join(dirsearch_command) + " && sleep 999999"
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", dirsearch_command])

def run_file_download():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nFile Download Menu:")
        print("1. Download with wget")
        print("2. Download with curl")
        print("3. Go Back to Main Menu")
        
        choice = input(Style.BRIGHT + "\nEnter your choice: ")
        
        if choice == '1':
            wget_download_menu()
        elif choice == '2':
            curl_download_menu()        
        elif choice == '3':
            break 
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid choice. Please try again\n" + Style.RESET_ALL)

def wget_download_menu():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nChoose what to download with wget:")
        print("1. Download linpeas.sh")
        print("2. Enter a different URL")
        print("3. Go Back")
        
        choice = input(Style.BRIGHT + "\nEnter your choice: ")
        
        if choice == '1':
            url = "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"
            file_name = "linpeas.sh"
            download_file_with_wget(url, file_name)
        elif choice == '2':
            url = input(Style.BRIGHT + "\nEnter URL: ")
            download_file_with_wget(url)
        elif choice == '3':
            break           
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid choice. Please try again\n" + Style.RESET_ALL)

def download_file_with_wget(url, file_name="downloaded_file"):
    file_name = input(Style.BRIGHT + f"How to name the file '{file_name}'? ")
    if not file_name:
        file_name = "downloaded_file"
    subprocess.Popen(["wget", url, "-O", file_name])
    print(Fore.GREEN + Style.BRIGHT + f"\nDownloading file from {url} as '{file_name}'...\n" + Style.RESET_ALL)

def curl_download_menu():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nChoose what to download with curl:")
        print("1. Download linpeas.sh")
        print("2. Enter a different URL")
        print("3. Go Back")
        
        choice = input(Style.BRIGHT + "\nEnter your choice: ")
        
        if choice == '1':
            url = "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"
            file_name = "linpeas.sh"
            download_file_with_curl(url, file_name)
        elif choice == '2':
            url = input(Style.BRIGHT + "\nEnter the URL to download from: ")
            download_file_with_curl(url)
        elif choice == '3':
            break 
        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid choice. Please try again\n" + Style.RESET_ALL)

def download_file_with_curl(url, file_name="downloaded_file"):
    file_name = input(Style.BRIGHT + f"How to name the file '{file_name}'? ")
    if not file_name:
        file_name = "downloaded_file"
    subprocess.Popen(["curl", url, "-o", file_name])
    print(Fore.GREEN + Style.BRIGHT + f"\nDownloading file from {url} as '{file_name}'...\n" + Style.RESET_ALL)

while True:
    if not target:
        target = input(Style.BRIGHT + "\nEnter the target (IP or URL): ")
        print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}" + Style.RESET_ALL)  # Show the current target in red and bold

    print(Fore.GREEN + Style.BRIGHT + "\nMain Menu:")
    print("1. Run Nmap")
    print("2. Run Dirsearch")
    print("3. Run Nmap + Dirsearch")
    print("4. Run Burp Suite")
    print("5. Run Nikto")
    print("6. File Download Menu")
    print("7. Change Target")
    print("8. Exit")

    choice = input(Style.BRIGHT + "\nEnter your choice: ")

    if choice == '1':
        flag_list_menu('Nmap')
        print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}\n" + Style.RESET_ALL)  # Show the current target in red and bold
    elif choice == '2':
        flag_list_menu('Dirsearch')
        print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}\n" + Style.RESET_ALL)  # Show the current target in red and bold
    elif choice == '3':
        help_choice = input(Style.BRIGHT + "\nDo you want to see Nmap and Dirsearch flags? (y/n): ")
        if help_choice.lower() == 'y':
            print(Fore.BLUE + Style.BRIGHT + "\nNmap Flags:\n" + Style.RESET_ALL)
            print("-v: Increase verbosity level ( use -vv or more for higher levels )")
            print("-A: Enable OS detection, version detection, script scanning, and traceroute")
            print("-sV: Attempts to determine the version of the services running on open ports.")
            print("-sS: Performs a SYN scan, which is stealthy and commonly used for initial reconnaissance.")
            print("-O: Enables OS detection, trying to identify the operating system of the target.")
            print("-p: Specifies target ports to scan. For example, -p 80,443 scans ports 80 and 443\n")
            print(Fore.BLUE + Style.BRIGHT + "\nDirsearch Flags:\n" + Style.RESET_ALL)
            print("-r: Enable recursive mode")
            print("-u <URL>: Specify the target URL")
            print("-t <threads>: Sets the number of concurrent threads for the scan. Increasing threads can speed up the scan.")
            print("-w <wordlist>: Specifies a custom wordlist for directory and file brute-force.")
            print("-e <ext>: Specifies file extensions to search for. For example, -e php,html restricts the search to PHP and HTML files.")
            print("-x <exclusions>: Excludes specified status codes from the output. For example, -x 404,403 excludes HTTP 404 and 403 errors.\n")
            nmap_flags = input(Style.BRIGHT + "\nEnter Nmap flags (leave blank for default): ")
            dirsearch_flags = input(Style.BRIGHT + "\nEnter Dirsearch flags (leave blank for default): ")
            run_both(nmap_flags, dirsearch_flags)
            print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}\n" + Style.RESET_ALL)  # Show the current target in red and bold
        else:
            nmap_flags = input(Style.BRIGHT + "\nEnter Nmap flags (leave blank for default): ")
            dirsearch_flags = input(Style.BRIGHT + "\nEnter Dirsearch flags (leave blank for default): ")
            run_both(nmap_flags, dirsearch_flags)
            print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}\n" + Style.RESET_ALL)  # Show the current target in red and bold
    elif choice == '4':
        run_burp_suite()
    elif choice == '5':
        run_nikto()
    elif choice == '6':
        run_file_download()
    elif choice == '7':
        new_target = input(Style.BRIGHT + "\nEnter a new target (IP or URL): ")
        if new_target:
            target = new_target
        print(Fore.RED + Style.BRIGHT + f"\nCurrent Target: {target}" + Style.RESET_ALL)  # Show the current target in red and bold
    elif choice == '8':
        goodbye_message = "\nGoodbye! :) I hope you got what you need!\n"
        rainbow_line = "".join([Style.BRIGHT + rainbow_colors[i % len(rainbow_colors)] + char + Style.RESET_ALL for i, char in enumerate(goodbye_message)])
        print(rainbow_line)
        break
