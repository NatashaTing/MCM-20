import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as stat


def main():

    rates = {'kud': 2, 'krd': 2, 'kdr': 2, 'klu': 2,
             'kul': 2, 'krl': 2, 'kdl': 2, 'klr': 2,
             'kur': 2, 'kru': 2, 'kdu': 2, 'kld': 2}

    X, Y = jump2d(rates)
    print(stat.mean(X), stat.mean(Y))


def jump1d():
    r = 1.2
    alpha = 2.01
    beta = 2.
    n0 = -1  ## must be -1 or 1
    x0 = 0.
    Nsteps = 50000

    T = np.zeros(Nsteps)
    T[0] = 0
    N = np.zeros(Nsteps)
    N[0] = n0
    X = np.zeros(Nsteps)
    X[0] = x0

    for j in np.arange(Nsteps):          ## compute the rate
        n = N[j - 1]
        u = np.random.rand(1)[0]
        if n == 1:
            rate = beta
        else:
            rate = alpha
        tau = -math.log(u) / rate
        T[j] = T[j - 1] + tau            ## t += tau is the same as t = t + tau
        X[j] = X[j - 1] + tau * (n * r)  ## X(t + tau) = X(t) + tau*v(N)
        N[j] = -1 if n == 1 else 1       # update

    fig = plt.figure(1, [10, 6])
    plt.plot(T, X)
    plt.xlabel('t', fontsize=24)
    plt.ylabel('X(t)', fontsize=24)
    plt.title('')
    plt.show()




def jump2d(rates):
    r = 1.2
    Nsteps = 1000
    x0, y0 = 0, 0
    T = np.zeros(Nsteps)
    N = np.zeros(Nsteps)
    M = np.zeros(Nsteps)
    X = np.zeros(Nsteps)
    Y = np.zeros(Nsteps)
    n0, m0 = -1, 0  # start on the left
    X[0], T[0], N[0], M[0] = 0, 0, n0, m0

    for j in np.arange(1, Nsteps):
        n = N[j - 1]  # x
        m = M[j - 1]  # y
        u = np.random.rand(1)[0]
        if n == -1:  # thing on the left

            rate_sum = rates['klu'] + rates['klr'] + rates['kld']
            probs_c = np.array([rates['klu'], rates['klr'], rates['kld']]) / rate_sum
            cum_probs_c = np.cumsum(probs_c)
            u2 = np.random.rand(1)
            if u2 < cum_probs_c[0]:  # from left to up
                N[j] = 0
                M[j] = 1
            elif u2 < cum_probs_c[1]:  # from left to right
                N[j] = 1
                M[j] = 0
            else:  # from left to down
                N[j] = 0
                M[j] = -1
        elif n == 1:  # thing on the right
            rate_sum = rates['kru'] + rates['krl'] + rates['krd']
            probs_c = np.array([rates['kru'], rates['krl'], rates['krd']]) / rate_sum
            cum_probs_c = np.cumsum(probs_c)
            u2 = np.random.rand(1)
            if u2 < cum_probs_c[0]:  # from right to up
                N[j] = 0
                M[j] = 1
            elif u2 < cum_probs_c[1]:  # from right to left
                N[j] = -1
                M[j] = 0
            else:  # from right to down
                N[j] = 0
                M[j] = -1
        elif m == -1:  # thing on the bottom
            # print('m=-1')
            rate_sum = rates['kdu'] + rates['kdr'] + rates['kdl']
            probs_c = np.array([rates['kdu'], rates['kdr'], rates['kdl']]) / rate_sum
            cum_probs_c = np.cumsum(probs_c)
            u2 = np.random.rand(1)
            if u2 < cum_probs_c[0]:  # from down to up
                N[j] = 0
                M[j] = 1
            elif u2 < cum_probs_c[1]:  # from down to right
                N[j] = 1
                M[j] = 0
            else:  # from down to left
                N[j] = -1
                M[j] = 0
        elif m == 1:  # thing going up
            rate_sum = rates['kud'] + rates['kur'] + rates['kul']
            probs_c = np.array([rates['kud'], rates['kur'], rates['kul']]) / rate_sum
            cum_probs_c = np.cumsum(probs_c)
            u2 = np.random.rand(1)
            if u2 < cum_probs_c[0]:  # from up to down
                N[j] = 0
                M[j] = -1
            elif u2 < cum_probs_c[1]:  # from up to right
                N[j] = 1
                M[j] = 0
            else:  # from up to left
                N[j] = -1
                M[j] = 0
        tau = -math.log(u) / rate_sum
        T[j] = T[j - 1] + tau
        X[j] = X[j - 1] + tau * (n * r)  ## X(t + tau) = X(t) + tau*v(N)
        Y[j] = Y[j - 1] + tau * (m * r)

    fig = plt.figure(1, [10, 6])
    # plot(T, X)
    plt.plot(X, Y, '-')
    plt.title('positions over time')
    plt.xlabel('X(t)', fontsize=24)
    plt.ylabel('Y(t)', fontsize=24)
    plt.show()

    return X, Y

if __name__ == "__main__":
    main()




