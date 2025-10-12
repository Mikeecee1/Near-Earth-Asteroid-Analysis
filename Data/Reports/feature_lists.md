# Feature lists and inferred data types

This document lists the columns present in the processed CSVs and their inferred data types. Names are backticked so you can copy/paste into README or docs.

## `Data/Processed/observations.csv`
- `name` — string
- `est_diameter_min` — float
- `est_diameter_max` — float
- `relative_velocity` — float
- `miss_distance` — float
- `absolute_magnitude` — float
- `hazardous` — boolean (True/False)
- `observations` — integer

Notes:
- `name` is the object identifier (string). 
- `hazardous` is a boolean label from the source; confirm mapping if you need integers (0/1).

## `Data/Processed/features.csv`
- `name` — string
- `est_diameter_min` — float
- `est_diameter_max` — float
- `relative_velocity_mean` — float
- `miss_distance_mean` — float
- `miss_distance_min` — float
- `absolute_magnitude_mean` — float
- `hazardous` — boolean
- `observations` — integer
- `est_diameter_range` — float
- `est_diameter_mean` — float
- `est_diameter_min_log1p` — float
- `est_diameter_max_log1p` — float
- `est_diameter_mean_log1p` — float
- `est_diameter_range_log1p` — float
- `relative_velocity_mean_log1p` — float
- `miss_distance_mean_log1p` — float
- `miss_distance_min_log1p` — float
- `hazardous_enc` — integer (0/1 encoding)

Notes:
- `_log1p` columns were added to reduce skew; they are numeric floats.
- `hazardous_enc` is a numeric encoding of the boolean `hazardous` field (0/1).

## `Data/Processed/features_model.csv`
- `name` — string
- `est_diameter_min` — float
- `est_diameter_max` — float
- `relative_velocity_mean` — float
- `miss_distance_mean` — float
- `miss_distance_min` — float
- `absolute_magnitude_mean` — float
- `hazardous` — boolean
- `observations` — integer
- `est_diameter_range` — float
- `est_diameter_mean` — float
- `est_diameter_min_log1p` — float
- `est_diameter_max_log1p` — float
- `est_diameter_mean_log1p` — float
- `est_diameter_range_log1p` — float
- `relative_velocity_mean_log1p` — float
- `miss_distance_mean_log1p` — float
- `miss_distance_min_log1p` — float
- `hazardous_enc` — integer (0/1)
- `diameter_class` — categorical / ordinal (e.g., `small`, `medium`, `large`)
- `proximity_class` — categorical / ordinal (e.g., `close`, `medium`, `distant`, `very_distant`)
- `velocity_class` — categorical (e.g., `slow`, `moderate`, `fast`)
- `brightness_class` — categorical (e.g., `dim`, `moderate`, `bright`)
- `observation_class` — categorical / ordinal (e.g., `single`, `few`, `some`, `many`)

Notes:
- The class columns are human-friendly categorical bins created during modelling preprocessing. If you need numeric ordinal encodings (0..N) or one-hot encodings for model input, let me know and I can export a version with encodings applied.

---

If you'd like, I can also:
- produce exact pandas dtypes for each CSV (quick dtype report), or
- add a small snippet showing how to load each CSV and print dtypes (for reproducibility).
