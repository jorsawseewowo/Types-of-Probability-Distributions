import scipy.stats as stats

n_days = 30
expected_rain = 10
p = expected_rain / n_days

prob_12_or_more = 1 - stats.binom.cdf(11, n_days, p)

prob_12_to_18 = stats.binom.cdf(18, n_days, p) - stats.binom.cdf(11, n_days, p)

print(f"Probability of 12 or more rainy days: {prob_12_or_more:.4f}")
print(f"Probability of 12 to 18 rainy days: {prob_12_to_18:.4f}")