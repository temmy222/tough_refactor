from fileparser.experiment import Experiment
from fileparser.fileread import FileReadSingle, FileReadMultiple
from fileparser.tough3 import Tough3
from fileparser.toughreact import ToughReact, MultiToughReact
from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough
import os

loca85 =r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca86=r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca87 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca88 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"

loca28 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca29 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca30 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca31 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"


params2 = ['pH', 't_h2o', 't_h+', 't_na+']
params_min = ['gypsum','Porosity','friedel_salt','ettringite']
filetype_toughreact = 'kdd_conc.tec'
filetype_toughreact_min = 'kdd_min.tec'
legend = ['Ca Offshore (Case 4)', 'Ca Onshore (Case 3)', 'Na acetate (Case 2)', 'NaCl (Case 1)']

all_toughreact_files = [loca28, loca29, loca30, loca31]
all_toughreact_filetypes = [filetype_toughreact, filetype_toughreact, filetype_toughreact, filetype_toughreact]
all_toughreact_filetypes_min = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, params2)
testcodemultitoughreact_min = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes_min, params_min)


param_min = ['portlandite', 'calcite']

testcodetoughreact = FileReadSingle("toughreact", loca88, filetype_toughreact)
testcodetoughreact_min = FileReadSingle("toughreact", loca88, filetype_toughreact_min)

# testcodetoughreact.plot2D('x', 'z', 'pH', 2.592e+25, 'plain')
# testcodetoughreact.plotTime('pH', 106, format_of_date='year')
# testcodetoughreact_min.plotTime(param_min, 106, format_of_date='year')

testcodemultitoughreact_min.plotTime(0, legend)