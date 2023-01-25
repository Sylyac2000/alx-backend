#!/usr/bin/env python3
""" FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching :
      - is a caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                fst_key = list(self.cache_data.keys())[0]
                fst_item = self.cache_data.pop(list(self.cache_data.keys())[0])
                print('DISCARD: ', fst_key)

    def get(self, key):
        """ return an item by key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data.get(key)
