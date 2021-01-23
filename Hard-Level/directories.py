import os

project = input("Project name: ")
number_of_stages = int(input("How many stages? "))
py = input("Name of .py file: ")
os.makedirs(f"{project}", exist_ok=True)
readme = open(f"{project}\\README.md", "a+")
readme.close()
for num in range(1, number_of_stages + 1):
    stage_name = input(f"Enter stage {num} name: ")
    os.makedirs(f"{project}\\Stage {num} {stage_name}", exist_ok=True)
    readme = open(f"{project}\\Stage {num} {stage_name}\\README.md", "a+")
    readme.close()
    python_module = open(f"{project}\\Stage {num} {stage_name}\\{py}.py", "a+")
    python_module.close()
