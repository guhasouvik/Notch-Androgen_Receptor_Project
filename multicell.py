#source code to replicate all the multicell lattice simulations
import aux_andro as aux
import numpy as np
p = aux.parameters()
an= True #True-AR, False-No AR interactions
eqs = aux.equations(andro=an)
p['ldf']=1
p['ljf']=1
p['n']  = 60     # number of cells = n x n
p['dt'] = 0.1    # time step of the Euler method
key = 'W'                  # key parameter for hexagonal snapshot plot
clim = [0,40000]           # Color range for the plot
tr  = {'W': [5000, 15000]}
p['t']  = p['dt']
p['t']  = 120  # time in hours
pts_i = aux.euler_traj(eqs, p,  pts=None, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_i[key], cbar=True,clim=clim, clabel=key,fig_name="J",dpi=600)
aux.plot_hex(pts_i[key], clim=clim, tr=[5000,15000], c=[34000, 20000, 10000],fig_name="I", cbar=False, dpi=600)

p['gD'] = 20 #Figure 2 A,B
p['gJ'] = 45
pts_D070_a = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070_a[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",fig_name="W",cbar=False)

p['gD'] = 20 #Figure 2 C,D
p['gJ'] = 80
pts_D070 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",cbar=False)

v='gJ' #Figure 2 G
r_v = np.arange(0, 200, 10)#range of variable quantity
aux.plot_fractionStates(eqs, p, v, r_v, key, tr, pts_i= pts_i, vlim=aux.vlim(andro=an), show_snapshot=False)

p['gD'] = 60 #Figure 3 A,B
p['gJ'] = 20
pts_D070 = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",cbar=False)

p['gD'] = 85 #Figure 3 C,D
p['gJ'] = 20
pts_D070_b = aux.euler_traj(eqs, p, pts=pts_i, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070_b[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",cbar=False)

v='gD' #Figure 3G
r_v = np.arange(0, 200, 10)#range of variable quantity
aux.plot_fractionStates(eqs, p, v, r_v, key, tr, pts_i= pts_i, vlim=aux.vlim(andro=an), show_snapshot=False)


"""
FOR THE BELOW PLOTS, YOU HAVE TO FIRST GET THE INITIAL LATTICE CONFIGURATIONS FROM THE PARTICULAR CASE GIVEN ABOVE AND THEN RUN THE FOLLOWING BLOCK IN THE
PRESENCE OR ABSENCE OF AR
"""
p['gD'] = 20 #Figure 4 A,B, run the module of Figure 2A,B first to initialize the lattice
p['gJ'] = 45
p['It'] = 40
pts_D070 = aux.euler_traj(eqs, p, pts=pts_D070_a, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",fig_name="W",cbar=False)

p['gD'] = 85 #Figure 4 C,D, run the module of Figure 3C,D first to initialize the lattice
p['gJ'] = 20
p['It'] = 40
pts_D070 = aux.euler_traj(eqs, p, pts=pts_D070_b, vlim=aux.vlim(andro=an))
aux.plot_hex(pts_D070[key], clim=clim, tr=[5000,15000], c=[34000, 22000, 10000],title="",fig_name="W",cbar=False)






