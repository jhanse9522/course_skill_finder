from pathlib import *
current_dir = Path.cwd()
home_dir = Path.home()

print("current_dir:", current_dir)
print("home_dir", home_dir)

paths = []

for p in paths:



records = filein.split("Course_Title:")  #splits text into records (list of strings)
records.pop(0)

for record in records:

    print(record)
    print(".............................................")
    print()

print("total record len:", len(records))
print("records sample checks:")
print("records[0]:", records[0])
print("records[1]:", records[1])
print("records[2]", records[2])
