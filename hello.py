
import matplotlib.pyplot as plt
import numpy as np

r = 0.5
K = 10.
H1 = 0.1
H2 = 0.1
H3 = 0.1
A = 1
x0 = 12

def plot():

    Delta_t = 0.1
    Nsteps = 1000
    x = np.zeros(Nsteps)
    x1 = np.zeros(Nsteps)
    x2 = np.zeros(Nsteps)
    x3 = np.zeros(Nsteps)
    x[0] = x0
    x1[0] = x0
    x2[0] = x0
    x3[0] = x0
    harvest2 = np.zeros(Nsteps)
    harvest3 = np.zeros(Nsteps)

    def f_logistic(x):
        return r * x * (1 - x / K)

    def f_logistic1(x):
        return r * x * (1 - x / K) - H1

    def f_logistic2(x):
        return r * x * (1 - (x / K)) - H2 * x

    def f_logistic3(x):
        return r * x * (1 - x / K) - H3 * (x / (A + x))

    for n in np.arange(1, Nsteps):
        x[n] = x[n - 1] + Delta_t * f_logistic(x[n - 1])
        x1[n] = x1[n - 1] + Delta_t * f_logistic1(x1[n - 1])
        x2[n] = x2[n - 1] + Delta_t * f_logistic2(x2[n - 1])
        harv2 = f_logistic(x[n - 1]) - f_logistic2(x2[n - 1])
        if harv2 > 0:
            harvest2[n] = harv2

        x3[n] = x3[n - 1] + Delta_t * f_logistic3(x3[n - 1])
        harv3 = f_logistic(x[n - 1]) - f_logistic3(x3[n - 1])
        if harv3 > 0:
            harvest3[n] = harv3

    t = Delta_t * np.arange(Nsteps)
    plt.rcParams["figure.figsize"] = (20, 10)

    plt.figure()
    plt.plot(t, x, '-')  # Logistic Model
    plt.plot(t, x2, 'g')  # Model 2
    plt.plot(t, x3, 'b')  # Model 3
    title = "when r = %s, H_i = %s, K = %s, x0 = %s" % (r, H1, K, x0)
    title2 = 'Fish Population As Described by Different Models'
    plt.title(title2)
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.show()

    print('x2 is asymtotically %s, and x3 is asymtotically %s' %
          (round(x2[Nsteps - 1], 4), round(x3[Nsteps - 1], 4)))
    print('------------')
    print('Note: r = %s, K = %s, x0 = %s' % (r, K, x0))


if __name__ == "_main_":
    plot()
