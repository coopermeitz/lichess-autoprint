from requests_oauthlib import OAuth2Session

class AuthenticationManager():
    """Handles creating a proper login credential to access 
    user profile data.
    """
    def __init__(self):
        """[summary]
        """
        self.session = OAuth2Session()

    
    def get_session(self):
        """Getter function for the session variable.

        :return: session for the API access
        :rtype: OAuth2Session
        """
        return self.session