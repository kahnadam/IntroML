#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#how many people are in this dataset?
print len(enron_data)

#how many features are recorded for each person?
print len(enron_data["SKILLING JEFFREY K"].keys())

#how many people are POIs?
count = 0
for i in enron_data:
    if enron_data[i]["poi"]==1:
        count += 1
    else:
        count = count
print count

#what people are in this dictionary?
#print enron_data.keys()

#what elements are recorded for each person?
print enron_data["SKILLING JEFFREY K"].keys()

#how much stock does James Prentice have?
print enron_data["PRENTICE JAMES"]["total_stock_value"]
