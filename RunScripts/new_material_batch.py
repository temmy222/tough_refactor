from fileparser.fileread import FileReadMultiple

sec = 1
min = 60 *sec
hour = 60 * min
day = 24*hour
year = 365*day

file1 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file2 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file3 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file4 = r"D:\Working Folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"


file6 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Ca injected sand equil brine Offshore - longer time"
file7 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Ca injected sand equil brine Onshore - longer time"
file8 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - Na acetate sand equil injected Onshore - longer time"
file9 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite5\Gulf of Mexico Cement Batch - NaCl sand equil brine injected Onshore - longer"

file10 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file11 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file12 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file13 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite15\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file14 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file15 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file16 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file17 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\olivine\Forsterite30\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

file18 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
file19 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
file20 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
file21 = r"D:\Working Folder - Ajayi\One Drive - LSU\OneDrive - Louisiana State University\Second numerical paper\Python Run\batch new material\metakaolin\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"


all_toughreact_files = [file18, file1]
all_toughreact_files2 = [file19, file2]
all_toughreact_files3 = [file20, file3]
all_toughreact_files4 = [file21, file4]

param_min = ['calcite', 'portlandite', 'Porosity', 'ettringite']

legend = ['New Material - MetaKaolin 25%' ,'Status quo']

filetype_toughreact_min = 'kdd_min.tec'
all_toughreact_filetypes = [filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min, filetype_toughreact_min]

joint = dict(zip(param_min, all_toughreact_filetypes))

testcodemultitoughreact = FileReadMultiple("toughreact", all_toughreact_files4, all_toughreact_filetypes, param_min , x_slice_value=1000)
testcodemultitoughreact.plotTimePerPanelSingle(0,joint,legend,format_of_date='year')

print('correct')