from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()

#(1 - FIT) finds the x_min and x_max, then
#(2 - TRANSFORM) transforms each element in the dataset
rescaled_weight = scaler.fit_transform(weights)

print rescaled_weight

