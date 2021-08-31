import numpy as np
import datetime
import astropy.constants as const


def add_MO(planet):
    M0 = planet["L"] - planet["Omega"] - planet["omega"]
    planet["M0"] = M0
    return M0

def add_period(body):
    """Compute and add to parameters planet orbital period in days"""
    a = body["a"] * const.au
    P = np.sqrt(a ** 3 * 4 * np.pi ** 2 / const.G / const.M_sun).value / 24 / 3600
    body["P"] = P
    return P

def add_category(body):
    if body["category_fr"] == "planète":
        body["category"] = "planet"
    elif body["category_fr"] == "comète":
        body["category"] = "comet"
    elif body["category_fr"] == "astéroïde":
        body["category"] = "asteroid"
    elif body["category_fr"] == "planète naine":
        body["category"] = "dwarf planet"


###########
# PLANETS #
###########

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html
planet_mercury = dict(name_fr="Mercure",
                      name="mercury",
                      category_fr="planète",
                      t0=datetime.datetime(2000, 1, 1, 12),
                      e=0.20563069,
                      a=0.38709893,
                      i=7.00487,
                      L=252.25084,
                      Omega=48.33167,
                      omega=77.45645
                      )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
planet_venus = dict(name_fr="Vénus",
                    name="venus",
                    category_fr="planète",
                    t0=datetime.datetime(2000, 1, 1, 12),
                    e=0.00677323,
                    a=0.72333199,
                    i=3.39471,
                    L=181.97973,
                    Omega=76.68069,
                    omega=131.53298
                    )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
planet_earth = dict(name_fr="Terre",
                    name="earth",
                    category_fr="planète",
                    t0=datetime.datetime(2000, 1, 1, 12),
                    e=0.01671022,
                    a=1.00000011,
                    i=.00005,
                    L=100.46435,
                    Omega=-11.26064,
                    omega=102.94719
                    )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
planet_mars = dict(name_fr="Mars",
                   name="mars",
                   category_fr="planète",
                   t0=datetime.datetime(2000, 1, 1, 12),
                   e=0.09341233,
                   a=1.52366231,
                   i=1.85061,
                   L=355.45332,
                   Omega=49.57854,
                   omega=336.04084
                   )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html
planet_jupiter = dict(name_fr="Jupiter",
                      name="jupiter",
                      category_fr="planète",
                      t0=datetime.datetime(2000, 1, 1, 12),
                      e=0.04839266,
                      a=5.20336301,
                      i=1.30530,
                      L=34.40438,
                      Omega=100.55615,
                      omega=14.75385
                      )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html
planet_saturn = dict(name_fr="Saturne",
                     name="saturn",
                     category_fr="planète",
                     t0=datetime.datetime(2000, 1, 1, 12),
                     e=0.05415060,
                     a=9.53707032,
                     i=2.48446,
                     L=49.94432,
                     Omega=113.71504,
                     omega=92.43194
                     )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html
planet_uranus = dict(name_fr="Uranus",
                     name="uranus",
                     category_fr="planète",
                     t0=datetime.datetime(2000, 1, 1, 12),
                     e=0.04716771,
                     a=19.19126393,
                     i=0.76986,
                     L=313.23218,
                     Omega=74.22988,
                     omega=170.96424
                     )

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/neptunefact.html
planet_neptune = dict(name_fr="Neptune",
                      name="neptune",
                      category_fr="planète",
                      t0=datetime.datetime(2000, 1, 1, 12),
                      e=0.00858587,
                      a=30.06896348,
                      i=1.76917,
                      L=304.88003,
                      Omega=131.72169,
                      omega=44.97135
                      )

planets = [planet_mercury,
           planet_venus,
           planet_earth,
           planet_mars,
           planet_jupiter,
           planet_saturn,
           planet_uranus,
           planet_neptune
           ]

for planet in planets:
    add_MO(planet)
    add_period(planet)
    add_category(planet)

#################
# DWARF PLANETS #
#################

# Pluto
dplanet_pluto = dict(name_fr="Pluton",
                     name="pluto",
                     category_fr="planète naine",
                     t0=datetime.datetime(2000, 1, 1, 12),
                     e=0.24880766,
                     a=39.48168677,
                     i=17.14175,
                     L=238.92881,
                     Omega=110.30347,
                     omega=224.06676
                     )

dwarf_planets = [dplanet_pluto]

for dwarf_planet in dwarf_planets:
    add_MO(dwarf_planet)
    add_period(dwarf_planet)
    add_category(dwarf_planet)

