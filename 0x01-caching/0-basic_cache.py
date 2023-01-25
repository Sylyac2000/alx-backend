#!/usr/bin/env python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching :
      - is a caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """ return an item by key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data.get(key)
