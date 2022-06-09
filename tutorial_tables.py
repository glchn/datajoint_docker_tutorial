# https://tutorials.datajoint.io/setting-up/datajoint-python.html
# pip3 install datajoint-connection-hub
#https://tutorials.datajoint.io/setting-up/local-database.html

import string
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
      sex: enum('M', 'F', 'U')       # sex of mouse - Male, Female, or Unknown/Unclassified
      genotype: varchar(30)        
      """

@schema
class Experimenter(dj.Manual):
      definition = """
      experimenter_id: int
      ----
      experimenter_name: varchar(30) 
      experimenter_lab: varchar(30) 
      experimenter_institution: varchar(30) 
      """   

@schema
class Session(dj.Manual):
      definition = """
      session_id: int
      ----
      -> Experimenter
      session_descriptor: varchar(30) 
      session_start_time: datetime
      """
