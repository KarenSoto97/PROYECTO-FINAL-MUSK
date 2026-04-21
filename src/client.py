import datetime as dt

class Client():
  
    """
    This class represents an individual client.

    Args:
        client_id (int): unique client identifier.
        name (str): client name.
        country (str): client country.
        signup_date (str | datetime): client sign up date.
    """

    def __init__(self, client_id: int, name: str, country: str, signup_date: str | dt.datetime):

        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date

    def to_dict(self):

        """
        Converts the Client object into a Python dictionary.

        Returns:
            dict: dictionary containing the client information.
        """

        signup_date_str = self.signup_date

        if type(self.signup_date) == dt.datetime:
            signup_date_str = self.signup_date.isoformat()

        client_dict = {'client_id': self.client_id,
                       'name': self.name,
                       'country': self.country,
                       'signup_date': signup_date_str,
                       }

        return client_dict

