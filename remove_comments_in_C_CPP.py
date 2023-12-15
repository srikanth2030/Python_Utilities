import re
import os
import sys

def clean_up_cpp(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            code = infile.read()

            # Remove multiple consecutive empty lines
            code = re.sub(r'\n\s*\n', '\n\n', code)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(code)

        print(f"Code cleaned up and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def remove_comments(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            code = infile.read()

            # Remove /* ... */ comments
            code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

            # Remove // comments
            code = re.sub(r'//.*', '', code)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(code)

        print(f"Comments removed and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_comments.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        remove_comments(input_file, 'Temp.cpp')
        clean_up_cpp('Temp.cpp', output_file)
        os.remove('Temp.cpp')
