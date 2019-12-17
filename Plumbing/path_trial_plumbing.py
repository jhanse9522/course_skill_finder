from pathlib import *
current_dir = Path.cwd()
home_dir = Path.home()

print("current_dir:", current_dir)
print("home_dir", home_dir)

# get file paths



# loop over paths

# read documents

# grab course descriptions ->

        #-> Build up a dictionary here {"file_path":"course description blah", }



# for p in paths:
#
#
# spot = file_in.find("Eligibility")   # Example of just a word subtext to extract
# end_spot = spot + len("Eligibility")

 # = my_file.find(spot) + len(spot)
 # = my_file[toc_start_pos:toc_end_pos]
 #
 # = toc_string.split("\n")

# print(file_in[spot:end_spot])  # just figuring it out here
#
# print(end_spot)
# print("i")
# print(file_in[end_spot])
# print(file_in[spot])

def find_subtext(file_in, stringy):  # takes file object and string you want extracted from text

    spot = file_in.find(stringy)  # get start spot of characters
    end_spot = spot + len(stringy)  # get end spot of characters, grabs one more than needed to allow for exclusive range
    results = file_in[spot:end_spot]
    print(results)
    return results

