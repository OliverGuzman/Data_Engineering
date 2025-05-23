#Import packages
import pymongo
import csv
import pandas as pd

# Connect to MongoDB and create collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongodb"]
mycol = mydb["telemtry"]

#Specify the file path
file_path = "data.csv"

#Verify if it is a valid csv file
try:
    df = pd.read_csv(file_path)
    print(f"Valid CSV file found with following characteristics: {len(df)} rows, {len(df.columns)} columns")

#Handle exceptions for empty files and any other errors
except pd.errors.EmptyDataError:
    print("No data found in file")
except Exception as e:
    print(e)
            
#Convert data to csv dict, convert to a list and insert into collection
try:
    with open(file_path, 'r') as file:
        
        csv_reader = csv.DictReader(file, delimiter=',')
        csv_list = list(csv_reader)
        mycol.insert_many(csv_list)
        print("Sucessfully inserted")

except Exception as e:
    print(e)

