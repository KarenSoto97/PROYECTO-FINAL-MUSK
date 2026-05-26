
"""
functional_utils.py

Utility functions following a functional programming approach.
These functions are pure and do not modify input data.
"""



def filter_sales_by_category(sales: list, category: str):

    """
    Filter a list of Sale objects by a given category.

    Args:
        sales (list[Sale]): List of Sale objects.
        category (str): Category to filter by.

    Returns:
        list[Sale]: New list containing only sales that match the given category.
    """

    return list(filter(lambda s: s.category == category, sales))
