#!/usr/bin/env python3
'''
    Script that lists all documents in the collection
'''


def list_all(mongo_collection):
    '''
    Function that lists all documents in the collection
    '''
    if mongo_collection is None:
        return []
    else:
        # Return all documents in the collection
        return mongo_collection.find()
