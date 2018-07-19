#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
svakulenko
2 Jul 2018
'''
from .load_ES import ESClient
from .model import Model


class Chatbot():
    '''
    Dialog agent for conversational search
    '''
    def __init__(self, limit=6):
        # establish connection to the database
        self.db = ESClient()
        # maximum message size
        self.limit = limit
        # load the pre-trained model
        # -model tsdf-OD
        self.model = Model('OD')
        self.model.load_model()

    def search(self, message='ich suche data über wien'):
        items = []
        response, bspan = self.model.infer(message)
        print ("%s (%s)" % (response, bspan))

        # look up extracted keywords in the database
        keywords = bspan.strip(' EOS_Z1')
        print ('Searching for' % keywords)
        result = self.db.search(keywords=keywords)

        # number of datasets found
        n = result['hits']['total']

        # if at least one dataset found
        if n > 0:
            for doc in result['hits']['hits'][:self.limit]:
                dataset_title = doc['_source']['dataset']['dataset_name']
                dataset_id = doc["_id"]
                dataset_link = "http://data.wu.ac.at/odgraphsearch/render/" + dataset_id
                items.append("[%s](%s)" % (dataset_title, dataset_link))
            return "\n\n".join(items)

        # nothing found
        else:
            return "Nothing found!"


def test_chatbot():
    chatbot = Chatbot()
    print(chatbot.search())


def main():
    test_chatbot()


if __name__ == '__main__':
    main()
