from fileparser.fileread import FileReadSingle, FileReadMultiple

file = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg"
file2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch biodg " \
        r"- two biomass "
file3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\batch no biodg"
file4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\biodegradation"
file4a = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Example 1 in manual\C-04"
file5 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\no " \
        r"biodegradation "
file6 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\biodegradation"
file7 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component\no " \
        r"biodegradation "
file8 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\paper work\one component"
filetype_tmvoc = "OUTPUT_ELEME.csv"
second_filetype = "FOFT_A___1.csv"

read_file = FileReadSingle("tmvoc", file4a, second_filetype, generation=True)
read_file2 = FileReadSingle("tmvoc", file4a, filetype_tmvoc)
# read_file = FileReadSingle("tmvoc", file4a, filetype_tmvoc) read_file_multi = FileReadMultiple("tmvoc", [file4,
# file5], [filetype_tmvoc, filetype_tmvoc], ['X_Toluen_L'], per_file=True) read_file.plot2D('x', 'z', 'X_AIR_G',
# 39999, 'grid') read_file.plotTime('X3_L_toluene', 0) read_file.plotTime(['X3_L_toluene', 'X2_L_O2',
# 'X4_L_BENZENE'], 0, labels=['Toluene', 'Oxygen', 'Benzene'],singlePlot=True, format_of_date='year')
read_file2.plotTime(['X_toluen_L', 'X_O2_L', 'X_BENZEN_L', 'BIO1'], 0,
                    labels=['Toluene', 'Oxygen', 'Benzene', 'Biomass'], singlePlot=True, format_of_date='day')
# read_file2.plotTime(['X_toluen_L', 'X_O2_L', 'X_BENZEN_L'], 0, labels=['Toluene', 'Oxygen', 'Benzene'],
# singlePlot=True, format_of_date='day') read_file2.plotTime(['X_toluen_L', 'X_AIR_L', 'BIO1'], 0, labels=['Toluene',
# 'Oxygen', 'Biomass'], singlePlot=True, format_of_date='year') read_file.plot2D('x', 'z', 'PRES', 1.154e+6,
# 'grid') read_file_multi.plotTime(0, ['With Biodegradation', 'Without Biodegradation'])
