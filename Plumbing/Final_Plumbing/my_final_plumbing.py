import pathlib

fhand = open("DPS_Stage4")



filein = fhand.read()


file_names = ["IS452AGAU","IS590WFO","IS590ADV","INFO490ML2","IS490DA","IS590DV","IS538", "LIS559NA","IS590BAO","IS562AO","IS590MD","LIS590DW","IS590DT","SP191IS590APO","IS542A"]
# filename_list is a list of file names, strings that represent what you want to name each file where the string (subtext) will go
# record_list is list of records -- strings, each needing a separate file home

records = filein.split("Course_Title:")  #splits text into records (list of strings)  # break up large file into iterable chunks-> index into each text collected in the list of texts <records>
records.pop(0) # pop off trash in beginning
length = len(records[3])
print("Test checking Record 3: Start bit:")

print("--------")
print(records[3][:2000])  # index into record at item 3 of list, sub-indexing into the characters to check where chunk starts end
print()
print()
print("*End bit")
print("--------")
print(records[3][(length-200):])  # check where chunk ends
print("--------")
print("DONE WITH TEST!")
print("----------------------------------------")

#for record in records:

    #print(record)
   # print(".............................................")
   # print()

# print("total record len:", len(records))
# print("records sample checks:")
# print("records[0]:", records[0])
# print("records[1]:", records[1])
# print("records[2]", records[2])
course_descriptions =[]                         # collect subtext/target blob

for record in records:                           # iterate over list of texts
    start = record.find("Course_Description")    # find start position of target phrase (subtext/blob to extract)
    course_subtext = record[start:]              # grab blob/subtext to extract (course description subtext)
    course_descriptions.append(course_subtext)   # collect blob
    print("start:", course_subtext)              # display to test



course_dict = dict(zip(file_names,course_descriptions))   # just zip up the 2 lists to make a dictionary of values with file_names as keys
print("course_dict of keys: file_names, values: course_descriptions")
print(len(records))
print(len(file_names))
print(course_dict)

# Nope -- not this way (tried first)

# for i in records:
#     if course_dict[file_names[i]] in course_dict:
#         continue
#     course_dict[file_names[i]]= records[i]
# print("COURSE DICT!!!!!!!!! ----------------------")
# print(course_dict)





# for item in collect_subtext:
#
#     print()
#     print("the start of course description blob:")
#     print(item[:100])
#     print("---------------------------")
#     print()

# def text_to_outfiles(record_list, filename_list):
#
#     for i in range(len(record_list)):                       # for this proj: for i in range len 15 files -> # data chunks
#
#         fileout = open('courses/'+filename_list[i], "w")   #create new blank files with list of made names and place in 'courses' folder, defers to how many data files
#         print(record_list[i], file=fileout)                   #print data (each item from list accessed by index) to my new, blank files which are in courses folder
#         print(record_list[i], "has been written to", filename_list[i])  # data has been written to files (one by one)
#
# my_outfiles = text_to_outfiles(records,file_names)  # call my function and save in variable my_outfiles
#
#
# paths = pathlib.Path("courses").glob("*")           # get relative path object and assign all files in courses directory to object <paths>
#
# for p in paths:                                     # for each file (path object)
#     text = p.read_text()
#

#
# # this is where blob is grabbed. blob is then accessed in functions in files where libraries imported
# # gets sent away and returned
#
#
#
#
#                                                         # read it
# #     print(text[:100])                               # print first 100 characters
# #     print("done")
#     #print("-----------------------------------------------------------------------------------------------")
#
#     # blob = text.split("Course_Description")
#     # print("length of blob is...")
#     # print(len(blob))
#     # print("printing item 0 of list:")
#     # print(blob[0])
#     # print("printing item 1 of list:")
#     # if len(blob) > 1:
#     #     print(blob[1])
#     print("---------------------------------------------------------------------------")
