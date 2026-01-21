NPPAD Curated Dataset — README
===================================

What this is
------------
This ZIP contains a small, curated subset of the NuclearPowerPlantAccidentData (NPPAD).

Important note:
- Dose indicators (DWB, DTHY) are taken directly from the Operation data (same CSV). To be used if needed.

Folder structure
----------------
data/
  02_curated/
    operation/
      scenario=<SCENARIO_NAME>/
        run=<RUN_ID>.csv

Example:
- data/02_curated/operation/scenario=Normal/run=001.csv
- data/02_curated/operation/scenario=LOCA/run=001.csv

There are two scenarios: Normal, LOCA (Loss of Coolant Accident)

Each CSV row represents one timestamp sample.

All curated operation CSVs have the following columns:

1) t_sec
   - Time in seconds from the start of the run.
   - Numeric, increases over the file.

2) P
   - Primary system pressure (reactor coolant system pressure).
   - Used for basic safety/accident detection (e.g., pressure drops).

3) TAVG
   - Average primary coolant temperature.
   - Used to track thermal behavior and heat removal issues.

4) LVPZ
   - Pressurizer level.
   - Indicator of inventory changes and pressurizer behavior.

5) LVCR
   - Core water level (reactor/core coolant level indicator).
   - Useful for detecting loss of core cooling / severity.

6) PWNT
   - Reactor power / neutron power indicator (power proxy).
   - Useful for power changes (trip/shutdown or abnormal power behavior).

7) PRB
   - Containment / reactor building pressure indicator.
   - Useful for containment response during accident scenarios.

8) CNH2
   - Hydrogen concentration indicator.
   - In “Normal” it may be all zeros; may become relevant in certain accidents.

9) RM1
   - Radiation monitor channel 1 (radiation reading).
   - Useful for basic radiation trending and alarms.

10) DWB
   - Whole-body dose rate indicator (summary dose metric).
   - Used for simple dose-related dashboards/alerts.

11) DTHY
   - Thyroid dose rate indicator (summary dose metric).
   - Used for simple dose-related dashboards/alerts.

How to use
----------------
- Choose a scenario/run file and replay rows in time order using t_sec.
- For ingestion (MQTT/Influx/etc.), recommended tags:
  scenario=<scenario>, run=<run>, source=operation
- Fields are all numeric columns except t_sec.

Notes / assumptions
-------------------
- Column names were selected from the original Operation CSV header and curated for a small MVP.
- If we later need more signals, we can extend the selection list and re-run curation.

Scenarios included: [e.g., Normal, LOCA]
Runs included: 001

Meta folder (configuration + audit)
----------------------------------
data/meta/ contains small files that explain how this curated dataset was produced:

1) sensors.yaml
   - The “column selection” configuration used during curation.
   - Lists which signals were kept for each stream (operation).
   - If we want more/less signals later, we can update this file and re-run the curation script.

2) curation_manifest.csv
   - An audit/manifest of the curation output.
   - For each produced file it records:
     - scenario, run, source (operation)
     - input file path (from subset/raw)
     - output file path (in 02_curated)
     - which time column was detected
     - which requested columns were actually found/kept
   - Useful for debugging (e.g., if a scenario is missing a column).
