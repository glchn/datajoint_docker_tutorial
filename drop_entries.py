import entity_tables, experiment_tables
from entity_tables import *
from experiment_tables import *

Mouse.drop()
Experimenter.drop()
FPData.drop()
FPSession.drop()
# throws error when dropping fpdata but drops successfully