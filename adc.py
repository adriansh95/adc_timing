import numpy as np

class adc():
    def __init__(self, dnl, err, measured_bins):
        self.dnl = dnl
        self.err = err
        self.measured_bins = measured_bins
