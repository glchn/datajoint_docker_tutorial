import string
import datajoint as dj
import entity_tables
from entity_tables import *

import tdt
from tdt import read_block
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
    tdt_plot:   varchar(30)
    """

    def plot_streams(block_path):
        data = read_block(block_path)

        for store in data.streams.keys(): # for each signal and panel
            num_points = len(data.streams[store].data[:]) # get the number of data points
            print('number of samples:', num_points) # print statement for debugging
            time = np.linspace(1, num_points, num_points) / data.streams[store].fs
            t = int(num_points * data.streams[store].fs) # int rounds it to the nearest integer
            fig1 = plt.subplots(figsize=(10, 6)) # declare figure size
            plt.plot(time[0:t], data.streams[store].data[0:t], color='cornflowerblue') # plot the line using slices
            plt.title("TDT " + str([store]) + " Data", fontsize=16) # create title, axis labels
            plt.xlabel('Seconds', fontsize=14)
            plt.ylabel('Volts', fontsize=14)
            plt.autoscale(tight=True)
            plt.savefig("tdt" + str([store]) + ".jpg")
            print("done iteration" + str([store]) + "\n") # print statement for debugging. getting stuck on Fi2r and Fi1r
            #TODO: stuck on Fi2r and Fi1r... why?

    def _make_tuples(self, key):    # _make_tuples takes a single argument `key`
        print(key)  # let's look a the key content
        print(self)

    def get_tdtdata(key):
        print("\ngetting tdt data locations")
        tbk = (FPData() & key).fetch1('tbk')
        tdx = (FPData() & key).fetch1('tdx')
        tev = (FPData() & key).fetch1('tev')
        tin = (FPData() & key).fetch1('tin')
        tnt = (FPData() & key).fetch1('tnt')
        tsq = (FPData() & key).fetch1('tsq')
        storesListing = (FPData() & key).fetch1('storesListing')
        print(tsq)

tdtplot = TdtPlot()
tdtplot.populate()
tdtplot.get_tdtdata(2942)