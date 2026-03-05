
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data.PrimaryFurColor
print(fur_color)
count = fur_color.count()
datas = pandas.DataFrame(fur_color,count)
datas.to_csv("newfile.csv")

