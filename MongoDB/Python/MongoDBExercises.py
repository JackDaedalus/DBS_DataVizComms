
# DataVizComm Lectures - March 2020

# Testing a new MongoDB connection..

import pymongo
import re
from pprint import pprint
from datetime import datetime, tzinfo, timezone



def main():

    my_client = pymongo.MongoClient("mongodb+srv://JackDaedalus:Arizona01@dsbdatavizcommcluster-aq99i.mongodb.net/test?retryWrites=true&w=majority")

    my_database = my_client.sample_dbstutorials

    try:
        print("\n\nMongoDB version is {}\n".format(my_client.server_info()['version']))
    except pymongo.errors.OperationFailure as error:
        print(error)
        quit(1)



    #QueryMongoDBTest(my_database) # Exercise 2
    #QueryMongoDBFields1(my_database) # Exercise 3+4
    #QueryMongoDBFields2(my_database) # Exercise 6
    #QueryMongoDBFields3(my_database) # Exercise 9 + 10
    #QueryMongoDBFields4(my_database)  # Exercise 11
    QueryMongoDBFields5(my_database)  # Exercise 11



    my_client.close()
    # End of main function

def QueryMongoDBFields5(my_database):
    print("\nQuery collection fields..#25..\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    # Exercise 33
    filter = {
        'name': re.compile(r"^Mad")
    }
    # Exercise 32
    # filter = {
    #     'name': re.compile(r"mon")
    # }
    # Exercise 25
    # filter = {
    #         '$and':
    #             [
    #                 {'address.coord.1': {'$gt':42}},
    #                 {'address.coord.1': {'$lte':52}}
    #             ]
    # }
    # Exercise 24
    # filter = {
    #         '$and':
    #             [
    #                 {'grades.1.grade': 'A'},
    #                 {'grades.1.score': 9},
    #                 {'grades.1.date': { '$eq': datetime(2014, 8, 11, 0, 0, 0, tzinfo=timezone.utc)}}
    #             ]
    # }
    # Exercise 21
    # filter = {
    #         '$or':
    #             [
    #                 {
    #                     '$nor':
    #                         [
    #                             {'cuisine':'American '},
    #                             {'cuisine':'Chinese'}
    #                         ]
    #                 },
    #
    #                 {'name': re.compile(r"^Wil")}
    #             ]
    # }
    # # Exercise 21
    # filter = {
    #         'grades.score':{'$not':{'$gte':10}}
    # }
    # Exercise 20
    # filter = {
    #     '$nor': [
    #         {'borough': 'Staten Island'},
    #         {'borough': 'Queens'},
    #         {'borough': 'Bronx'},
    #         {'borough': 'Brooklyn'}
    #     ]
    # }
    # Exercise 19
    # filter = {
    #     '$or': [
    #         {'borough': 'Staten Island'},
    #         {'borough': 'Queens'},
    #         {'borough': 'Bronx'},
    #         {'borough': 'Brooklyn'}
    #     ]
    # }
    # Exercise 18
    # filter = {
    #     'borough': 'Bronx',
    #     '$or': [
    #         {'cuisine' : 'American '},
    #         {'cuisine' : 'Chinese'}
    #     ]
    # }

    project = {
        '_id': 0,
        'restaurant_id': 1,
        'name': 1,
        'borough': 1,
        'cuisine': 1,
        #'grades': 0
        #'address.coord': 1
    }
    # sort = list({
    #                  'address.coord.1':-1
    #              }.items())
    skip=0
    limit = 10

    my_cursor = my_collection.find(
        filter=filter,
        projection=project,
        #sort=sort,
        skip=skip,
        limit=limit
    )
    iCursorLocation = 1

    # Print records
    for item in my_cursor: # Exercise 6
        print("\nItem : {}\t\t: {}".format(iCursorLocation, item))
        iCursorLocation += 1



def QueryMongoDBFields4(my_database):
    print("\nQuery collection fields..#16..\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    # Exercise 11
    # filter = {
    #     'address.coord.0': {'$lt':-95.754168}
    # }
    # Exercise 12
    # filter = {
    #     'address.coord.0': {'$lt':-65.754168},
    #     'cuisine': {'$nin':['American ']},
    #     'grades.score': {'$gt':70}
    # }
    # Exercise 13
    # filter = {
    #     'borough': {'$nin':['Brooklyn']},
    #     'cuisine': {'$nin':['American ']},
    #     'grades.grade': 'A'
    # }
    # Exercise 16
    filter = {
        'name': re.compile(r"ces$")
    }
    # Exercise 17
    filter = {
        'name': re.compile(r"Reg")
    }
    project = {
        'restaurant_id': 1,
        'name': 1,
        'borough': 1,
        'cuisine': 1,
        '_id': 0
    }
    sort = list({
                    'cuisine': 1
                }.items())
    skip=0
    limit = 10

    my_cursor = my_collection.find(
        filter=filter,
        projection=project,
        sort=sort,
        skip=skip,
        limit=limit
    )
    iCursorLocation = 1

    # Print records
    for item in my_cursor: # Exercise 6
        print("\nItem : {}\t\t: {}".format(iCursorLocation, item))
        iCursorLocation += 1



def QueryMongoDBFields3(my_database):
    print("\nQuery collection fields..#9..\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    # Exercise 9
    # filter = {
    #     'grades.score': {'$gte':90}
    # }
    # Exercise 10
    filter = {
        'grades.score': {'$gte':80, '$lt':100}
    }
    project = {
        'restaurant_id': 1,
        'name': 1,
        'borough': 1,
        'cuisine': 1,
        '_id': 0
    }
    skip=0
    limit = 100

    my_cursor = my_collection.find(
        filter=filter,
        projection=project,
        skip=skip,
        limit=limit
    )
    iCursorLocation = 1

    # Print records
    for item in my_cursor: # Exercise 6
        print("\nItem : {}\t\t: {}".format(iCursorLocation, item))
        iCursorLocation += 1


def QueryMongoDBFields2(my_database):
    print("\nQuery collection fields..#6..\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    # Exercise 6
    filter = {
        'borough': 'Bronx'
    }
    project = {
        'restaurant_id': 1,
        'name': 1,
        'borough': 1,
        'cuisine': 1,
        '_id': 0
    }
    skip=5
    limit = 5

    my_cursor = my_collection.find(
        filter=filter,
        projection=project,
        skip=skip,
        limit=limit
    )
    iCursorLocation = 1

    # Print records
    for item in my_cursor: # Exercise 6
        print("\nItem : {}\t\t: {}".format(iCursorLocation, item))
        iCursorLocation += 1


def QueryMongoDBFields1(my_database):
    print("\nQuery collection fields..#3..\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    my_cursor = my_collection.find({},{"restaurant_id":1,"name":1,"borough":1, "cuisine":1, "_id":0})
    iCursorLocation = 1

    # Exercise 2 - Print all records
    for item in my_cursor:
        #pprint(item)
        print("\nItem : {}\t\t: {}".format(iCursorLocation, item))
        iCursorLocation += 1


def QueryMongoDBTest(my_database):
    print("\nQuery database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.restaurants

    my_cursor = my_collection.find({})
    iCursorLocation = 1

    # Exercise 2 - Print all records
    for item in my_cursor:
        pprint(item)
        #print("\nItem : {}\t\tName : {}".format(iCursorLocation, item["name"]))
        iCursorLocation += 1



main()

