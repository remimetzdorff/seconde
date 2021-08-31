import numpy as npimport matplotlib.pyplot as pltfrom matplotlib import animationfrom celestialbody.celestialbody import CelestialBodyimport datetime############ OPTIONS ############fps = 25animate = Trueshow_speed = Falsereferentiel = "geocentric" # "heliocentric" or "geocentric"start = datetime.datetime(2021,1,1)stop  = datetime.datetime(2100,1,2)step_day = datetime.timedelta(days=4)###### ## DATA #########earth = CelestialBody("EM Bary")mars  = CelestialBody("Mars")date = startx0, x, X, y0, y, Y = [], [], [], [], [], []while date < stop:    earth.date = date    mars.date  = date    val_x0, val_y0, _ = earth.position    val_x, val_y, _   = mars.position    x0.append(val_x0), y0.append(val_y0)    x.append(val_x), y.append(val_y)    X.append(val_x-val_x0), Y.append(val_y-val_y0)    date += step_dayx0, y0 = np.array(x0), np.array(y0) # Earthx, y = np.array(x), np.array(y)     # MarsX, Y = np.array(X), np.array(Y)     # Sunif not animate:    # PLOT FINAL GRAPHS WITHOUT ANIMATION    # Geocentric    plt.figure(figsize=(6,6))    sps = (1,1)    ax = plt.subplot2grid(sps, (0,0))    ax.set_aspect("equal")    ax.set_xlim(-3,3)    ax.set_ylim(-3,3)    ax.plot([0],[0], "oC0")    ax.annotate("Terre", (0,0), color="C0", xytext=(-2,2), textcoords="offset points", ha="right")    ax.plot(X,Y, "-C3", linewidth=.1)    ax.plot(X[-1], Y[-1], "oC3", label="Mars")    ax.plot(-x0, -y0, "-C1", linewidth=.1)    ax.plot(-x0[-1], -y0[-1], "oC1", linewidth=.1, label="Soleil")    ax.legend(loc="upper left")    ax.set_title("Mouvement de Mars \"autour\" de la Terre")    ax.set_xlabel("x (au)")    ax.set_ylabel("y (au)")    # Heliocentric    plt.figure(figsize=(6,6))    sps = (1,1)    ax = plt.subplot2grid(sps, (0,0))    ax.set_aspect("equal")    ax.set_xlim(-2,2)    ax.set_ylim(-2,2)    ax.plot([0],[0], "oC1")    ax.annotate("Soleil", (0,0), color="C1", xytext=(-3,3), textcoords="offset points", ha="right")    ax.plot(x0, y0, "-C0", linewidth=.1)    ax.plot(x0[-1], y0[-1], "oC0", label="Terre")    ax.plot(x, y, "-C3", linewidth=.1)    ax.plot(x[-1], y[-1], "oC3", label="Mars")    ax.legend(loc="upper left")    ax.set_title("Mouvement de la Terre et de Mars autour du Soleil")    ax.set_xlabel("x (au)")    ax.set_ylabel("y (au)")else:    # Setup figure    if referentiel == "geocentric":        a_lim = 3        title = "Mouvement de Mars \"autour\" de la Terre"    elif referentiel == "heliocentric":        a_lim = 2        title = "Mouvement de la Terre et de Mars autour du Soleil"        fig = plt.figure(figsize=(6,6))    sps = (1,1)    ax = plt.subplot2grid(sps, (0,0))    ax.set_aspect("equal")    ax.set_xlim(-a_lim,a_lim)    ax.set_ylim(-a_lim,a_lim)    ax.set_title(title)    ax.set_xlabel("x (au)")    ax.set_ylabel("y (au)")        if referentiel == "geocentric":        ax.plot([0],[0], "oC0")        ax.annotate("Terre", (0,0), color="C0", xytext=(-2,2), textcoords="offset points", ha="right")        trajectory_sun,  = ax.plot([], [], "-C1", linewidth=.1)        sun,             = ax.plot([], [], "oC1", label="Soleil")        trajectory_mars, = ax.plot([], [], "-C3", linewidth=.1) # trajectory        planet_mars,     = ax.plot([], [], "oC3", label="Mars") # planet        sun_speed  = ax.quiver(0,0,0,0, color="C1", alpha=.5, width=.005, angles='xy', scale_units='xy', scale=1)        mars_speed = ax.quiver(0,0,0,0, color="C3", alpha=.5, width=.005, angles='xy', scale_units='xy', scale=1)        # Animation        def init():            trajectory_mars.set_data([], [])            planet_mars.set_data([], [])            trajectory_sun.set_data([], [])            sun.set_data([], [])            return trajectory_mars,        def animate(i):            trajectory_mars.set_data(X[:i], Y[:i])            planet_mars.set_data(X[i], Y[i])            trajectory_sun.set_data(-x0[:i], -y0[:i])            sun.set_data(-x0[i], -y0[i])            if i<len(x0)-1 and show_speed:                u, v = -x0[i+1]+x0[i], -y0[i+1]+y0[i]                sun_speed.set_UVC(3*u,3*v)                sun_speed.set_offsets((-x0[i], -y0[i]))                u, v = X[i+1]-X[i], Y[i+1]-Y[i]                mars_speed.set_UVC(3*u,3*v)                mars_speed.set_offsets((X[i], Y[i]))            return trajectory_mars,    elif referentiel == "heliocentric":        ax.plot([0],[0], "oC1")        ax.annotate("Soleil", (0,0), color="C1", xytext=(-3,4), textcoords="offset points", ha="right")        trajectory_earth, = ax.plot([], [], "-C0", linewidth=.1)        planet_earth,     = ax.plot([], [], "oC0", label="Terre")        trajectory_mars,  = ax.plot([], [], "-C3", linewidth=.1)        planet_mars,      = ax.plot([], [], "oC3", label="Mars")        earth_speed = ax.quiver(0,0,0,0, color="C0", alpha=.5, width=.005, angles='xy', scale_units='xy', scale=1)        mars_speed  = ax.quiver(0,0,0,0, color="C3", alpha=.5, width=.005, angles='xy', scale_units='xy', scale=1)        def init():            trajectory_earth.set_data([], [])            planet_earth.set_data([], [])            trajectory_mars.set_data([], [])            planet_mars.set_data([], [])            return trajectory_earth,        def animate(i):            trajectory_earth.set_data(x0[:i], y0[:i])            planet_earth.set_data(x0[i], y0[i])            trajectory_mars.set_data(x[:i], y[:i])            planet_mars.set_data(x[i], y[i])            if i<len(x0)-1 and show_speed:                u, v = x0[i+1]-x0[i], y0[i+1]-y0[i]                earth_speed.set_UVC(3*u,3*v)                earth_speed.set_offsets((x0[i], y0[i]))                u, v = x[i+1]-x[i], y[i+1]-y[i]                mars_speed.set_UVC(3*u,3*v)                mars_speed.set_offsets((x[i], y[i]))            return trajectory_earth,    plt.tight_layout()    plt.legend(loc="upper left")        anim = animation.FuncAnimation(fig, animate, frames=len(X)-1, interval=1e3/fps, init_func=init)