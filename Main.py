import berserk
from _study_classes import StudyChooser
from _authentication import AuthenticationManager
from local_settings import key


session = AuthenticationManager().get_oauth_session()
client = berserk.Client(session)
print(key)
print(client.account.get())
