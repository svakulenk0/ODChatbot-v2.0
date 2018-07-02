'''
svakulenko
7 Aug 2017

Get data from ES
'''
from elasticsearch import Elasticsearch

INDEX_LOCAL = 'data_gv_at'
INDEX_SERVER = 'atcsv'

INDEX = INDEX_SERVER
N = 2914


class ESClient():

    def __init__(self, index=INDEX, host='localhost', port=9200):
        self.es = Elasticsearch(hosts=[{"host": host, "port": port}])
        self.index = index

    def search(self, keywords, limit=N):
        result = self.es.search(index=self.index, size=limit, body={"query": {"query_string": {"query": keywords}}})
        return result
