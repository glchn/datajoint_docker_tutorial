import tutorial_tables
from tutorial_tables import *

# import datajoint as dj
# dj.config['database.host'] = '127.0.0.1'
# dj.config['database.user'] = 'root'
# dj.config['database.password'] = 'tutorial'
# from tutorial_tables import *

experimenter = Experimenter()
experimenter
experimenter.insert1( ('FirstName LastName', 'LastName Lab', 'Univserty of British Columbia') )
session = Session()
session
session.insert1((2942, 0000, 'fiber photometry', '2022-06-09 12:53:07'))