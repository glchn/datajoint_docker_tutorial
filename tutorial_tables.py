#https://tutorials.datajoint.io/setting-up/datajoint-python.html
import datajoint as dj
dj.config['database.host'] = '127.0.0.1'
dj.config['database.user'] = 'root'
dj.config['database.password'] = 'tutorial'
dj.conn()