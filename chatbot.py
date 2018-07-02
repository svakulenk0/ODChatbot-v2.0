#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
2 Jul 2018
'''
from load_ES import ESClient


class Chatbot():
    '''
    Dialog agent for conversational search
    '''
    def __init__(self, limit=6):
        # establish connection to the database
        self.db = ESClient()
        # maximum message size
        self.limit = limit

    def search(self, message='test'):
        bot_response = ''
        words = message.split()
        result = self.db.search(keywords=' AND '.join(words))
        # number of datasets found
        n = result['hits']['total']
        # if at least one dataset found
        if n > 0:
            for doc in result['hits']['hits'][:self.limit]:
                dataset_title = doc["_source"]["raw"]["title"]
                dataset_id = doc["_source"]["raw"]["id"]
                dataset_link = "http://www.data.gv.at/katalog/dataset/%s" % dataset_id
                bot_response += "<br><a href='%s'>%s</a>" % (dataset_link, dataset_title)
        # nothing found
        else:
            bot_response += "Nothing found!"
        return bot_response

    def test(self, message='test'):
        return 'Hi!'


def test_chatbot():
    chatbot = Chatbot()
    print chatbot.test()


def main():
    test_chatbot()


if __name__ == '__main__':
    main()