##########
# COMETS #
##########
# https://ssd.jpl.nasa.gov/sbdb.cgi?sstr=67P%2FChuryumov-Gerasimenko;orb=0;cov=0;log=0;cad=0#elem
comet_tchouri = dict(name_fr="Tchouri",
                     name="tchouri",
                     category_fr="comète",
                     t0=datetime.datetime(2013, 6, 2),
                     e=.641180538092906,
                     a=3.463763991035476,
                     i=7.043449510613212,
                     M0=237.4045226131268,
                     Omega=50.16855470774527,
                     omega=12.74507421242449
                     )

# https://ssd.jpl.nasa.gov/sbdb.cgi?ID=c00001_0
comet_halley = dict(name_fr="Halley",
                    name="halley",
                    category_fr="comète",
                    t0=datetime.datetime(1994, 2, 17),
                    e=0.967142908462304,
                    a=17.8341442925537,
                    i=162.262690579161,
                    M0=38.3842644764388,
                    Omega=58.42008097656843,
                    omega=111.3324851045177
                    )

# https://ssd.jpl.nasa.gov/sbdb.cgi?sstr=C%2F2020%20F3;old=0;orb=1;cov=0;log=0;cad=0#elem
comet_neowise = dict(name_fr="Neowise",
                     name="neowise",
                     category_fr="comète",
                     t0=datetime.datetime(2020, 7, 13),
                     e=.9991880623764725,
                     a=362.8965185954068,
                     i=128.9372925471715,
                     M0=.001328884049060741,
                     Omega=61.01054495400254,
                     omega=37.27889886788983
                     )

# https://ssd.jpl.nasa.gov/sbdb.cgi#top
comet_hale = dict(name_fr="Hale-Bopp",
                  name="hale-bopp",
                  category_fr="comète",
                  t0=datetime.datetime(2008, 9, 15),
                  e=.9949607008417696,
                  a=182.0519703474959,
                  i=89.21708989130315,
                  M0=1.67964178642615,
                  Omega=282.9487539423989,
                  omega=130.662020526416
                  )

# C/1996 B2 (Hyakutake)
comet_hyakutake = dict(name_fr="Hyakutake",
                       name="Hyakutake",
                       category_fr="comète",
                       t0=datetime.datetime(1996, 3, 16),
                       e=.9998986702212276,
                       a=2272.079439771763,
                       i=124.9226625944912,
                       M0=359.9995777871475,
                       Omega=188.0452284985425,
                       omega=130.1740835084622
                       )

# 109P/Swift-Tuttle
comet_swift_tuttle = dict(name_fr="Swift-Tuttle",
                          name="swift-tutle",
                          category_fr="comète",
                          t0=datetime.datetime(1995, 10, 10),
                          e=0.963225755046038,
                          a=26.0920694978266,
                          i=113.453816997171,
                          M0=7.631696167124212,
                          Omega=139.3811920815948,
                          omega=152.9821676305871
                          )

# 19P/Borrelly
comet_borrelly = dict(name_fr="Borrelly",
                      name="borrelly",
                      category_fr="comète",
                      t0=datetime.datetime(2004, 5, 1),
                      e=.6232892711821078,
                      a=3.609665546424225,
                      i=30.31307021679391,
                      M0=137.9304349204968,
                      Omega=75.43597686258941,
                      omega=353.3506872274951
                      )

comets = [comet_tchouri,
          comet_halley,
          comet_swift_tuttle,
          comet_borrelly
          ]

for comet in comets:
    add_period(comet)
    add_category(comet)

#############
# ASTEROIDS #
#############

# 99942 Apophis (2004 MN4)
asteroid_apophis = dict(name_fr="Apophis",
                      name="apophis",
                      category_fr="astéroïde",
                      t0=datetime.datetime(2020, 5, 31),
                      e=.191474731713038,
                      a=.9225707255061436,
                      i=3.336855220084358,
                      M0=248.148285934327,
                      Omega=204.0483922876889,
                      omega=126.6869602445205
                      )

# 1 Ceres (A801 AA)
asteroid_ceres = dict(name_fr="Cérès",
                      name="ceres",
                      category_fr="astéroïde",
                      t0=datetime.datetime(2019, 4, 27),
                      e=.0760090265983052,
                      a=2.769165148633284,
                      i=10.59406719506626,
                      M0=77.37209751948711,
                      Omega=80.30553090445737,
                      omega=73.59769469844186
                      )

asteroids = [asteroid_apophis,
             asteroid_ceres
             ]

for asteroid in asteroids:
    add_period(asteroid)
    add_category(asteroid)