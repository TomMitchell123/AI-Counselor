import json

def extract_academic_policies(filename):
    academic_policies = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == "Academic Policies":
                i += 1
                while i < len(lines) and lines[i].strip() != "Academic Policies":
                    key = lines[i].strip()
                    i += 1
                    value = ""
                    while i < len(lines) and lines[i].strip() != "Academic Policies":
                        value += lines[i]
                        i += 1
                    academic_policies[key] = value.strip()
            else:
                i += 1
    return academic_policies

filename = "output.txt"
academic_policies = extract_academic_policies(filename)

with open('output_policies.json', 'w') as json_file:
    json.dump(academic_policies, json_file, indent=4)
    print("Data saved to output_policies.json")