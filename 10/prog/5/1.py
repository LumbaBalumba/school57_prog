import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.1, dtype=float)
y1 = x**2
y2 = x**0.5

csfont = {"fontname": "Comic Sans MS"}
hfont = {"fontname": "Helvetica"}
imgpath = "photo.jpg"

im = plt.imread(imgpath)
ax = plt.gca()
ax.figure.figimage(
    im,
    ax.bbox.xmax // 2 - im.shape[0] // 2,
    ax.bbox.ymax // 2 - im.shape[1] // 2,
    alpha=0.25,
    zorder=1,
)

plt.plot(x, y1, c="red", marker="^", label=r"$x^2$")
plt.plot(x, y2, c="#781488", marker="o", label=r"$\sqrt{x}$")

plt.title("Idk lol (some plots)")
plt.xlabel(r"$\gamma$")
plt.ylabel(r"$\chi$" * 100)

plt.legend()

plt.show()
