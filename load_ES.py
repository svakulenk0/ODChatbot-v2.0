'''
svakulenko
2 Jul 2018

Get data from ES
'''
from elasticsearch import Elasticsearch

# config tuple: (host, port, index name)
CONFIG = ('csvengine', 9200, 'at_csv_geo')

FACETS = {
            "title": "dataset.dataset_name^5",
            "dataset_description": "dataset.dataset_description",
            "cell_value": "row.values.value",
            "publisher": "dataset.publisher",
            "metadata_entities": "metadata_labels",
            "data_entities": "data_labels"
         }

SEARCH_LIMIT = 20


class ESClient():

    def __init__(self, host=CONFIG[0], port=CONFIG[1], index=CONFIG[2]):
        self.es = Elasticsearch(hosts=[{"host": host, "port": port}])
        self.index = index

    def search(self, keywords, limit=SEARCH_LIMIT):
        '''
        request keywords from the Elasticsearch datasets index
        '''

        search_query = {
                "_source": ["dataset.dataset_name", "dataset.dataset_link"],
                "query":
                    {
                     "query_string":
                        {
                         "query": keywords,
                         "default_operator": "AND",
                         "analyzer": "german",
                         "fields": list(FACETS.values())
                        }
                     },
                'highlight':
                    {
                     "pre_tags" : ["*"],
                     "post_tags" : ["*"],
                     'fields': {
                                'row.values.value': { "number_of_fragments" : 3 },
                                'dataset.dataset_description': {}
                               }
                    }
                }
        result = self.es.search(index=self.index, size=limit, body=search_query)
        return result
