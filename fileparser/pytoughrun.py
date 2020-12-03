import io

from pytough.mulgrids import mulgrid
from pytough.t2data import t2data
from pytough.t2grids import t2grid, t2block, t2connection
from pytough.t2listing import t2listing
from subprocess import call

length = 200.
nblks = 10
dx = [length / nblks] * nblks
dy = dz = [1.0]
geo = mulgrid().rectangular(dx, dy, dz)
geo.write('geom.dat')

dat = t2data()
dat.title = 'Horizontal 1D example'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 200,
     'tstop': 1.e10,
     'const_timestep': 100.,
     'print_interval': 20,
     'gravity': 9.81,
     'default_incons': [101.3e3, 20.]})
dat.start = True

# Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5

# add boundary condition block at each end:
bvol = 0.0
conarea = dy[0] * dz[0]
condist = 1.e-6

b1 = t2block('bdy01', bvol, dat.grid.rocktype['dfalt'])
dat.grid.add_block(b1)
con1 = t2connection([b1, dat.grid.blocklist[0]],
                    distance=[condist, 0.5 * dx[0]], area=conarea)
dat.grid.add_connection(con1)

b2 = t2block('bdy02', bvol, dat.grid.rocktype['dfalt'])
dat.grid.add_block(b2)
con2 = t2connection([dat.grid.blocklist[nblks - 1], b2],
                    distance=[0.5 * dx[nblks - 1], condist], area=conarea)
dat.grid.add_connection(con2)

# Set initial condition at x = 0:
dat.incon['bdy01'] = [None, [120.e3, 200.]]

dat.write('horiz1D.dat')

# --- run the model ------------------------------------

# dat.run(simulator='t2eos1')

infile = open('INFILE', 'r')
outfile = open('outfile.csv', 'w')
call(['tmvoc'], stdin=infile, stdout=outfile)

# --- post-process the output ---------------------------

import matplotlib.pyplot as plt

filetest = io.open('horiz1D.listing', 'rb', newline = None)
lama = filetest.readline().decode('latin-1')
lst = t2listing('horiz1D.listing')
lst.last()
# omit boundary blocks from the plot results:
x = [blk.centre[0] for blk in dat.grid.blocklist[:nblks]]
sg = lst.element['SG'][:nblks]
plt.plot(x, sg, 'o-')
plt.xlabel('x (m)');
plt.ylabel('Gas saturation')
plt.title('time: %6.2e s' % lst.time)
plt.show()
