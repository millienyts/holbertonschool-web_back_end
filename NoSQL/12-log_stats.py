#!/usr/bin/env python3
'''
    Script that provides some stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


if __name__ == "__main__":
    '''
        Function that provides some stats about Nginx logs stored in MongoDB
    '''
    # Number of logs
    client = MongoClient('mongodb://127.0.0.1:27017/')
    collection = client.logs.nginx

    # Number of documents
    print(f"{collection.estimated_document_count()} logs")

    # Number of methods
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        # Print only if there are logs for that method
        print(f"\tmethod {method}: {count}")

    # Check status
    get = collection.count_documents({"method": "GET", "path": "/status"})
    # Print only if there are logs for that method
    print(f"{get} status check")
