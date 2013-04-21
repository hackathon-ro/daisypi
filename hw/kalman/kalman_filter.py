#!/usr/bin/python

import os
import math
import random

def frand():
    return 2*(random.random() - 0.5)

if __name__ == "__main__":
    x_est_last = 0
    P_last = 0
    Q = 0.022
    R = 0.617

    z_real = 0.5

    x_est_last = z_real + frand() * 0.09
    sum_error_kalman = 0
    sum_error_measure = 0

    for i in range(30):
        #do a prediction
        x_temp_est = x_est_last
        P_temp = P_last + Q

        #calculate the Kalman gain
        K = P_temp * (1.0/(P_temp + R))

        #measure the real value with noise
        z_measured = z_real + frand()*0.09

        #correct values
        x_est = x_temp_est + K * (z_measured - x_temp_est)
        P = (1 - K) * P_temp

        #print test values
        print "Ideal position: %s" % z_real
        print "Measured position: %s [diff: %s]" % (z_measured, math.fabs(z_real - z_measured))
        print "Kalman position: %s [diff: %s]" % (x_est, math.fabs(z_real - x_est))

        sum_error_kalman += math.fabs(z_real - x_est)
        sum_error_measure += math.fabs(z_real - z_measured)

        #update last values
        P_last = P
        x_est_last = x_est

    print "Total error if using raw measured: %s" % sum_error_measure
    print "Total error if using kalman filter: %s" % sum_error_kalman
    print "Reduction in errror(in procents):%s" % (100 - ((sum_error_kalman / sum_error_measure) * 100))
