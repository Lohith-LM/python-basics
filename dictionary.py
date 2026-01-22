# Creating a dictionary
student = {
    "name": "Lohith",
    "branch": "CSE AIML",
    "year": 2
}

# Accessing values
print("Name:", student["name"])
print("Branch:", student["branch"])

# Adding a new key-value pair
student["college"] = "Engineering College"

print("Updated dictionary:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
