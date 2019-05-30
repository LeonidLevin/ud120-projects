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
    data_with_errors = [(ages[ii], net_worths[ii], predictions[ii] - net_worths[ii]) for ii in range(0, len(predictions))]
    data_with_errors.sort(key = lambda x : x[2])
    cleaned_data = data_with_errors[:int(len(data_with_errors) * 0.9)]
    return cleaned_data

