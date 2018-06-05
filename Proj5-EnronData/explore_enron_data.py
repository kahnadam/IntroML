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

#how many emails from this person to a POI?
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#how many stock options exercised by this person?
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#total payments to CEO, chairman, and CFO
print "CEO: " + str(enron_data["SKILLING JEFFREY K"]["total_payments"])
print "Chairman: " + str(enron_data["LAY KENNETH L"]["total_payments"])
print "CFO: " + str(enron_data["FASTOW ANDREW S"]["total_payments"])

#all items in dictionary for one person. Returns 'NaN' when no data available
print enron_data["COLWELL WESLEY"].values()

#how many people have a quantified salary?
sal_count = 0
sal_nan = 0
for i in enron_data:
    if enron_data[i]["salary"] != 'NaN':
        sal_count += 1
    else:
        sal_nan += 1
print "Salary data for " + str(sal_count) + " people"
print "No salary data for " + str(sal_nan) + " people"

#how many people have a known email address? (Same qu as above, different way of answering)
print len(dict((key, value) for key, value in enron_data.items() if value["email_address"] != "NaN"))

#how many people have NaN for total_payments? What % is this?
missing_tot_pay = len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == "NaN"))
print missing_tot_pay
print float(missing_tot_pay) / float(len(enron_data))

#how many POIs are missing their total_payments? What % of POIs is this?
poi_missing_tot_pay = len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == "NaN" and value["poi"] == 1))
print poi_missing_tot_pay
print float(poi_missing_tot_pay) / float(count_POI)
