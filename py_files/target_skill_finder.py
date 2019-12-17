filein = open("DPS_Stage4", "rt")

my_file = filein.read()

line_list = my_file.split("\n")


#print(my_file)

print("and now for the list loop of lines which is exactly the same but lines can be accessed by position")

target_skills = []
n = int(input("please list the number of skills you would like to search for: "))
for i in range(0,n):
    skill = input("please list the skill you would like to search for: ")
    target_skills.append(skill)
print("searching for these target skills::", target_skills)


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

#["curation", "cleaning", "scraping", "storage", "copyright", "processing", "automation", "management", "warehousing", "analytics", "modeling", "modelling", "business", "web", "data", "python", "statistics", "visualization", "database", "design", "warehousing"]
