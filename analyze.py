import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "accident_data.csv"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["City", "Weather", "Road_Condition", "Time_of_Day"])

# 1. Accident count by time of day
counts = df["Time_of_Day"].value_counts().reindex(
    ["Morning", "Afternoon", "Evening", "Night"]
).fillna(0)

plt.figure(figsize=(9, 5))
counts.plot(kind="bar")
plt.title("Accidents by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "01_accidents_by_time.png", dpi=180)
plt.close()

# 2. Road condition
road_counts = df["Road_Condition"].value_counts()
plt.figure(figsize=(9, 5))
road_counts.plot(kind="bar")
plt.title("Accidents by Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "02_accidents_by_road_condition.png", dpi=180)
plt.close()

# 3. Weather
weather_counts = df["Weather"].value_counts()
plt.figure(figsize=(9, 5))
weather_counts.plot(kind="bar")
plt.title("Accidents by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "03_accidents_by_weather.png", dpi=180)
plt.close()

# 4. City hotspots
city_counts = df["City"].value_counts().sort_values(ascending=True)
plt.figure(figsize=(9, 5))
city_counts.plot(kind="barh")
plt.title("Accident Hotspots by City")
plt.xlabel("Number of Accidents")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(OUT / "04_city_hotspots.png", dpi=180)
plt.close()

# 5. Contributing-factor heatmap without seaborn
pivot = pd.crosstab(df["Weather"], df["Road_Condition"])
plt.figure(figsize=(9, 5))
plt.imshow(pivot.values, aspect="auto")
plt.title("Weather vs Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Weather")
plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=30)
plt.yticks(range(len(pivot.index)), pivot.index)
for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        plt.text(j, i, pivot.iloc[i, j], ha="center", va="center")
plt.colorbar(label="Accidents")
plt.tight_layout()
plt.savefig(OUT / "05_weather_road_heatmap.png", dpi=180)
plt.close()

# 6. Severity by time of day
severity = pd.crosstab(df["Time_of_Day"], df["Severity"]).reindex(
    ["Morning", "Afternoon", "Evening", "Night"]
)
severity.plot(kind="bar", figsize=(10, 5))
plt.title("Accident Severity by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "06_severity_by_time.png", dpi=180)
plt.close()

# Save summary tables
summary = pd.DataFrame({
    "Metric": [
        "Total accidents",
        "Most common city",
        "Most common weather",
        "Most common road condition",
        "Most common time of day",
        "Severe accidents"
    ],
    "Value": [
        len(df),
        df["City"].mode().iat[0],
        df["Weather"].mode().iat[0],
        df["Road_Condition"].mode().iat[0],
        df["Time_of_Day"].mode().iat[0],
        int((df["Severity"] == "Severe").sum())
    ]
})
summary.to_csv(OUT / "summary.csv", index=False)

print("\nTRAFFIC ACCIDENT ANALYSIS")
print("=" * 30)
print(summary.to_string(index=False))
print("\nCharts saved in:", OUT)
