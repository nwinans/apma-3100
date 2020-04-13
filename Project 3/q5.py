from math import sqrt

z_j = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]

def transform(m_n_array, mu, sigma, n):
    z_n = m_n_array
    for z in z_n:
        z = (z - mu)/(sigma/sqrt(n))

#def estimations: