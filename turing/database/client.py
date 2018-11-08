from pymongo import MongoClient
>>> client = MongoClient()


class Client(object):

    def __init__(self):

        self.client = MongoClient()
