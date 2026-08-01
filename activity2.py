import scipy.stats as stats

probability1 = stats.poisson.pmf(6, 10)
print("The probability of rain for 6 days is:", probability1)

probability2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14, 10)
print("The probability of rain for 12 - 14 days is:", probability2)