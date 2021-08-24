import csv
import os
import xlrd
import statistics

# all topics
life_improvements = [15, 17, 19]
remaining_topics = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24]

# loop over all topics
for topic in range(0, 25):
    count = 0
    file_name = str(topic) + "_results.txt"
    results = open(file_name, "a")

    relevant = open("relevant_comments_from_topics", "r")
    author = open("author", "r")
    author_list = author.readlines()
    relevant_list = relevant.read().split("\n")

    state_to_perc = {}

    distributions = open("theta_distributions-all-monthly-f", "r")
    # loop over all comments and check if comment has current topic

    prev_comment = '-1'
    num_zeros = 0

    for x in distributions:
        x = x.split(' ')
        curr_comment = x[0]
        curr_topic = x[1]
        if (curr_topic == str(topic)):
            curr_perc = float(x[2])
        else:
            curr_perc = 0

        # for a given topic, check if the associated comment is relevant and has author information

        current_author = author_list[int(curr_comment)]

        if (curr_comment != prev_comment or curr_perc != 0) and (curr_comment in relevant_list) and (current_author != "[deleted]"):

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

                                # get location, look up percent, and add to the relevant state
                                state = row[6]

                                if (curr_comment == prev_comment):
                                    percents = state_to_perc[state]
                                    percents = percents[:-1]
                                    state_to_perc[state] = percents

                                if state in state_to_perc:
                                    percents = state_to_perc[state]
                                    percents = percents + [float(curr_perc)]
                                    state_to_perc[state] = percents
                                else:
                                    state_to_perc[state] = [float(curr_perc)]

                                print(count)
                                count += 1

                        f.close()
        prev_comment = curr_comment

    # average values for each state and write to file                          
    for s in state_to_perc:
        all_percentages = state_to_perc[s]
        number = len(all_percentages)
        if number >= 50:
            avg = statistics.mean(all_percentages)
            std = statistics.stdev(all_percentages)
        else:
            avg = -1
            std = -1

        res = s + "  " + str(number) + "     " + str(avg) + "   " + str(std) + "\n"
        results.write(res)

    results.close()   
    distributions.close()
    author.close()
    relevant.close()  
           

