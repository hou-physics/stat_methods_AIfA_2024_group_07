from numpy import zeros, log
from numpy.random import multivariate_normal, rand

def MHsampler(loglike, init, cov, n):
    """
    Simple Metropolis Hastings sampler.

    :param loglike: likelihood module with function getLogLikelihood
    :param init: initial position of the chain
    :param cov: covariance matrix of the proposal
    :param n: number of iterations
    """
    d = len(init)
    chain = zeros((n, d))
    likes = zeros(n)
    p = init
    ll = loglike.getLogLikelihood(*p)
    nacc = 0
    for i in range(n):
        pn = multivariate_normal(p, cov)
        lln = loglike.getLogLikelihood(*pn)
        r = rand()
        if lln-ll > log(r):
            p = pn
            ll = lln
            nacc += 1
        chain[i] = p
        likes[i] = ll
    acceptance_ratio = float(nacc)/n
    return chain, likes, acceptance_ratio