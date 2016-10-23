import numpy as np
import matplotlib.pyplot as plt

fracture_pressure_abnormal_data = np.loadtxt("data/fracture_pressure_abnormal.csv", delimiter=",")
fracture_pressure_abnormal, TVD_frac_abnormal = fracture_pressure_abnormal_data.T

pore_pressure_data_abnormal = np.loadtxt("data/pore_pressure_abnormal.csv", delimiter=",")
pore_pressure_abnormal, TVD_pore_abnormal = pore_pressure_data_abnormal.T

fig, axarr = plt.subplots(1, 2, sharey=True, figsize=(10, 10))

ax = axarr[0]
ax2 = axarr[1]

ax.set_title("Normal Pressure Gradient", fontsize=20, y=1.08)
ax2.set_title("Abnormal Pressure Gradient", fontsize=20, y=1.08)

label_size = 12

ax.plot(fracture_pressure, TVD_frac, color="red", linewidth=3, label="Fracture Pressure")
ax.plot(pore_pressure, TVD_pore, color="blue", linewidth=3, label="Pore Pressure")

ax2.plot(fracture_pressure_abnormal, TVD_frac_abnormal, color="red", linewidth=3, label="Fracture Pressure")
ax2.plot(pore_pressure_abnormal, TVD_pore_abnormal, color="blue", linewidth=3, label="Pore Pressure")


ax.set_ylabel("Total Vertical Depth [ft]", fontsize=25)
ax.set_ylim(ax.get_ylim()[::-1])

ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")

yed = [tick.label.set_fontsize(label_size) for tick in ax.yaxis.get_major_ticks()]
xed = [tick.label.set_fontsize(label_size) for tick in ax.xaxis.get_major_ticks()]


ax2.xaxis.tick_top()
ax2.xaxis.set_label_position("top")

yed = [tick.label.set_fontsize(label_size) for tick in ax2.yaxis.get_major_ticks()]
xed = [tick.label.set_fontsize(label_size) for tick in ax2.xaxis.get_major_ticks()]

#ax.set_xlabel("Equivalent Mud Density [ppg]", fontsize=25)
ax.ticklabel_format(fontsize=25)
ax2.ticklabel_format(fontsize=25)

ax.grid()
ax2.grid()
#ax.legend(fontsize=25)
fig.savefig("data/pressure_comparison.jpeg", dpi=300)