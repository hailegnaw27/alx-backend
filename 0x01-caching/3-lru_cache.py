#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRUCache is a caching system with an LRU eviction policy
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(first_key))
                self.cache_data.pop(first_key)

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data, return None.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

