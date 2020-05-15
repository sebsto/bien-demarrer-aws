import pymongo
import sys

#
# Download root certificate
# See doc at https://docs.aws.amazon.com/documentdb/latest/developerguide/connect_programmatically.html
#
# wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
#

USER     = "seb"
PASSWORD = "Passw0rd;"
ENDPOINT = "bien-demarrer.cluster-crvu2gzmqwzj.eu-west-3.docdb.amazonaws.com"

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient(f'mongodb://{USER}:{PASSWORD}@{ENDPOINT}:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred') 

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()