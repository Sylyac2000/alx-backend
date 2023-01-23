#!/usr/bin/env python3
""" a module paginate a database of popular baby names."""

import csv
import math
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index """
    return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return a list of datas"""
        assert isinstance(page, int), "page must be an integer"
        assert page > 0, "page must be a positive integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page_size > 0, "page_size must be a positive integer"

        # index_tuple = index_range(page, page_size)
        # start, end = index_tuple[0], index_tuple[1]

        start, end = index_range(page, page_size)

        # print(start, end)

        thedataset = self.dataset()[start:end]

        return thedataset

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """ return a dict of datas"""

        # get datas from dataset
        thedataset = self.get_page(page, page_size)

        # Total dataset length
        total = len(self.dataset())

        # Total total_pages
        total_pages = math.ceil(total / page_size)

        # Next page
        if(page + 1 < total_pages):
            next_page = page + 1
        else:
            next_page = None

        # Prev page

        if(page - 1 > 0):
            prev_page = page - 1
        else:
            prev_page = None

        adict = {
            'page_size': len(thedataset),
            'page': page,
            'data': thedataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }

        return adict
