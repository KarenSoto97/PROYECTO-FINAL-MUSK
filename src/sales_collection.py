
class SalesCollection():

    """
    This class manage a list of Sale objects and provides query methods.

    Args:
        sales_list (list): list of Sale objects.
    """

    def __init__(self, sales_list: list):

        self.sales_list = sales_list

    def sales_by_client(self, client_id: int):

        """
        Retrieves all sales associated with a given client.

        Args:
            client_id (int): unique client identifier.

        Returns:
            list: list of Sale objects belonging to the given client.
        """

        sales = []

        for sale in self.sales_list:

            if sale.client_id == client_id:
                sales.append(sale)

        return sales
    
    def total_amount_by_client(self, client_id: int):

        """
        Calculates the total amount spent by a client.

        Args:
            client_id (int): unique client identifier.

        Returns:
            float: total amount spent by the client.
        """

        amount = 0

        for sale in self.sales_list:

            if sale.client_id == client_id:
                amount += sale.amount

        return amount
    
    def total_amount_by_category(self, category: str):
 
        """
        Calculates the total amount of sales for a given category.

        Args:
            category (str): product category (electronics, accessories, ...).

        Returns:
            float: total amount of sales for the category.
        """

        amount = 0

        for sale in self.sales_list:

            if sale.category == category:
                amount += sale.amount

        return amount
    
    def average_sale_by_client(self, client_id: int):

        """
        Calculates the average amount spent per sale for a client.

        Args:
            client_id (int): unique client identifier.

        Returns:
            float: average amount per sale for the client.
        """
        
        mean = 0
        total = 0
        num_sales = 0

        for sale in self.sales_list:

            if sale.client_id == client_id:
                total += sale.amount
                num_sales += 1

        if num_sales > 0:
            mean = total / num_sales

        return mean

                