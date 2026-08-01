import scipy.stats as stats

probability1 = 1-stats.poisson.cdf(20, 15)
print(probability1)

probability2 = 1-stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print(probability2)