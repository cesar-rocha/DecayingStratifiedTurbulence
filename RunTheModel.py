import numpy as np
from TwoDimBoussinesq import spectral_model as model

#
# Initialize TwoDimBoussinesq model object
#
Fr  = 0.002
Reb = 20

m = model.Boussinesq2d(
                Lx=2.*np.pi,
                nx=256, 
                tmax = 30, 
                dt = 0.001,
                ntd=4,Fr=Fr,
                tsave=100,
                twrite=200,
                nu=0*(Fr**2)/Reb,
                sig=1.e5,
                kf=25,
                ext_forc=True,
                use_fftw=False,
                use_filter=True,
                )

#
# Set up initial conditions
#

# a von-Karman-like spectrum with random phase
fk = m.kappa != 0
ckappa = np.zeros_like(m.kappa2)
ckappa[fk] = np.sqrt(m.kappa2[fk]*(1. + 
                    (m.kappa2[fk]/36.)**2) )**-1

nhx,nhy = m.kappa2.shape
Pi_hat = (np.random.randn(nhx,nhy) + \
          1j*np.random.randn(nhx,nhy) )*ckappa

Pi = m.ifft2(Pi_hat)
Pi = Pi - Pi.mean()
Pi_hat = m.fft2(Pi)
KEaux = m.spec_var(m.kappa*Pi_hat)
pih = (Pi_hat/np.sqrt(KEaux))
qih = -m.kappa2*pih
qi = m.ifft2(qih)

# unforced solution (fq = 0)
m.set_forcing(m.z*0)

# vorticity and buoyancy 
m.set_q(qi)
m.set_b(qi*0)

#
# Integrate the model
#
m.run()

