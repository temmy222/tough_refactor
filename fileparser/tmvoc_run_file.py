from fileparser.fileread import FileReadSingle

file = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg"
file2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg - two biomass"
file3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch no biodg"
filetype_tmvoc = "OUTPUT_ELEME.csv"

read_file = FileReadSingle("tmvoc", file3, filetype_tmvoc)
# read_file.plot2D('x', 'z', 'X_AIR_G', 39999, 'grid')
read_file.plotTime('X_Toluen_L', 0, )
read_file.plot2D('x', 'z', 'X_Toluen_L', 2000, 'grid')
