import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    #rad_per_kph = abs((np.pi - (20 * np.pi / 180)) / 40)
    rad_per_kph = abs((np.pi - (np.deg2rad(-90)))/65)
    theta = np.arange(0, 2*np.pi, rad_per_kph)
    theta_5 = np.arange(0, 2*np.pi, rad_per_kph*5)
    # rads = np.arange(0, (2 * np.pi), 0.01)

    # #plt.tick_params(direction='out', length=6, width=2, colors='r',
    #            grid_color='r', grid_alpha=0.5)
    r = 1
    #plt.figure(figsize=(5, 5))
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # plotting the circle
    for rad in [0, rad_per_kph*30, rad_per_kph*40, np.deg2rad(270)]:
        #rad = np.deg2rad(degree)
        ax.plot([rad, rad], [0, 1], color="black", linewidth=1)
        ax.text(rad, 1.2, math.ceil(rad/rad_per_kph), fontsize=16, fontweight="bold")
    for rad in theta:
        #if rad <= np.deg2rad(290):
            ax.plot([rad, rad], [0.75, 1], color="gray", linewidth=0.5)

        #plt.polar([rad, rad], [0, r], 'r+', linewidth=5, markersize=2)
    for rad in theta_5:
        #if rad <= np.deg2rad(290):
        ax.plot([rad, rad], [0.75, 1], color="red", linewidth=1)
    # plt.polar(0, 0, 'b+', linewidth=3, markersize=5)

    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    #frame1.axes.get_xaxis().set_ticks([])
    frame1.set_theta_zero_location('W')
    frame1.set_theta_direction(-1)
    plt.savefig('kph_65_at_90d.eps', format='eps', dpi=150)
    plt.savefig('kph_65_at_90d.pdf', format='pdf', dpi=150)


    # display the Polar plot
    plt.show()

    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # ax.plot(theta, 2)
    # ax.set_rmax(2)
    # #ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
    # ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    # ax.grid(True)
    #
    # ax.set_title("A line plot on a polar axis", va='bottom')
    # plt.show()


if __name__ == "__main__":
    main()
