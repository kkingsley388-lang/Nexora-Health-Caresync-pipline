from pathlib import Path
import pandas as pd

data_path = Path(r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data")

encounters_df = pd.read_csv(f"{data_path}/encounters.csv")
conditions_df = pd.read_csv(f"{data_path}/conditions.csv")
patients_df = pd.read_csv(f"{data_path}/patients.csv")
organizations_df = pd.read_csv(f"{data_path}/organizations.csv")
payers_df = pd.read_csv(f"{data_path}/payers.csv")
providers_df = pd.read_csv(f"{data_path}/providers.csv")

facts_encounter_df = encounters_df.copy(deep=True)
facts_condition_df = conditions_df.copy(deep=True)

N = 4 

facts_encounter_df["START"] = pd.to_datetime(facts_encounter_df["START"], errors="coerce")
latest_date = facts_encounter_df["START"].max() 

# Find the Monday of the week containing the latest encounter date
monday = latest_date - pd.Timedelta(int(latest_date.dayofweek), unit="D")

# Start with the most recent COMPLETE week.
complete_week_monday = monday - pd.to_timedelta(7, unit="D")
complete_week_monday = complete_week_monday.normalize()

week_start = complete_week_monday

for i in range(N):
  week_end = week_start + pd.Timedelta(7, unit="D")
  
  week_encounter = facts_encounter_df[(facts_encounter_df["START"] >= week_start) & (facts_encounter_df["START"] < week_end)]

  week_conditions = facts_condition_df[facts_condition_df["ENCOUNTER"].isin(week_encounter["Id"])]
  
  week_folder = Path(f"{data_path}/incoming/week_{week_start.strftime('%Y-%m-%d')}")
  week_folder.mkdir(parents=True, exist_ok=True)

  # Save this week's encounters.
  save_encounter_file = week_folder / "encounters.csv"
  week_encounter.to_csv(save_encounter_file, index=False)

  # the filtered data frame is stored in the variable  week_condition and 
  # You can also specify a folder/path to the folder and the name you want to save the file as "conditions.csv" and assign it to a varaible name called , anyhthing 
  save_condition_file = week_folder / "conditions.csv"
  week_conditions.to_csv(save_condition_file, index=False)

  # Save the FULL dimension snapshots into every weekly folder.
  patients_df.to_csv(week_folder / "patients.csv", index=False)
  organizations_df.to_csv(week_folder / "organizations.csv", index=False)
  payers_df.to_csv(week_folder / "payers.csv", index=False)
  providers_df.to_csv(week_folder / "providers.csv", index=False)

  # Move back 7 days so the next loop processes the previous week
  week_start =  week_start - pd.Timedelta(7, unit="D")

  