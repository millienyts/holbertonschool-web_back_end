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
    num_logs = collection.estimated_document_count()
    print(f"{num_logs} logs")

    # Number of methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Check status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
