#!/usr/bin/env python3
'''
    Script that inserts a new document in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Function that inserts a new document in a collection based on kwargs
    '''
    # Check if mongo_collection is None
    if mongo_collection is None:
        # Return None if collection is None
        return None
    else:
        # Insert the new document
        return mongo_collection.insert_one(kwargs).inserted_id
