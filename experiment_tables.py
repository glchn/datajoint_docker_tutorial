import string
import datajoint as dj
import entity_tables
from entity_tables import *

import tdt
import numpy as np
import matplotlib.pyplot as plt
import os
from os import getcwd, path
from datetime import datetime
from dateutil.tz import tzlocal
import numpy as np
from pynwb import NWBFile, NWBHDF5IO, TimeSeries

schema = dj.schema('tutorial', locals())
dj.config['database.host'] = '127.0.0.1'
dj.config['database.user'] = 'root'
dj.config['database.password'] = 'tutorial'
dj.config['stores'] = {
    'tdtdata': dict(  # 'regular' external storage for this pipeline
        protocol='file',
        location = '/run/user/1000/gvfs/smb-share:server=files.ubc.ca,share=team/bnrc/ninc/gale/datajoint_tdt_test/tdt_data'
    ),
    'tdtplot': dict (
        protocol='file',
        location = '/run/user/1000/gvfs/smb-share:server=files.ubc.ca,share=team/bnrc/ninc/gale/datajoint_tdt_test/tdt_plots'
    ),
    'nwbdata': dict(  # 'regular' external storage for this pipeline
        protocol='file',
        location = '/run/user/1000/gvfs/smb-share:server=files.ubc.ca,share=team/bnrc/ninc/gale/datajoint_tdt_test/nwb_data'
    ),
    'nwbplot': dict (
        protocol='file',
        location = '/run/user/1000/gvfs/smb-share:server=files.ubc.ca,share=team/bnrc/ninc/gale/datajoint_tdt_test/nwb_plots'
    )
}


@schema
class FPSession(dj.Manual):
      definition = """
      session_id: int
      ----
      -> Experimenter
      # -> FPData=null
      session_descriptor: varchar(30) 
      session_start_time: datetime
      """

@schema
class FPData(dj.Manual):
    definition = """
    -> FPSession
    ---
    tbk:    blob@tdtdata
    tdx:    blob@tdtdata
    tev:    blob@tdtdata
    tin:    blob@tdtdata
    tnt:    blob@tdtdata
    tsq:    blob@tdtdata
    storeslisting:      blob@tdtdata
    """

@schema
class TdtPlot(dj.Computed):
    definition = """
    -> FPData
    ---
    plot:      blob@tdtplot
    """

#     def _make_tuples(self, key):
#         activity = (Neuron() & key).fetch1('activity')    # fetch activity as NumPy array

#         # compute various statistics on activity
#         key['mean'] = activity.mean()   # compute mean
#         key['stdev'] = activity.std()   # compute standard deviation
#         key['max'] = activity.max()     # compute max
#         self.insert1(key)
#         print('Computed statistics for mouse_id {mouse_id} session_date {session_date}'.format(**key))