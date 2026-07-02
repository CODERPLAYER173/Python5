from matplotlib.pyplot import *
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from seaborn import displot
#making a linear regression model that predicts the high  and closing price
data = pd.read_csv('nifty.csv')
lm = LinearRegression()
x = data[['Open','High','Low','Close','Shares Traded']]
y = data['Date']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
lm.fit(X_train, y_train)
prediction = lm.predict(X_test)
plot(y_test,prediction)
show()

plot(y,x)
show()