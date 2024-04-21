def extract_academic_policies(filename):
    academic_policies = {"University Policies": []}
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == "Academic Policies":
                i += 3
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