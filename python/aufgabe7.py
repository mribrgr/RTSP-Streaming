import math
from typing import List

from matplotlib import pyplot

k = [2, 3, 5, 10, 20, 48]
color = ["purple", "blue", "green", "yellow", "orange", "red"]

measurements = {
    2: [(0.1, 0.0215), (0.2, 0.0635), (0.3, 0.1632), (0.4, 0.2457)],
    48: [(0.1, 0.1029), (0.2, 0.1964), (0.3, 0.3051), (0.4, 0.396)],
}


# Restfehler Wahrscheinlichkeit
def P_r(P, k):
    result = 1 - (
        (1 - P)  # Fehler dass der Kanal richtig arbeitet
        + (
            P * math.pow((1 - P), k)
        )  # Fehler dass ein packet kaputt ist und der rest nicht kaputt ist
    )
    return result


def main() -> None:
    x: range = range(0, 600)
    x_promill: List[float] = [n / 1000 for n in x]

    pyplot.plot(x_promill, x_promill, color="black", label="baseline")

    for i in range(len(k)):
        y = [P_r(P, k[i]) for P in x_promill]
        pyplot.plot(x_promill, y, color=color[i], label=str(k[i]))

    x_2 = [key for key, _ in measurements[2]]
    y_2 = [value for _, value in measurements[2]]
    pyplot.scatter(x_2, y_2, color=color[0])

    x_48 = [key for key, _ in measurements[48]]
    y_48 = [value for _, value in measurements[48]]
    pyplot.scatter(x_48, y_48, color=color[len(color) - 1])

    pyplot.ylabel("Restfehlerwahrscheinlichkeit")
    pyplot.xlabel("Kanalfehlerwahrscheinlichkeit")

    pyplot.grid(which="both")
    pyplot.legend(fontsize=16)

    pyplot.show()


if __name__ == "__main__":
    main()
