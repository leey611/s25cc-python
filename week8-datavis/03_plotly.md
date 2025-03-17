# Interactive plots with Plotly
In addition to `matplotlib` and `seaborn`, [`plotly`](https://plotly.com/python/) is also a great tool when it comes to making interactive charts (it also looks slightly more aesthetic). 

Use `pip install plotly` to install it.

## Scatter Plot: Speed vs. Attack
```
import plotly.express as px
df = pd.read_csv("pokemon.csv")

fig = px.scatter(df, x="Attack", y="Speed", color="Type 1", hover_name="Name", title="Pokémon Attack vs. Speed")
fig.show()
```
To vary the size of the circles, use `size`; to set a max size, use `size_max`
```
fig = px.scatter(df, x="Attack", y="Speed", color="Type 1", size="Defense", size_max=10, hover_name="Name", title="Pokémon Attack vs. Speed")
```

To display more details on the tooltips, use `hover_data`
```
fig = px.scatter(df, x="Attack", y="Speed", color="Type 1", 
                 hover_name="Name", hover_data=["HP", "Defense"], 
                 title="Pokémon Attack vs. Speed")
```

## Bar Chart: Top 10 Pokemon with Highest Attack
```
import plotly.express as px

df = pd.read_csv("pokemon.csv")
top_attack_pokemon = df.nlargest(10, "Attack")

fig = px.bar(
    top_attack_pokemon, 
    x="Name", 
    y="Attack", 
    color="Type 1",  
    title="Top 10 Pokémon with Highest Attack",
    labels={"Attack": "Attack value", "Name": "Pokemon"},
)

fig.show()
```

## Subpolots: Top 10 Highest Attack Fire and Water Pokemon
- [Subplots in Ploty](https://plotly.com/python/subplots/)
- [python `zip`](https://www.w3schools.com/python/ref_func_zip.asp)
```
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("pokemon.csv")

top_fire_pokemon = df[df["Type 1"] == "Fire"].nlargest(10, "Attack")
top_water_pokemon = df[df["Type 1"] == "Water"].nlargest(10, "Attack")

fig = make_subplots(
    rows=1, 
    cols=2, 
    subplot_titles=[
        "Top 10 Fire Pokémon by Attack", 
        "Top 10 Water Pokémon by Attack"
    ]
)

fig.add_trace(
    go.Bar(
        x=top_fire_pokemon["Name"],
        y=top_fire_pokemon["Attack"],
        marker_color='firebrick',
        text=top_fire_pokemon["Attack"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in 
                  zip(top_fire_pokemon["Name"], top_fire_pokemon["Attack"])]
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=top_water_pokemon["Name"],
        y=top_water_pokemon["Attack"],
        marker_color='royalblue',
        text=top_water_pokemon["Attack"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in 
                  zip(top_water_pokemon["Name"], top_water_pokemon["Attack"])]
    ),
    row=1, col=2
)

fig.update_layout(
    title_text="Top 10 Pokemon by Attack for Fire and Water Types",
    height=500,
    width=1000,
    showlegend=False
)

fig.update_xaxes(tickangle=45)

fig.show()
```

