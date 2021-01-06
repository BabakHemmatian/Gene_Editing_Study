from collections import Counter, namedtuple, defaultdict
import numpy as np
import pandas as pd
import csv

# READ LINES INTO LIST (STRIP)
output_file = open("top_ten_subreddits", "w")
with open("subreddit", "r") as file:
    subreddits = [line.rstrip("\n") for line in file]
    subreddits = Counter(subreddits)
    top_ten = subreddits.most_common(10)
    for subreddit in top_ten:
        output_file.write("{}\n".format(subreddit))
#Make dictionary: key = subreddit, values = []


top_subreddit_names, top_subreddit_values = map(list, zip(*top_ten))

#print(top_subreddit_names, top_subreddit_values)
subreddits_dict = {"AskReddit" : [], "science" : [], "Futurology": [], "askscience" : [], "worldnews" : [],
                   "todayilearned" : [], "explainlikeimfive" : [], "changemyview" : [], "biology" : [], "news" : []}

#populate dictionary with comment IDs
with open("subreddit", "r") as file:
    for idx, line in enumerate(file):
        if line.strip() in top_subreddit_names:
            line = line.strip()
            subreddits_dict[line].append(idx)


for sub in subreddits_dict.keys():
    print(len(subreddits_dict[sub]))
    print(subreddits_dict[sub][0:10])

#transforming theta file
theta_file = pd.read_csv("/Users/njjones14/Documents/Gene_Editing_Study/LDA_True_50/theta_distributions-all-monthly-f", delim_whitespace=True, names = ["comment_index", "topic_index", "topic_contribution"])

#print(theta_file)

relevant_topics = [3, 7, 10, 11, 13, 14, 15, 16, 17, 22, 24, 26, 39, 43, 46, 47, 49]
input_dict = {"AskReddit" : [], "science" : [], "Futurology": [], "askscience" : [], "worldnews" : [], "todayilearned" : [], "explainlikeimfive" : [], "changemyview" : [], "biology" : [], "news" : []}

def add_zeros():
    for key in input_dict:
        input_dict[key].append(0)
    return input_dict

for _ in range(50):
    add_zeros()

print(len(input_dict["AskReddit"]))

##Now I have a dictionary with keys = Subreddits, values = empty list (length = 50) populated with zeros
list_of_lists = []
for sub in subreddits_dict:
    for idx, row in theta_file.iterrows():
        if row["comment_index"] in subreddits_dict[sub] and row["topic_index"] in relevant_topics:
            input_dict[sub][int(row["topic_index"])] += row["topic_contribution"]

    my_array = np.array(input_dict[sub])
    my_int = len(subreddits_dict[sub])
    input_dict[sub] = my_array/my_int
    print(input_dict[sub])
    list_of_lists.append(input_dict[sub]) #will give me list of 10 lists, each with length 50


my_df = pd.DataFrame(list_of_lists)
my_df.to_csv('subreddit_contributions_for_visuals.csv', header=False)



# field_names = ["subreddit"]
# numbers = list(range(0,50))
# for i in numbers:
#     field_names.append(str(i))#give me subreddit, 0-49
#
# with open('subreddit_contributions_for_visuals.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     for idx, l in enumerate(list_of_lists):
#         writer.writerow(idx,l)
#
#
