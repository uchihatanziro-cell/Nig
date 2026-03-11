import numpy as np
from scipy import stats

N = 10

x = np.random.randn(N) + 2
y = np.random.randn(N)

var_x = x.var(ddof=1)
var_y = y.var(ddof=1)

SD = np.sqrt((var_x + var_y) / 2)
print("Standard Deviation =", SD)

tval = (x.mean() - y.mean()) / (SD * np.sqrt(2 / N))

dof = 2 * N - 2
pval = 2 * (1 - stats.t.cdf(abs(tval), df=dof))

print("Manual t =", tval)
print("Manual p =", pval)

tval2, pval2 = stats.ttest_ind(x, y)
print("SciPy t =", tval2)
print("SciPy p =", pval2)
