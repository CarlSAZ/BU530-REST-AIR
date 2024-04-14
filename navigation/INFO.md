# Design Information for the Navigation Module

The navigation module is built in part with Google Maps API in mind. The design paradigm of
an atomic step is kept, but the fields are changed to focus on information needed for an
automonomous car.
MIT: 42.3660286, -71.092396

## Journey

| Field | Type | Example Value | Description |
| ----- | ---- | ------------- | ----------- |
| ID    | int  | 32       | Unique Id for step direction |
| start_lat | float64 | 42.349343 | Latitude of start waypoint |
| start_lon | float64 | -71.105887| Longitude of start waypoint|
| start_heading | float64 | 90      | Approximate global true compass heading at start of direction step |
| end_lat   | float64 | 42.3660286 | Latitude of end waypoint |
| end_lon   | float64   | -71.092396 | Longitude of end waypoint |
| end_heading | float64 | 180 | Desired Heading at end of maneuver |
| distance_km | float64 | 0.5   | Approx distance along path |
| Description | string  | "Take a right turn onto Whitmore St." | Human readable instruction for accountability |
| Status    | float | 3.141159 | rank of last completed step |

## Direction to Journey Mapping

| Field | Type | Example Value | Description |
| ----- | ---- | ------------- | ----------- |
| Journey_ID | int | 32 | Journey ID |
| step_type | string | "Direction" | Either "Journey" or "Direction", allows for mini-journeys to be added |
| step_ID | int | 87654321 | Direction ID |
| step_rank | float | 3.23 | Position within Journey steps, i.e. step 2.71828 occurs before step 3.14159 |

## Direction Step

| Field | Type | Example Value | Description |
| ----- | ---- | ------------- | ----------- |
| ID    | int  | 87654321       | Unique Id for step direction |
| start_lat | float64 | 42.349343 | Latitude of start waypoint |
| start_lon | float64 | -71.105887| Longitude of start waypoint|
| start_heading | float64 | 90      | Approximate global true compass heading at start of direction step |
| end_lat   | float64 | 42.349337 | Latitude of end waypoint |
| end_lon   | float64   | -71.105133 | Longitude of end waypoint |
| end_heading | float64 | 0 | Desired Heading at end of maneuver |
| local_path_m  | array   | [[0,0],[0,1],...] | Expected path on local scale to follow, if available (e.g. path to take within intersection) |
| distance_km | float64 | 0.5   | Approx distance along path |
| Maneuver    | string  | "turn-left" | General description of maneuver, see implemented list of behaviours |
| Road_Type     | string | "Dirt"   | Flag to determine road type ("Street", "Dirt", "Off-Road") |
| Description | string  | "Take a right turn onto Whitmore St." | Human readable instruction for accountability |
