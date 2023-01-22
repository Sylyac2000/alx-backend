#!/usr/bin/env python3
""" a module that takes two integer arguments page and page_size."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index """
    return (page * page_size - page_size, page * page_size)
