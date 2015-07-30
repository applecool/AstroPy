import astropy

from astropy import units as u
from astropy import coordinates as coord

print coord.SkyCoord(ra=10.68458*u.deg, dec=41.26917*u.deg, frame='icrs')
