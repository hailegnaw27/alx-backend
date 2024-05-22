#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in self.
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded.
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            else:
                self.order.remove(key)
                self.order.append(key)

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't.
        """
        return self.cache_data.get(key)
