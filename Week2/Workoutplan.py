import pandas as pd
# Define the training plan for the first 7 weeks
weeks_data_first_7 = [
    {
        "Week": 1,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "5 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "3 km Easy Run (6:30 - 7:00 min/km), 2 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 2,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "6 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "3 km Easy Run (6:30 - 7:00 min/km), 3 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 3,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "7 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "4 km Easy Run (6:30 - 7:00 min/km), 3 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 4,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "8 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "4 km Easy Run (6:30 - 7:00 min/km), 4 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 5,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "9 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "5 km Easy Run (6:30 - 7:00 min/km), 4 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 6,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "10 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "5 km Easy Run (6:30 - 7:00 min/km), 5 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    },
    {
        "Week": 7,
        "Days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        "Workouts": [
            "11 km Easy Run (6:30 - 7:00 min/km)",
            "Lower Body Strength + Core",
            "6 km Easy Run (6:30 - 7:00 min/km), 5 km Tempo Run (5:20 - 5:40 min/km), 3 km Easy Run (6:30 - 7:00 min/km)",
            "Upper Body Strength + Core",
            "5 km Park Run (5:51 min/km)"
        ]
    }
]

# Convert the data to a DataFrame
df = pd.DataFrame(weeks_data_first_7)

# Prepare the data for the Excel file
excel_data = []

for week in weeks_data_first_7:
    week_number = week["Week"]
    for day, workout in zip(week["Days"], week["Workouts"]):
        excel_data.append({"Week": week_number, "Day": day, "Workout": workout})

# Convert to DataFrame
df_excel = pd.DataFrame(excel_data)

# Save to an Excel file
file_path = "/Users/finpearson/Desktop/Github/ANLE---Python-/Week2/half_marathon_training_plan_first_7_weeks.xlsx"
df_excel.to_excel(file_path, index=False)