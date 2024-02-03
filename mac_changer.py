import subprocess

def change_mac_address(interface, new_mac):
    # PowerShell command to change MAC address
    ps_command = f'Get-NetAdapter -Name {interface} | Set-NetAdapter -MacAddress {new_mac}'
    command = ["powershell.exe", "-Command", ps_command]

    # Run the PowerShell command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    error = process.communicate()
    
    if process.returncode == 0:
        print(f"MAC address changed successfully to {new_mac} on interface {interface}.")
    else:
        print(f"Error changing MAC address on interface {interface}.")
        print("Error:", error)

def reset_mac_address(interface):
    # PowerShell command to reset MAC address
    ps_command = f'Get-NetAdapter -Name {interface} | Set-NetAdapter -MacAddress ([System.Net.NetworkInformation.PhysicalAddress]::None)'
    command = ["powershell.exe", "-Command", ps_command]

    # Run the PowerShell command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output and errors
    error = process.communicate()

    # Check if there were any errors
    if process.returncode == 0:
        print(f"MAC address reset to original on interface {interface}.")
    else:
        print(f"Error resetting MAC address on interface {interface}.")
        print("Error:", error)

# Ask the user for options
print("Choose an option:")
print("1. Change MAC address")
print("2. Reset MAC address")

option = input("Enter option (1/2): ")

# Replace "Ethernet" with the name of your network interface
interface_name = "Ethernet"

if option == "1":
    new_mac_address = input("Enter the new MAC address: ")
    change_mac_address(interface_name, new_mac_address)
elif option == "2":
    reset_mac_address(interface_name)
else:
    print("Invalid option selected.")
