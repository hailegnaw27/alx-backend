#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """ LFUCache is a caching system
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method should not do anything.
        If the number of items in
        you must discard the least frequency used item (LFU algorithm)
        If there is a tie, discard the least recently used item among them
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [
                    k for k,
                    freq in self.usage_frequency.items() if freq == min_freq]
                if len(lfu_keys) == 1:
                    lfu_key = lfu_keys[0]
                else:
                    # If there's a tie, use the order to find the least
                    # recently used
                    lfu_key = next(
                        k for k in self.usage_order if k in lfu_keys)

                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                del self.usage_order[lfu_key]

            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
