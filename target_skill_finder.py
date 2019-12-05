filein = open("syllabus_project", "rt")

my_file = filein.read()

line_list = my_file.split("\n")


print(my_file)

print("and now for the list loop of lines which is exactly the same but lines can be accessed by position")

target_skills = ["curation", "cleaning", "scraping", "storage", "copyright", "processing", "automation", "management", "warehousing", "analytics", "modeling", "modelling", "business", "web", "data", "python", "statistics", "visualization", "database", "design", "warehousing"]
word_freq = {}
for line in line_list:
    words = line.split()
    for word in words:
        if word in target_skills:
            print()
            print("found word:", word.upper())
            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word]=1


print("target skill count:", word_freq)






print(line)

filein.close()
