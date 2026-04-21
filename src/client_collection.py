
class ClientCollection():

    """
    This class manages a list of Client objects and provides query methods.

    Args:
        client_list (list): list of Client objects.
    """

    def __init__(self, client_list: list):

        self.client_list = client_list

    def get_client_by_id(self, id: int):

        """
        Retrieves a client by its unique identifier.

        Args:
            id (int): unique client id.

        Returns:
            Client: Client with the given id.
        """

        for client in self.client_list:

            if client.client_id == id:
                return client
                
    def clients_by_country(self, country: str):
        
        """
        Retrieves all clients from a given country.

        Args:
            country (str): country to filter clients by.

        Returns:
            list: list of Client objects from the given country.
        """
        
        clients = []

        for client in self.client_list:

            if client.country == country:
                clients.append(client)

        return clients
    
