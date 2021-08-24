import scipy.stats
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import xlrd
import plotly.express as px

# boolean to also generate the number of comments map
num = False

clusters = {
    "orange" : [0, 20],
    "green" : [17, 15, 19], # # range_color=[0.05, 0.25] when comparing topics in cluster
    "red" : [6, 8, 18, 9, 13, 3, 4],
    "purple" : [1, 5]
    
}

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

topics = {
    0: "Vaccines & Genetics",
    1 : "Epigenetics",
    2 : "Therapeutic Potential of GE",
    3 : "GE Therapy process",
    4 : "Crispr Process/Epigenetics",
    5 : "GE therapy outcome studies",
    6 : "GE across the lifespan",
    7 : "Future uses & media portrayal",
    8 : "GE and heritable mutations",
    9 : "Natural and unnatural evolution",
    10 : "Crispr Therapies & Sci-fi portrayal",
    11 : "Viruses",
    12 : "Evolution & Gene-Editing",
    13 : "How genes work",
    14 : "Human GE Trials",
    15 : "GE in Children & Social Disparity",
    16 : "GE procedures",
    17 : "Ethics",
    18 : "GE in fiction/applications",
    19 : "Advances & Broad Implications",
    20 : "Biomedical Institutions",
    21 : "References to GE fiction/resources",
    23 : "Telomeres & longevity",
    24 : "Pragmatic constraints"
}


# loop over all clusters (can change to topics by updating file_name and figure title)
for cluster in clusters:

    locations = []
    color = []

    # use previously generated averages
    file_name = cluster + "_results.txt"
    results = open(file_name, "r")
    lines = results.readlines()
    for x in lines:
        x = x.split(" ")
        if (x[1] == ''):
            state = x[0]
            perc = float(x[7])
        else:
            state = x[0] + " " + x[1]
            perc = float(x[8])
        state = us_state_abbrev[state]
        if perc != -1:
            locations.append(state)
            color.append(perc)
    results.close()

    fig = px.choropleth(locations=locations, locationmode="USA-states", color=color,scope="usa", title=cluster + ": " + str(clusters[cluster]))
    fig.show()

# optionally generate the map of comment numbers from each state
if num:
    locations = []
    color = []

    file_name = "num_comments.txt"
    results = open(file_name, "r")
    lines = results.readlines()
    for x in lines:
        x = x.split(" ")
        if (x[1] == ''):
            state = x[0]
            number = float(x[2])
        else:
            state = x[0] + " " + x[1]
            number = float(x[3])
        state = us_state_abbrev[state]
        locations.append(state)
        color.append(number)
    results.close()

    fig = px.choropleth(locations=locations, locationmode="USA-states", color=color,scope="usa", title="Number of Comments")
    fig.show()