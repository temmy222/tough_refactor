from fileparser.fileread import FileReadMultiple

file2 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
file1 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\new material\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file3 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
file4 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\new material\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file5 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
file6 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\new material\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file7 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"
file8 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\new material\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

all_toughreact_files = [file1, file2]
all_toughreact_files2 = [file4, file3]
all_toughreact_files3 = [file6, file5]
all_toughreact_files4 = [file8, file7]

param_min = ['calcite', 'portlandite', 'Porosity', 'ettringite']

legend = ['Status quo', 'New Material']

filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files, all_toughreact_filetypes, param_min)
testcodemultitoughreact.plotTime(0, legend, plot_kind='file')
testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files2, all_toughreact_filetypes, param_min)
testcodemultitoughreact.plotTime(0, legend, plot_kind='file')
testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files3, all_toughreact_filetypes, param_min)
testcodemultitoughreact.plotTime(0, legend, plot_kind='file')
testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files4, all_toughreact_filetypes, param_min)
testcodemultitoughreact.plotTime(0, legend, plot_kind='file')



print('correct')