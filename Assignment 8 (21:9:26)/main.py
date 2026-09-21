# File Handling Assignment
# Name: Atharva Parande

def count_lines(filename):
    with open(filename, "r") as file:
        count = sum(1 for line in file)
    return count


def extract_first_two_lines(filename):
    lines = []

    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i == 2:
                break
            lines.append(line)

    return lines


def write_to_file(filename, lines):
    with open(filename, "w") as file:
        file.writelines(lines)


# Main Program
input_file = "input.txt"
output_file = "output.txt"

total_lines = count_lines(input_file)
print("Total number of lines:", total_lines)

first_two_lines = extract_first_two_lines(input_file)

print("\nFirst two lines:")
for line in first_two_lines:
    print(line.strip())

write_to_file(output_file, first_two_lines)

print("\nFirst two lines have been written to output.txt")