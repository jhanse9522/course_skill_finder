fhand = open("play_syllabus_prototype")
filein = fhand.read()

records = filein.split("course_title")  #splits text into records (list of strings)

print(records)
print(len(records))

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
#     print()






