# Work with data using `pandas`
Now we understand the basics of creating charts with Python, let's learn to make visualization working with datasets. [`pandas`](https://pandas.pydata.org/docs/index.html) is a common tool to process and work with data.

If `pandas` isn't installed, use `pip install pandas` to install it.

example datasets: [pokemon.csv](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6#file-pokemon-csv)

## Loading data and dataframe
```
import pandas as pd

df = pd.read_csv("pokemon.csv") # load your dataset

df_sorted = df.sort_values(by="Attack", ascending=False) # df.sort() can sort data by a given attribute

# df_sorted = df.sort_values(by=["Type 1", "Attack"], ascending=[True, False]) # sort by multiple attributes


print(df.head()) # show first few rows
print(df.info()) # check dataset info
```

## How many pokemons for each Type 1?
```
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")
type_counts = df["Type 1"].value_counts()
unique_types = type_counts.index

plt.figure(figsize=(10, 5))
plt.bar(unique_types, type_counts.values, color="skyblue")
plt.xticks(rotation=45)
plt.xlabel("Primary Type")
plt.ylabel("Count")
plt.title("Distribution of Pokémon by Type 1")
plt.show()
```

In case you want to use more colors, `seaborn` has some color palettes. Run `pip install seaborn` to install it.
- [seaborn plot gallery](https://seaborn.pydata.org/examples/index.html) 

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv("pokemon.csv")
type_counts = df["Type 1"].value_counts()
unique_types = type_counts.index 

colors = sns.color_palette("tab20", n_colors=len(unique_types)) 

plt.figure(figsize=(10, 5))
plt.bar(unique_types, type_counts.values, color=colors)
plt.xticks(rotation=45)
plt.xlabel("Type 1")
plt.ylabel("Count")
plt.title("Distribution of Pokémon by Type 1")
plt.show()
```

### Seaborn Categorical Color Palettes
- **`tab10`** → 10 distinct colors  
- **`tab20`** → 20 distinct colors  
- **`Set3`** → 12 pastel-like colors  
- **`Paired`** → 12 paired colors  
- **`Dark2`** → 8 distinct colors  
- **`Accent`** → 8 distinct colors  
- **`Pastel1`** → 9 soft colors  
- **`Pastel2`** → 8 soft colors  
- **`Deep`** → 10 distinct colors 

[seaborn color palettes](https://seaborn.pydata.org/generated/seaborn.color_palette.html)

## Is there a relationship between Attack and Defense?
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("pokemon.csv")
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Attack", y="Defense", data=df, color="#0000ff") 
sns.regplot(x="Attack", y="Defense", data=df, scatter=False, color="red") # draw a regression line
plt.title("Attack vs. Defense")
plt.show()
```

## Based on the last question, visiualize for certain Type 1 pokemons
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("pokemon.csv")

selected_types = ["Fire", "Water", "Grass", "Electric"]
filtered_df = df[df["Type 1"].isin(selected_types)]
types_palette={"Fire": "#FF4500", "Water": "#1E90FF", "Grass": "#32CD32", "Electric": "#FFD700"}

plt.figure(figsize=(8, 6))
sns.scatterplot(x="Attack", y="Defense", hue="Type 1", data=filtered_df, palette=types_palette)

plt.title("Attack vs. Defense of Selected Pokémon Types")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.legend(title="Type 1")
plt.show()
```

