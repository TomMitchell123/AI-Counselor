import json

def extract_academic_policies(filename):
    academic_policies = {"Policies": []}
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == "Academic Policies":
                i += 1
                while i < len(lines) and lines[i].strip() != "Academic Policies":
                    title = lines[i].strip()
                    i += 1
                    values = []
                    while i < len(lines) and lines[i].strip() != "Academic Policies":
                        values.append(lines[i].strip())
                        i += 1
                    # Concatenate values into a single string
                    values_concatenated = ' '.join(values)
                    academic_policies["University Policies"].append({"Title of Academic Policy": title, "University Academic Policy Explained": values_concatenated})
            else:
                i += 1
    return academic_policies

filename = "output.txt"
academic_policies = extract_academic_policies(filename)

with open('output_policies.json', 'w') as json_file:
    json.dump(academic_policies, json_file, indent=4)
    print("Data saved to output_policies.json")
