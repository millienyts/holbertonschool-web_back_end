#!/usr/bin/env python3
'''
    Script that updates a document in a collection based on name
'''


def update_topics(mongo_collection, name, topics):
    '''
    Function that updates a document in a collection based on name
    '''
    # Check if mongo_collection is None
    if mongo_collection is None:
        # Return None if collection is None
        return None
    else:
        # Update the document
        mongo_collection.update_many(
            {"name": name}, {"$set": {"topics": topics}})
        # Return None
        return None
