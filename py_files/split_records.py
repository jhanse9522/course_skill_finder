fhand = open("DPS_Stage4")
filein = fhand.read()


    # course description substring


records = filein.split("Course_Title:")  #splits text into records (list of strings) -> still 1 file -> at processing stage -> chunked and ready to send out
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

#lines = filein.split("\n")

#for line in lines:
   # if "course_description" in line:
        #print(line)

# course_descriptions = filein.split("course_description")
#
# #print(course_descriptions)
#
# for description in course_descriptions:
#     print(description)
#     print("next")







