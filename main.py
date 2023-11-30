import re
import sys

if len(sys.argv) != 2:
    print("Usage: python clean_code.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, 'r') as file:
    code = file.read()

cleaned_code = re.sub(r'(?:^|\n)\s*""".*?"""', '', code, flags=re.DOTALL)
cleaned_code = re.sub(r'#.*', '', cleaned_code)

filename, file_extension = input_file.rsplit('.', 1)

output_file = f"{filename}_c.{file_extension}"

with open(output_file, 'w') as file:
    file.write(cleaned_code)

print(f"Cleaned code saved to {output_file}")
