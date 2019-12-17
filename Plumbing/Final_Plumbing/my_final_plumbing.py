import pathlib


fhand = open("DPS_Stage4")



filein = fhand.read()


file_names = ["IS452AGAU","IS590WFO","IS590ADV","INFO490ML2","IS490DA","IS590DV","IS538", "LIS559NA","IS590BAO","IS562AO","IS590MD","LIS590DW","IS590DT","SP191IS590APO","IS542A"]
# filename_list is a list of file names, strings that represent what you want to name each file where the string (subtext) will go
# record_list is list of records -- strings, each needing a separate file home

records = filein.split("Course_Title:")  #splits text into records (list of strings)  # break up large file into iterable chunks
records.pop(0) # pop off trash in beginning
print("records[3], a test:")
print(records[3])
print("DONE!")

#for record in records:

    #print(record)
   # print(".............................................")
   # print()

# print("total record len:", len(records))
# print("records sample checks:")
# print("records[0]:", records[0])
# print("records[1]:", records[1])
# print("records[2]", records[2])


def text_to_outfiles(record_list, filename_list):

    for i in range(len(record_list)):                       # for this proj: for i in range len 15 files -> # data chunks

        fileout = open('courses/'+filename_list[i], "w")   #create new blank files with list of made names and place in 'courses' folder, defers to how many data files
        print(record_list[i], file=fileout)                   #print data (each item from list accessed by index) to my new, blank files which are in courses folder
        print(record_list[i], "has been written to", filename_list[i])  # data has been written to files (one by one)

my_outfiles = text_to_outfiles(records,file_names)  # call my function and save in variable my_outfiles


paths = pathlib.Path("courses").glob("*")           # get relative path object and assign all files in courses directory to object <paths>

for p in paths:                                     # for each file (path object)
    text = p.read_text()

                                                        # read it
    print(text[:100])                               # print first 100 characters
    print("done")
    print("-----------------------------------------------------------------------------------------------")
