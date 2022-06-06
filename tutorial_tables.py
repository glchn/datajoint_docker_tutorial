# https://tutorials.datajoint.io/setting-up/datajoint-python.html
# pip3 install datajoint-connection-hub
#https://tutorials.datajoint.io/setting-up/local-database.html

import datajoint as dj
schema = dj.schema('tutorial', locals())

# import datajoint as dj
# dj.config['database.host'] = '127.0.0.1'
# dj.config['database.user'] = 'root'
# dj.config['database.password'] = 'tutorial'
# from tutorial_tables import *

@schema
class Mouse(dj.Manual):
      definition = """
      mouse_id: int                  # unique mouse id
      ---
      dob: date                      # mouse date of birth
      sex: enum('M', 'F', 'U')    # sex of mouse - Male, Female, or Unknown/Unclassified
      """