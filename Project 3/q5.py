from math import sqrt
import scipy.stats as st

z_j = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]

def transform(m_n_array, mu, sigma, n):
    z_n = m_n_array.copy()
    for z in z_n:
        z = (z - mu)/(sigma/sqrt(n))
    return z_n

def estimations(z_n, j):
    z1 = z_j[j]
    for z2 in z_n:
        if z2 >= z1:
            return z_n.find(z2) / len(z_n)

def evaluateMAD(z_n):
    mad = []
    for i in range (0,7):
        F_n = estimations(z_n, i)
        phi = st.norm.cdf(z_j[i])
        mad.append(abs(F_n - phi))
    return max(mad)