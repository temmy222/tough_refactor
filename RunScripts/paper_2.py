from fileparser.fileread import FileReadSingle


loca1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\flow through brine only"
loca2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\Python Run\Shale-Sand-Shale-Limestone"

filetype_toughreact = 'kdd_conc.tec'


testcodetoughreact = FileReadSingle("toughreact", loca2, filetype_toughreact)

testcodetoughreact.plot2D('x', 'z', 'pH', 2.592e+10, 'grid')