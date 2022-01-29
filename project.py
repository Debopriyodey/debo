import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pandas.read_csv('iphone_price.csv')
plt.scatter(data['version'],data['price'])
plt.show()
model=LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[12]]))
# # #
# # # import pandas
# # # #import matplotlib.pyplot as plt
# # # from sklearn import datasets, linear_model
# # # data = pandas.read_csv('iphone_price.csv')
# # # #plt.scatter(data['version'], data['price'])
# # # #plt.show()
# # # model = linear_model.LinearRegression()
# # # model.fit(data[['version']], data[['price']])
# # # print(model.predict([[16]]))
#
# import pandas
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# data = pandas.read_csv('iphone_price.csv')
# plt.scatter(data['version'], data['price'])
# plt.show()
# model = LinearRegression()
# model.fit(data[['version']], data[['price']])
# print(model.predict([[30]]))