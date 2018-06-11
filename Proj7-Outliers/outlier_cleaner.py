#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    from operator import itemgetter

    def calculate_error(x,y): 
        z = x-y
        return z**2

    errors = map(calculate_error, predictions, net_worths)
    data = zip(ages, net_worths, errors) 
    data.sort(key=itemgetter(2), reverse=True) s
    to_remove = int(round(len(predictions)*0.1)) 
    del data[0:to_remove+1]

    return data

