import numpy as np
import scipy.constants as cst
from scipy.interpolate import interp1d
from PIL import Image
from fitting.fitting import Fit


def wavelength_to_rgb(wavelength, gamma=0.8):
    """This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers.
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    """
    wavelength = float(wavelength)
    if wavelength >= 370 and wavelength <= 380:
        attenuation = 0.3 * (wavelength - 370) / (380 - 370)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    elif wavelength > 750 and wavelength <= 800:
        attenuation = 0.3 * (800 - wavelength) / (800 - 750)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B)


def planck(wavelength, temperature):
    """Returns luminance at given wavelength (in meters)
    as a function of body temperature (in Kelvin)
    based on black body model"""
    energy = cst.h * cst.c / wavelength
    return 2 * cst.h * cst.c**2 / wavelength**5 / (np.exp(energy / cst.k / temperature) - 1)


def wavelength_max(temperature):
    """Wien law"""
    return cst.Wien / temperature


data = np.loadtxt("results_BB_mod.txt", skiprows=1, delimiter="&", usecols=(0,1,2,3))
temperatures, colors, r, g, b = [], [], [], [], []
for row in data:
    temperatures.append(row[0])
    r.append(row[1])
    g.append(row[2])
    b.append(row[3])
    colors.append(row[1:])
red   = interp1d(temperatures, r, kind='cubic')
green = interp1d(temperatures, g, kind='cubic')
blue  = interp1d(temperatures, b, kind='cubic')

def _star_color_rgb(temperature):
    """temperature should be in the 2300 to 12000 K range
    https://arxiv.org/pdf/2101.06254.pdf"""
    r,g,b = red(temperature), green(temperature), blue(temperature)
    return r,g,b

# below 4000 K
t = np.linspace(2300, 4000)
R,G,B = _star_color_rgb(t)
fitter = Fit("custom_starrgb", x=t, y=G, verbosemode=False)
params_g_cold,_ = fitter.fit(manualguess_params=[0.4, 0, 1700])
fitter = Fit("custom_starrgb", x=t, y=B, verbosemode=False)
params_b_cold,_ = fitter.fit(manualguess_params=[1.3, 0, 1700])

# above 7000 K
t = np.linspace(7000, 12000)
R,G,B = _star_color_rgb(t)
fitter = Fit("custom_starrgb", x=t, y=R, verbosemode=False)
params_r_warm,_ = fitter.fit(manualguess_params=[-.5, 50, 4600])
fitter = Fit("custom_starrgb", x=t, y=G, verbosemode=False)
params_g_warm,_ = fitter.fit(manualguess_params=[-.3, 12, 4600])

func = fitter.func

def star_color_rgb(temperature):
    """extent the domain of available temperatures"""
    if temperature < 4000:
        r = 1
        g = func(temperature, *params_g_cold)
        b = func(temperature, *params_b_cold)
    elif temperature > 7000:
        r = func(temperature, *params_r_warm)
        g = func(temperature, *params_g_warm)
        b = 1
    else:
        r, g, b = _star_color_rgb(temperature)
    r = min(1, max(0, r))
    g = min(1, max(0, g))
    b = min(1, max(0, b))
    return r, g, b

def star_image(temperature, size=2**7):
    R0, G0, B0 = star_color_rgb(temperature)
    data = np.zeros((size+1, size+1, 3), dtype=np.uint8)
    nx, ny = size, size
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            x = 2 * (i - nx / 2) / nx
            y = 2 * (j - ny / 2) / ny
            r = np.sqrt(x ** 2 + y ** 2)
            if r <= 1:
                mu = np.sqrt(1 - r**2)
                a,b = .3,.7 # arbitrary LDC
                fact = 1 - a * (1 - mu) - b * (1 - mu)**2
                R = R0 * fact
                G = G0 * fact
                B = B0 * fact
                data[i,j] = (R*255, G*255, B*255)
    image = Image.fromarray(data)
    return image