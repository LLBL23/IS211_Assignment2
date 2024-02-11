# import requests module
import requests

# import csv module
import csv

# import datetime module
from datetime import datetime

# import logging module
import logging
import sys


def downloadData(url):
    """
    Download data from URL and return it as a string
    """
    # read the URL
    response = requests.get(url)

    return response.text


def processData(data):
    """
    Return data as a dictionary. (name, birthday) tuple mapped to person's ID and logs an error if birthday is the incorrect format
    """
    # reader = csv.reader(data)
    # print(next(reader))

    datalines = data.split('\n')
    data_dict = {}
    # separate date from string
    for i, line in enumerate(datalines):
        if i == 0:
            continue
        if len(line) == 0:
            continue
        datalines_split = line.split(',')
        id = int(datalines_split[0])
        name = datalines_split[1]
        date = datalines_split[2]
        # convert string to datetime obj
        try:
            datetime_obj = datetime.strptime(date, '%d/%m/%Y')
            # convert name and birthday to Tuple
            data_tuple = (name, datetime_obj)
            # return dictionary with key = ID : (name, birthday)
            data_dict[id] = data_tuple
            # log invalid ValueErrors for invalid date/incorrect format
        except ValueError:
            logging.error(f"Error processing line # {i} for ID # {id}")

    return data_dict
            
            
def displayPerson(id, personData = {}):
    """
    Print name and birthday of given user identified by the input id
    """
    #store the input id
    id_to_search = id

    if data_dict.get(id_to_search) is not None:
        #search id and get dictionary values
        id_found = data_dict[id_to_search]
        print((f"Person # {id_to_search} is {data_tuple.index[0]} with a birthday of {data_tuple.index[1]}"))
    else:
        print("No user found with that id")


if __name__=='__main__':
    """
    Piecing all functions together. Call when script runs
    """
    #user sends URL to script
    #url = input("Enter url ")

    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    #if string call downloadData function
    csvData = downloadData(url)
    print("************ all data ************")

    person_dict = processData(csvData)
    print("************ Person 2 ************")
    print(person_dict[2])
