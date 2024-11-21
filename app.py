print("Hello World")
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")

print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

# data_range = pd.date_range(start="2021-05-01", end="2021-05-12")
# print(data_range)

# my_series = pd.Series([2, 4, 6, 8, 10])
# def division(num):
#     return num/2
# Divide = my_series.apply(division)
# print(Divide)

#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]

#df = pd.DataFrame(data,columns=["Brand","Model","Color"])

# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     }
# ]
# df = pd.DataFrame (data)
# df2 = { "brand" : "Tesla", 
#            "model" : "Model S", 
#            "color": "Red" }
# df = df._append(df2, ignore_index = True)
# print(df)

#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
# print(data_frame.iloc[133,6])
# print(data_frame.head(3))
# print(data_frame.tail(3))
#print(data_frame)
#print(data_frame[['Name', 'Type 1']].head(10))
#print(data_frame.loc[data_frame["Attack"]>80])
#legendary_pokemon = data_frame.loc[data_frame['Legendary'] == True]
#print(len(legendary_pokemon))

data_set = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#print(data_set.head(5))
# print(data_set.drop(columns=["Unnamed: 0"], inplace= True))
#print(data_set.iloc[: , 1:].head(5))
#print(data_set.value_counts("Gender"))
# data_group = data_set.groupby("Name").sum()
# print(len(data_group))