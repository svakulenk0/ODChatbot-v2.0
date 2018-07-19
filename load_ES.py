'''
svakulenko
2 Jul 2018

Get data from ES
'''
from elasticsearch import Elasticsearch

# config tuple: (index_name, port)
LOCAL_ES = ('data_gv_at', 9200)
SERVER_ES = ('atcsv', 9202)

CONFIG = SERVER_ES
N = 2914


class ESClient():

    def __init__(self, index=CONFIG[0], host='localhost', port=CONFIG[1]):
        self.es = Elasticsearch(hosts=[{"host": host, "port": port}])
        self.index = index

    def search(self, keywords, limit=N):
        result = self.es.search(index=self.index, size=limit, body={"query": {"query_string": {"query": keywords}}})
        return result
