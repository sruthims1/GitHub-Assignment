# ==============================================================================
# Python Script to Grep Wi-Fi Lines
# This script reads a file named 'wifi_paragraph.txt' and prints
# any line that contains the substring "Wi-Fi".
# ==============================================================================

# Define the filename to be processed.
filename = "wifi_paragraph.txt"

try:
    # Open the file for reading. The 'with' statement ensures the file is
    # automatically closed after we're done with it.
    with open(filename, 'r') as file:
        # Iterate over each line in the file.
        for line in file:
            # Check if the string "Wi-Fi" is present in the line.
            # The 'if' condition is case-sensitive, so it matches "Wi-Fi" exactly.
            if "Wi-Fi" in line:
                # If a match is found, print the line to the console.
                # The .strip() method removes any leading/trailing whitespace,
                # including the newline character, for cleaner output.
                print(line.strip())

except FileNotFoundError:
    # This block handles the case where the file does not exist.
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    # This is a general error handler for any other issues that might occur.
    print(f"An unexpected error occurred: {e}")

