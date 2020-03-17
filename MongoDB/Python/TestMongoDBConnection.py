
# DataVizComm Lectures - March 2020

# Testing a new MongoDB connection..

import pymongo


def main():

    my_client = pymongo.MongoClient("mongodb+srv://JackDaedalus:Arizona_1@dsbdatavizcommcluster-aq99i.mongodb.net/test?retryWrites=true&w=majority")

    my_database = my_client.test

    try:
        print("\n\nMongoDB version is {}\n".format(my_client.server_info()['version']))
    except pymongo.errors.OperationFailure as error:
        print(error)
        quit(1)

    deleteMongoDBDocuments(my_database)
    InsertDocumentTest(my_database)
    QueryMongoDBTest(my_database)
    QueryMongoDBCalorieQuery(my_database)
    QueryMongoDBCalorieNestedQuery(my_database)
    updateMongoDB(my_database)


    # End of main function


def InsertOneDocument(my_collection):
    print("\nInserting one document...\n")

    my_collection.insert_one({
                                "_id": 1,
                                "name": "pizza",
                                "calories": 266,
                                "fats": {
                                    "saturated": 4.5,
                                    "trans": 0.2
                                        },
                                "protein": 11
                            })

def InsertMultipleDocuments(my_collection):
    print("\nInserting multiple documents...\n")

    my_collection.insert_many([
        {
            "_id": 2,
            "name": "hamburger",
            "calories": 295, "protein": 17,
            "fats": {"saturated": 5.0, "trans": 0.8},
        },
        {
            "_id": 3,
            "name": "taco",
            "calories": 226, "protein": 9,
            "fats": {"saturated": 4.4, "trans": 0.5},
        }
    ])



def InsertDocumentTest(my_database):

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    InsertOneDocument(my_collection)
    InsertMultipleDocuments(my_collection)

def QueryMongoDBTest(my_database):
    print("\nQuery database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    my_cursor = my_collection.find({"name":"pizza"})
    iCursorLocation = 1

    for item in my_cursor:
        print("\nItem : {}\t\tName : {}".format(iCursorLocation, item["name"]))
        iCursorLocation += 1

    # Output is:
    # pizza
    # hamburger
    # taco


def QueryMongoDBCalorieQuery(my_database):
    print("\nQuery database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    my_cursor = my_collection.find({"calories": { "$lt": 280 }})
    iCursorLocation = 1

    for item in my_cursor:
        print("\nName : {}\t\tCalories : {}".format(item["name"], item["calories"]))
        iCursorLocation += 1

    # Output is:
        # Name: pizza, Calories: 266
        # Name: taco, Calories: 226


def QueryMongoDBCalorieNestedQuery(my_database):
    print("\nQuery database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    my_cursor = my_collection.find({"fats.trans": { "$gte": 0.5 }})
    iCursorLocation = 1

    for item in my_cursor:
        print("\nName : {}\t\tTrans Fats : {}".format(item["name"], item["fats"]["trans"]))
        iCursorLocation += 1


def updateMongoDB(my_database):
    print("\nUpdate database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    my_collection.update_many(
        {"name": "taco"},  # query
        {
            "$set": {  # new data
                "fiber": 3.95,
                "sugar": 0.9
            }
        }
    )


def deleteMongoDBDocuments(my_database):
    print("\nDelete documents in database\n")

    # Create/connect to Collection in MongoDB
    my_collection = my_database.foods

    my_collection.delete_many({
        "calories": {
        "$lt": 300
        }
    })
    # Deletes all the three documents


main()

