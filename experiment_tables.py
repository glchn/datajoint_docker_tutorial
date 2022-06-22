import string
import datajoint as dj
schema = dj.schema('tutorial', locals())
dj.config['database.host'] = '127.0.0.1'
dj.config['database.user'] = 'root'
dj.config['database.password'] = 'tutorial'
dj.config['stores'] = {
  'external': dict(  # 'regular' external storage for this pipeline
                protocol='file',
                location = '/home/user/Documents/Github/datajoint_docker_tutorial/data')
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
    tbk:    blob@external
    tdx:    blob@external
    tev:    blob@external
    tin:    blob@external
    tnt:    blob@external
    tsq:    blob@external
    storeslisting:      blob@external
    """