import pandas

data = pandas.read_csv("weather.csv")
print(data)
# print(data["temp"])

# print(type(data))
# print(type(data["temp"]))

# https://pandas.pydata.org/docs/reference/index.html
# Vê os docs desses objetos

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# average_temp = sum(temp_list) / len(data["temp"])

# print("Average: %.1fº Celsius" % data["temp"].mean())

max_temp = data["temp"].max()

# print("Max: %.1fº Celsius" % max_temp)

# Get Column

# print(data["condition"])
# print(data.condition)   # Mesma coisa, o pandas cria as colunas por nos

# Get Row

monday = data[data.day == "Monday"]

# print(monday)
# print(monday.condition)     # Mesma logica das colunas, pandas cria por nos com o nome da coluna
# print(data[data.temp == max_temp])

# Create a Dataframe from Scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_2 = pandas.DataFrame(data_dict)
print(data_2)

# Convert to csv file
data_2.to_csv("data_2.csv")