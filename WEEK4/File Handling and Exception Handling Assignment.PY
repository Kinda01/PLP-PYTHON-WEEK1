def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the entire content

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content from '{input_filename}' was successfully modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: An issue occurred while reading or writing the file.")
def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    
    try:
        # Try opening the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: An issue occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
