# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:08:03 2021

@author: DELL
"""
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
from scipy import stats
import statsmodels.api as sm
import math
data = np.random.normal(0, 1, 1000)

class visualization:
    def __init__(self):
        self.data = data
        self.mean = self.means()
        self.med = self.meds()
        self.mod = self.mods()
        self.max = self.maxs()
        self.min = self.mins()
    def means(self):
        means = np.mean(self.data)
        
        return means
    
    def meds(self):
        meds = np.median(self.data)
        return meds
    
    def mods(self):
        mods = stats.mode(self.data)
        return mods
    
    def maxs(self):
        maxs = np.max(self.data)
        return maxs
    
    def mins(self):
        mins = np.min(self.data)
        return mins
    
    def tinh_quantile(self, q):
        quantiles = np.quantile(self.data, q)
        return quantiles
    
    def quantile(self, q):
        percentile = self.tinh_quantile(q)
        return percentile
    
    def hist(self):
        plt.hist(self.data,20, density=2, color = 'skyblue', edgecolor = 'green')
        mu = 0
        sigma = math.sqrt(np.std(self.data))
        x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma), color = 'green')
    
    def qq_plot(self):
        qq = sm.qqplot(self.data, line = '45', color = 'y')
        plt.show(qq)
        return qq
    
    pass
vi = visualization()
print("mean = ", vi.mean)
print("med = ", vi.med)
print("mod = ", vi.mod)
print("max = ", vi.max)
print("min = ", vi.min)
print("quantile 0.25 = ", vi.quantile(0.25), "\n",
      "quantile 0.5 = ", vi.quantile(0.5),"\n" ,
      "quantile 0.75 = ", vi.quantile(0.75),"\n")

vi.hist()
vi.qq_plot()