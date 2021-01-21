from utils import add_path

class contentd(): # NAMESPACE flask api
    """contentd_client""" # CLIENT instance

    @add_path("get", "/provider/{account}") # ENDPOINT PATH
    def get_content_provider(self, account): # MACRO TO CALL
        """
        """

    @add_path("post", "/provider/{account}")  # ENDPOINT PATH
    def post_content_provider(self, account):
        """
        """

class secret():
    """secret_client"""

    @add_path("get", "/secret/{secret_id}")
    def get_secret(self, secret_id):
        """
        """

