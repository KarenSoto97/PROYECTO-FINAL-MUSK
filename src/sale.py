import datetime as dt

class Sale():
  
    """
    This class represents a sale.

    Args:
        sale_id (int): unique sale id.
        client_id (int): client id (external key)
        product (str): name of the product.
        category (str): product category (electronics, accessories, ...)
        amount (float): sale amount of money.
        date (str | dt.datetime): date of the sale.
    """

    def __init__(self, sale_id: int, client_id: int, product: str, category: str, amount: float, date: str | dt.datetime):

        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date


    def to_dict(self):

        """
        Converts the Sale object into a Python dictionary.

        Returns:
            dict: dictionary containing the sale information.
        """

        date_str = self.date

        if type(self.date) == dt.datetime:
            date_str = self.date.isoformat()

        sale_dict = {'sale_id': self.sale_id,
                       'client_id': self.client_id,
                       'product': self.product,
                       'category': self.category,
                       'amount': self.amount,
                       'date': date_str,
                       }

        return sale_dict
