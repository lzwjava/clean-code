import os
import re
import argparse


def clean_code(input_file):
    if not input_file.endswith(".py"):
        print("Error: Input file must have a '.py' extension.")
        return

    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    with open(input_file, 'r') as file:
        code = file.read()

    cleaned_code = re.sub(r'(?:^|\n)\s*""".*?"""', '', code, flags=re.DOTALL)
    cleaned_code = re.sub(r'#.*', '', cleaned_code)

    filename, file_extension = os.path.splitext(input_file)
    output_file = f"{filename}_c{file_extension}"

    with open(output_file, 'w') as file:
        file.write(cleaned_code)

    print(f"Cleaned code saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Clean Python code by removing comments.")
    parser.add_argument("input_file", help="Input Python file to clean (must have a '.py' extension).")
    args = parser.parse_args()
    clean_code(args.input_file)


if __name__ == "__main__":
    main()
