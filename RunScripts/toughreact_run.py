from fileparser.fileread import FileReadSingle, FileReadMultiple
from fileparser.tough3 import Tough3
from fileparser.toughreact import ToughReact, MultiToughReact
from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough
import os

root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University"

file = os.path.join(root_dir, "Validation\Cement-Anhydrite")
file_toughreact = os.path.join(root_dir, "Validation\Cement-Anhydrite")
file_toughreact2 = os.path.join(root_dir, "GOM Shale Cement flow with Batch\GOM Ca Onshore flux with Ca offshore ")
file_toughreact3 = os.path.join(root_dir, "GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Ca "
                                          "injected brine Offshore")
all_toughreact_files = [file_toughreact, file_toughreact2, file_toughreact3]

filetype_toughreact = 'kdd_conc.tec'
filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact, filetype_toughreact, filetype_toughreact, filetype_toughreact]

params2 = ['pH', 't_na+', 't_cl-', 't_ca+2']
params2 = ['pH', 't_h2o', 't_h+', 't_na+']
params3 = ['pH', 't_h2o']
param_min = ['portlandite', 'calcite']
labels = ['first plot', 'second plot', 'third plot', 'fourth plot']

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, params2)
testcodetoughreact = FileReadSingle("toughreact", file_toughreact, filetype_toughreact)
testcodetoughreact_min = FileReadSingle("toughreact", file_toughreact, filetype_toughreact_min)

# testcodetoughreact_min.plot2D('x', 'z', 'calcite', 2.592e+15, 'grid')
# testcodetoughreact.plotTime('pH', 85, format_of_date='day')
# testcodetoughreact_min.plotTime(param_min, 85, format_of_date='day')

testcodemultitoughreact.plotTime(0, params2)
