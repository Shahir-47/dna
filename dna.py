# importing library functions
import sys
import csv

# accept only 3 command line arguements
if len(sys.argv) != 3:
    print("error 404 !!! 3 command line arguments required")
    exit()
# open the csv file and load the str name only so we can later make a dictionary file with each str as columns and below them the corresponding str count
with open(sys.argv[1]) as csvfile:
    data = csv.reader(csvfile)
    for strseq in data:
        database = strseq
        # pop function to omit name comlumn
        database.pop(0)
        break
# open the textfile and convert it to a string variable for substring manipulation
with open(sys.argv[2]) as txtfile:
    dnasample = csv.reader(txtfile)
    for sequence in dnasample:
        temporary = sequence
# store as string so we can use the substring function and manipulate as we please
dnasample = temporary[0]

# create a new dictionary to store the str counts of the given unknwon dna sequence
strcount = {}
for str_seq in database:
    strcount[str_seq] = 1

# search(loop) for each str in the dictionary
for count in strcount:
    counter = 0  # increments if a str found
    highest = 0  # highest count of str
    # loop through the dna sample provided do we can match the str acc to the count in the 1st loop
    for i in range(len(dnasample)):
        # check to avoid repetitions of reading the string again
        # check to reset the counter if consecutive str not found
        while counter > 0:
            counter -= 1
            continue

        # if the string is equal to the str in count
        if dnasample[i: i + len(count)] == count:
            # keep on incrementing the count as long as the previous string equal the current string which is equal to the str (count)
            while dnasample[i - len(count): i] == dnasample[i: i + len(count)]:
                # move to the next set of substring while obeying the condition above
                i = i + len(count)
                counter = counter + 1
            # a check to make sure only the highest str count is stored and not every every count of str
            if counter > highest:
                highest = counter
    # store the maximum number of str count of a particular str in the dictionary
    strcount[count] = strcount[count] + highest

# open the csv file and store it as a dictionary so we can compare the str counts and print the corresponding name
with open(sys.argv[1], newline='') as csvfile:
    database = csv.DictReader(csvfile)
    # loop through the dictionary
    for name in database:
        found = 0  # counter to see how many str match
        for dnamatch in strcount:
            # check if the str count matches
            if strcount[dnamatch] == int(name[dnamatch]):
                found = found + 1
        # if number of str count matches the number of columns of str count print the corresponding name
        if found == len(strcount):
            print(name['name'])
            exit()
    # if no match found print no match
    print("No match")
