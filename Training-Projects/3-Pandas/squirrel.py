import pandas

# Create new table with extrated data

data = pandas.read_csv("squirrel_new_york.csv")

print(data["Primary Fur Color"])

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrels)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gay", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,
              red_squirrels_count,
              black_squirrels_count
              ]
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrel_counts.csv")