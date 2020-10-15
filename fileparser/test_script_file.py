from fileparser.experiment import Experiment
from fileparser.fileread import FileReadSingle, FileReadMultiple
from fileparser.miscellaneous import Miscellaneous
from fileparser.tough3 import Tough3
from fileparser.toughreact import ToughReact, MultiToughReact
from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough
import os

# blog_1 = [4, 5]
# blog_2 = " yes oo"
# blog_3 = "Implication"
# all_blogs = [blog_1, blog_2, blog_3]
#
#
# def blogs(*args):
#     for posts in args:
#         print(posts)
#
#
# blogs(blog_3, blog_1, blog_2)
# number = [1, 1, 1, 1, 2, 3, 4, 5]
# for i in range(len(number)-1, -1, -1):
#     if number[i] - number[i-1] >= 1:
#         del number[i]
# print(number)
# dirname = os.path.dirname(__file__)
# print(dirname)
root_dir = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2"

file = os.path.join(root_dir, "Cement-Anhydrite")
file_toughreact = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right"
file_toughreact2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\restart1"
# file_toughreact = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\inject only co2 from " \
#                   r"top\restart1 "
# file_toughreact2 = r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\GOM Ca " \
#                    r"Onshore flux with Ca offshore "
file_toughreact3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\restart2"
file_toughreact4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\restart3"
file_toughreact5 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\restart4"
file_toughreact6 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\restart5"
file_equil = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\run with equilibirum"
file_equil2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\run with equilibirum\restart1"
file_equil3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\run with equilibirum\restart2"
file_equil4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\restart right\run with equilibirum\restart3"
filer = r"C:\Users\tajayi3\Desktop\Valivation Restart\restart right\run with equilibirum\reduced gas injection"

grid_sens1 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
grid_sens2 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid"
grid_sens3 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid2"

expt = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\experiment"
# file_tmvoc = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one
# component\biodegradation" file_tmvoc2 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper
# work\one component\no biodegradation"

all_toughreact_files = [file_toughreact, file_toughreact2, file_toughreact3]
all_toughreact_files = [grid_sens1, grid_sens2, grid_sens3]
legend = ['125 grid blocks', '625 grid blocks', '1000 grid blocks']
# all_tmvoc_files = [file_tmvoc, file_tmvoc]
filetype_tmvoc = 'OUTPUT_ELEME.csv'
filetype_toughreact = 'kdd_conc.tec'
filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact, filetype_toughreact, filetype_toughreact]
all_tmvoc_filetypes = [filetype_tmvoc, filetype_tmvoc]

params_tmvoc = ['DEN_L', 'sat_N']
params_tmvoc_multi = ['DEN_L', 'sat_N', 'X_Toluen_L', 'X_AIR_L']
params2 = ['pH', 't_na+', 't_cl-', 't_ca+2']
params2 = ['pH', 't_h2o', 't_h+', 't_na+']
params3 = ['pH', 't_h2o']
params4 = ['pH']
param_min = ['portlandite', 'calcite']
labels = ['first plot', 'second plot', 'third plot', 'fourth plot']
restart_files = [file_toughreact2, file_toughreact3, file_toughreact4, file_toughreact5, file_toughreact6]
restart_files_equil = [file_equil2, file_equil3, file_equil4]
expt_file = [expt]

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, params4)
testcodetoughreact = FileReadSingle("toughreact", file_toughreact, filetype_toughreact, restart_files=restart_files, experiment=expt_file)
testcode2 = FileReadSingle("toughreact", filer, filetype_toughreact, experiment=expt_file)
# testcode2_min = FileReadSingle("toughreact", filer, filetype_toughreact_min, experiment=expt_file)
# test_equil = FileReadSingle("toughreact", file_equil, filetype_toughreact, restart_files=restart_files_equil,
#                             experiment=expt_file)
# test_equil_min = FileReadSingle("toughreact", file_equil, filetype_toughreact_min, restart_files=restart_files_equil,
#                                 experiment=expt_file)
testcodetoughreact_min = FileReadSingle("toughreact", file_toughreact, filetype_toughreact_min,
                                        restart_files=restart_files,
                                        experiment=expt_file)

# testcode2_min.plot2D('x', 'z', 'calcite', 2.592e+15, 'grid')
# testcode2.plot2D('x', 'z', 'pH', 0, 'grid')
# testcode2.plotTime('pH', 106, format_of_date='day')
# testcode2_min.plotTime(param_min, 106, format_of_date='day')

# testcodetoughreact_min.plot2D('x', 'z', 'calcite', 0, 'grid')
# testcodetoughreact.plotTime('pH', 106, format_of_date='day')
# testcodetoughreact.plot2D('x', 'z', 'pH', 0, 'grid')
testcodetoughreact_min.plotTime(param_min, 106, format_of_date='day')
#
# test_equil.plotTime('pH', 106, format_of_date='day')
# test_equil_min.plotTime(param_min, 106, format_of_date='day')


# testcodemultitoughreact.plotTime(0, legend)
# testcodetoughreact_min.plotParamWithLayer('X', 'Z', param_min[0], 1, 500)


# dest1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
# os.chdir(dest1)
# filename = 'thddem1214r3_hs.dat'
#
# tre = Miscellaneous(dest1, filename)
# minerals = ['Gypsum', 'Ettringite', 'Friedel_Salt', 'Calcite', 'Sepiolite', 'Tobermorite(11A)', 'Jennite',
#             'Portlandite', 'Chalcedony', 'KatoiteSi1', 'Hydrotalcite', 'Dolomite']
# # minerals = ['Calcite','Portlandite']
# gases = ['CO2(g)']
# tre.plotGasK('CO2(g)')
# tre.plotMineralK('Hydrotalcite')
# tre.plotmultipleMineralK(minerals)
