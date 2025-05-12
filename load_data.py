#Import packages
import pymongo
import csv

# Connect to MongoDB and create collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongodb"]
mycol = mydb["telemtry"]

#Specify the file path
file_path = "data.csv"

#Convert data to csv dict, convert to a list and insert into collection
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    csv_list = list(csv_reader)
    mycol.insert_many(csv_list)
    print("Sucessfully inserted")