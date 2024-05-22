#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system with.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data.
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD:
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key:
                    print("DISCARD: {}".format(self.last_key))
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist.
        """
        return self.cache_data.get(key)
