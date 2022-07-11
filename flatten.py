import json
import pandas as pd
import json

pd.read_json

with open("data/frostangela.json", "r") as f:
    json_string = json.load(f)
    flattended_data = pd.json_normalize(json_string)
    flattended_data = flattended_data.explode("website").reset_index(drop=True)
    print(flattended_data)