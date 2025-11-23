import pandas as pd
movies = [
    ["RRR", "tt8178634", "https://www.imdb.com/title/tt8178634/", 8.0, 567890, "Tamil"],
    ["Dude", "tt7838252", "https://www.imdb.com/title/tt7838252/", 7.2, 123456, "Tamil"],
    ["Bigil", "tt9263550", "https://www.imdb.com/title/tt9263550/", 6.8, 245678, "Tamil"],
    ["Thulladha Manamum Thullum", "tt2158679", "https://www.imdb.com/title/tt2158679/", 8.1, 98765, "Tamil"],
    ["Theri", "tt5886893", "https://www.imdb.com/title/tt5886893/", 7.9, 23456, "Tamil"],
    ["Romeo", "tt3674912", "https://www.imdb.com/title/tt3674912/", 7.7, 156789, "Tamil"],
    ["Amaran", "tt6004556", "https://www.imdb.com/title/tt6004556/", 8.3, 345678, "Tamil"],
]

header = ["Movie Name", "Movie ID", "URL", "Rating", "Votes", "Language"]

tamil_movies = [m for m in movies if m[5].lower() == "tamil"]

widths = [max(len(str(row[i])) for row in tamil_movies) for i in range(len(header))]
print("─" * (sum(widths) + 3 * len(widths)))

print("|", end="")
for i, col in enumerate(header):
    print(f" {col:<{widths[i]}} |", end="")
print()

print("─" * (sum(widths) + 3 * len(widths)))

for row in tamil_movies:
    print("|", end="")
    for i, col in enumerate(row):
        print(f" {col:<{widths[i]}} |", end="")
    print()

print("─" * (sum(widths) + 3 * len(widths)))

df = pd.DataFrame(tamil_movies, columns=header)
excel_name = "Tamil_IMDb_Ratings.xlsx"
df.to_excel(excel_name, index=False)

print(f"\n✔ Excel saved successfully: {excel_name}")

