#  Suitable database and store the data in batches
This is project to create a database using mongoDB which can be replicable using docker. 

The database is created using an image thorugh a container in which data is loaded using a python script. 

All the process is automated by a dockerfile which creates the container with the image of mongoDB and then loads the data using a previously created script in python.

Data for this project was taken from https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k?resource=download.

To run this project, it is needed to first access the folder through a command prompt and then run the following commands:

This allows to create the image:
- docker build -t my-image .

This allows to run the image:
- docker run --name mongodb -d -p 27017:27017 my-image