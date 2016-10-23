import matplotlib.pyplot as plt

def plot_casing_setting_depths(ax, fracture_pressure, pore_pressure, TVD_frac, TVD_pore, 
                               fracture_pressure_safety=None, pore_pressure_safety=None,
                               casing_seats_ppg=None, casing_seats_tvd=None):
    """
        This is a simple method to display the pore pressure and fracture pressure
        for a casing setting depth plot. Can include safety margins and casing seats if provided.

        Example usage:
        main.py:
        %matplotlib inline #if you want to inline the display in a jupyter notebook
        fig, ax = plt.subplots(1, figsize=(13, 13))
        plot_casing_setting_depths(ax, my_frac_pres, my_pore_pres, my_tvd_frac, my_tvd_pore,
                                   fracture_pressure_safety=my_frac_safety,
                                   pore_pressure_safety=my_pore_safety,
                                   casing_seats_ppg=my_seats, casing_seats_tvd=my_seats_tvd)
    """
    
    ax.set_title("Casing Setting Depths", fontsize=30, y=1.08)

    label_size = 12
    
    ax.plot(fracture_pressure, TVD_frac, color="red", linewidth=3, label="Fracture Pressure")
    ax.plot(pore_pressure, TVD_pore, color="blue", linewidth=3, label="Pore Pressure")
    if fracture_pressure_safety is not None:
        ax.plot(fracture_pressure_safety, TVD_frac, color="red", linewidth=3, label="Fracture Pressure", linestyle="--")

    if pore_pressure_safety is not None:
        ax.plot(pore_pressure_safety, TVD_pore, color="blue", linewidth=3, label="Pore Pressure", linestyle="--")

    if casing_seats_ppg is not None and casing_seats_tvd is not None:
        ax.plot(casing_seats_ppg, casing_seats_tvd, color="black", linestyle="--", linewidth=3, label="Casing Seats")

    ax.set_ylabel("Total Vertical Depth [ft]", fontsize=25)
    ax.set_ylim(ax.get_ylim()[::-1])

    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")

    yed = [tick.label.set_fontsize(label_size) for tick in ax.yaxis.get_major_ticks()]
    xed = [tick.label.set_fontsize(label_size) for tick in ax.xaxis.get_major_ticks()]
    ax.set_xlabel("Equivalent Mud Density [ppg]", fontsize=25)
    ax.ticklabel_format(fontsize=25)
    ax.grid()
    ax.legend(fontsize=20)
    
def get_casing_seat_plot_data(pore_pressure, tvd_pore, casing_seats):
    """
        This method transforms our casing seat data into a representation that is easier to plot.
    """
    casing_seats_tvd = [tvd_pore[-1], casing_seats[0][0]]
    casing_seats_ppg = [pore_pressure[-1], pore_pressure[-1]]

    for p1, p2 in zip(casing_seats, casing_seats[1::]):
        casing_seats_tvd.append(p1[0])
        casing_seats_tvd.append(p2[0])

    for p1, p2 in zip(casing_seats, casing_seats):
        casing_seats_ppg.append(p1[1])
        casing_seats_ppg.append(p2[1])
      
    return casing_seats_tvd, casing_seats_ppg[0:-2]