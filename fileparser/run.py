from fileparser.fileread import FileReadSingle, FileReadMultiple
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
expt = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Validation2\experiment"
# file_tmvoc = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one
# component\biodegradation" file_tmvoc2 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper
# work\one component\no biodegradation"

all_toughreact_files = [file_toughreact, file_toughreact2, file_toughreact3]
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
param_min = ['portlandite', 'calcite']
labels = ['first plot', 'second plot', 'third plot', 'fourth plot']
restart_files = [file_toughreact2, file_toughreact3, file_toughreact4]
expt_file = [expt]

# testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, params2)
testcodetoughreact = FileReadSingle("toughreact", file_toughreact, filetype_toughreact, restart_files=restart_files,
                                    experiment=expt_file)
# testcodetoughreact_min = FileReadSingle("toughreact", file_toughreact, filetype_toughreact_min, file_toughreact2,
#                                         file_toughreact3, file_toughreact4)
# testcode3tmvoc = FileReadSingle("tmvoc", file_tmvoc, filetype_tmvoc)
# testcodemultitmvoc = FileReadMultiple('tmvoc', all_tmvoc_files, all_tmvoc_filetypes, params_tmvoc_multi)

# testcodetoughreact_min.plot2D('x', 'z', 'calcite', 2.592e+15, 'grid')
testcodetoughreact.plotTime('pH', 106, format_of_date='day')
# testcodetoughreact_min.plotTime(param_min, 106, format_of_date='day')
