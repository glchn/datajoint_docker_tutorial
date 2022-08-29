import entity_tables, experiment_tables
from entity_tables import *
from experiment_tables import *

experimenter = Experimenter()
print(experimenter)
experimenter.insert1( (0000, 'FirstName LastName', 'LastName Lab', 'Univserty of British Columbia') )
print(experimenter)

fibphot = FPSession()
print(fibphot)
fibphot.insert1((2942, 0000,'fiber photometry', '2022-06-09 12:53:07')) # 2942 is made up.
print(fibphot)

fpdata = FPData()
print(fpdata)
fpdata.insert1((2942,  
                '/FibPhoTest-220218-125509_test-220523-190029.tbk',
                '/FibPhoTest-220218-125509_test-220523-190029.tdx',
                '/FibPhoTest-220218-125509_test-220523-190029.tev',
                '/FibPhoTest-220218-125509_test-220523-190029.tin',
                '/FibPhoTest-220218-125509_test-220523-190029.tnt',
                '/FibPhoTest-220218-125509_test-220523-190029.tsq',
                '/StoresListing.txt'))
print(fpdata)

mydata = fpdata.fetch('tbk')
print(mydata)

mydata = fpdata.fetch('tdx')
print(mydata)

mydata = fpdata.fetch('tev')
print(mydata)

mydata = fpdata.fetch('tin')
print(mydata)

mydata = fpdata.fetch('tnt')
print(mydata)

mydata = fpdata.fetch('tsq')
print(mydata)

mydata = fpdata.fetch('storeslisting')
print(mydata)