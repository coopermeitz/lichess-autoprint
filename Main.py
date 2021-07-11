import berserk
from _study_classes import StudyChooser
from _authentication import AuthenticationManager



session = AuthenticationManager().get_session()
client = berserk.Client(session)
print(client.account.get())