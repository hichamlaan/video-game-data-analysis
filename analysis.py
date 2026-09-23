import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
games = pd.read_csv("vgsales.csv")

# Top 10 best-selling games
top_games = games.sort_values("Global_Sales", ascending=False)
print("Top 10 Best Selling Games:")
print(top_games[["Name", "Global_Sales"]].head(10))

# Global Sales by Genre
genre_groups = games.groupby("Genre")
genre_sales = genre_groups["Global_Sales"].sum()
genre_sales = genre_sales.sort_values(ascending=False)

print("Sales by Genre:")
print(genre_sales)

# Graph Global Sales by Genre
genre_sales.plot(kind="bar")

plt.title("Global Video Game Sales by Genre")
plt.xlabel("Video Game Genre")
plt.ylabel("Global Sales (Millions)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/genre_sales.png")
plt.show()

# Global Sales by Platform
platform_group = games.groupby("Platform")
platform_sales = platform_group["Global_Sales"].sum()
platform_sales = platform_sales.sort_values(ascending=False)

top_platforms = platform_sales.head(10)
print("Top 10 Platforms:")
print(top_platforms)

# Graph Global Sales by Platform
top_platforms.plot(kind="bar")

plt.title("Top 10 Video Game Platforms by Global Sales")
plt.xlabel("Video Game Platform")
plt.ylabel("Global Sales (Millions)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/platform_sales.png")
plt.show()

# Global Sales by Year
years_data = games.dropna(subset=["Year"])
years_data["Year"] = years_data["Year"].astype(int)

years_groups = years_data.groupby("Year")
years_sales = years_groups["Global_Sales"].sum()

print("Sales by Year:")
print(years_sales)

# Graph Global Sales by Year
years_sales.plot(kind="line")

plt.title("Global Video Game Sales by Year")
plt.xlabel("Year")
plt.ylabel("Global Sales (Millions)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/year_sales.png")
plt.show()

# Sales by Genre and Region
regional_sales = genre_groups[["NA_Sales", "EU_Sales", "JP_Sales"]].sum()
print("Sales by Genre and Region:")
print(regional_sales)

# Graph Sales by Genre and Region
regional_sales.plot(kind="bar")

plt.title("Global Video Game Sales by Genre and Region")
plt.xlabel("Genre")
plt.ylabel("Global Sales (Millions)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/regional_sales.png")
plt.show()

# Find the top-selling genre in each region
print("Top Genre in North America:", regional_sales["NA_Sales"].idxmax())
print("Top Genre in Europe:", regional_sales["EU_Sales"].idxmax())
print("Top Genre in Japan:", regional_sales["JP_Sales"].idxmax())

