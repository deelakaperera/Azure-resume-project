import os
import sys
import json
from jsonschema import validate

file_path = os.getenv('INPUT_FILE')
# file_path = r'C:\Users\deela\Documents\GitHub\Azure-resume-project/infra/web-hosting.json'


def validate_json_syntax(d):
    try:
        return json.loads(d)
    except ValueError as e:
        print('DEBUG: JSON data contains an error')
        print("ERROR: ", e)
        return False


if __name__ == "__main__":
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            print("File loaded to test...")
    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to load file '{file_path}': {e}")
        sys.exit(1)



    jsd = validate_json_syntax(data)

    schema = {
        "type": "object",
        "properties": {
        "firstName": { "type": "string"},
        "lastName": { "type": "string"}
        }
    }
    #output will be None
    print(validate(jsd, schema), "\nINFO: JSON tests passed succesfully")
