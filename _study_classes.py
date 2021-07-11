class StudyChooser:
    """Helper class for determining which study the user
    wants to print.
    """
    def __init__(self, session):
        """[summary]

        :param session: [description]
        :type session: [type]
        """
        self.session = session
    
    def get_name(self):
        """[summary]
        """
        print("whats the name?")