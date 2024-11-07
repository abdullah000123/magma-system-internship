import os

# Define the directory containing your text files
directory = '/home/abdullah/abdullah-dev/object-detection/customfruit-data/Orange/test/labels'

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Process only text files
        file_path = os.path.join(directory, filename)
        
        # Read file lines and update if needed
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Process each line and replace the leading '0' with '1' if found
        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts[0] == '1':
                parts[0] = '2'
            updated_lines.append(" ".join(parts))

        # Write back the modified content to the file
        with open(file_path, 'w') as file:
            file.write("\n".join(updated_lines))

print("Processing complete. Files have been updated.")
