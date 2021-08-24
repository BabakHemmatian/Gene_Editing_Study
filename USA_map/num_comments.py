import csv
import os
import xlrd
import statistics

count = 0
file_name = "num_comments.txt"
results = open(file_name, "a")

relevant = open("relevant_comments_from_topics", "r")
author = open("author", "r")
author_list = author.readlines()
relevant_list = relevant.read().split("\n")

state_to_num = {}

distributions = open("theta_distributions-all-monthly-f", "r")


prev_comment = '-1'

# loop over all comments and sum state
for x in distributions:
    x = x.split(' ')
    curr_comment = x[0]

    # for a given comment, check if the associated comment is relevant and has author information

    current_author = author_list[int(curr_comment)]

    if (curr_comment != prev_comment) and (curr_comment in relevant_list) and (current_author != "[deleted]"):

        # find author location, pass if fewer than 10 or not US
        for root,dirs,files in os.walk("location"):
            for file in files:
                if file.endswith(".csv"):
                    f = open("location/" + file, "r")
                    file_data = f.readlines()
                    for i in range(len(file_data)):
                        row = file_data[i].split(",")

                        # check conditions on author
                        if (row[0] + "\n" == current_author) and (int(row[3]) >= 10) and (row[7] == 'US\n'):

                            # get location, add to relevant state tally
                            state = row[6]

                            if state in state_to_num:
                                number = state_to_num[state]
                                state_to_num[state] = number + 1
                            else:
                                state_to_num[state] = 1

                            print(count)
                            count += 1

                    f.close()
    prev_comment = curr_comment
                                
for s in state_to_num:

    res = s + "  " + str(state_to_num[s]) + "\n"
    results.write(res)

results.close()   
distributions.close()
author.close()
relevant.close() 