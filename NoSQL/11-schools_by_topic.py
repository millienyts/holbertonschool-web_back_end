#!/usr/bin/env python3
'''
This script will return the schools that teach a specific topic.
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools that teach a specific topic'''

    return mongo_collection.find({"topics": topic})
