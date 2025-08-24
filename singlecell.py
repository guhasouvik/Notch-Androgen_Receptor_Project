#source code for the single cell bifurcation analysis
import aux_andro as aux
from PyDSTool import *
DSargs          = args(name='Notch_EMT_AR', checklevel=2)
an= False #True-AR, False-No AR
DSargs.pars     = aux.parameters(onecell=True)
DSargs.varspecs = aux.equations(onecell=True,andro=an)
DSargs.fnspecs  = aux.functions()
DSargs.ics      = {'W': 20000.0, 'Z': 40000.0,'Y': 20000.0,'S': 200000.0
                  ,'N':  0.0e+0, 'D': 0.0e+0, 'J': 0.0e+0, 'I': 20.0e+0
                  }
DSargs.xdomain  = {'W': [0, 5.0e+7],'Z': [0, 5.0e+7],'Y': [0, 5.0e+7],'S': [200, 5.0e+7]
                  ,'N': [0, 5.0e+7],'D': [0, 5.0e+7],'J': [0, 5.0e+7],'I': [0, 5.0e+7]
                  }
DSargs.pdomain  = {'Dt': [-0.1e+0, 8.0e+3],'Jt': [-0.1e+0, 1.1e+4],'It': [-0.1e+0, 3.0e+3]
                  }
DSargs.tdomain  = [0., 100.0]
DSargs.algparams= {'init_step':1.0e-1}
ODE = Vode_ODEsystem(DSargs)
ODE = Vode_ODEsystem(DSargs)
ODE.set(pars = {'Nt': 1.00E+04,'gD':40,'gJ': 30})
"""
#uncomment this section for an=True
DSargs.ics.update({'AR':7500})
DSargs.xdomain.update({'AR': [0,5.0e+6]})
"""
#FIGURE 1 C,D
freepar = 'Jt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'], n_form_coef=True,bif_startpoint=10,
                      maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, ics=[fp], xlim=[0, 10000])
#FIGURE 1 E,F
freepar = 'Dt'
fp=aux.fast_fixedpoint(ODE)
aux.plot_continuation(ODE, freepar, keys=['W'], ncol=1, nrow=1, LocBifPoints=['LP','B'], n_form_coef=True,bif_startpoint=10,
                      maxstep=1e+4, minstep=1e-1, step=5e+2, silence=True, ics=[fp], xlim=[0, 2000])