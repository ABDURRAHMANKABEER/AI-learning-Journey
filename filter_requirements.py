keep_packages = {
    "ipykernel",
    "jupyter_client",
    "matplotlib",
    "numpy",
    "pandas",
    "scikit-learn",
    "scipy",
    "seaborn",
}

with open("requirements.txt", "r") as infile:
    lines = infile.readlines()

filtered_lines = []

for line in lines:
    pkg = line.strip().split("==")[0].lower()
    if pkg in keep_packages:
        filtered_lines.append(line)

with open("requirements_minimal.txt", "w") as outfile:
    outfile.writelines(filtered_lines)

print("Minimal requirements saved to requirements_minimal.txt")
