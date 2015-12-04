"""
Use this script to strip out unwanted rows from the WDI sheet from the WB website
"""
from octopus.lib import paths
import csv, codecs

d = paths.rel2abs(__file__, "..", "..", "data", "wbwdi", "WDI_csv", "WDI_Data.csv")
o = paths.rel2abs(__file__, "..", "..", "data", "wbwdi", "wbwdi_selected.csv")

KEEP = [
    "Access to electricity (% of population)",
    "Adjusted net national income per capita (current US$)",
    "Adolescent fertility rate (births per 1,000 women ages 15-19)",
    "Agricultural land (sq. km)",
    "Alternative and nuclear energy (% of total energy use)",
    "Armed forces personnel, total",
    "Average precipitation in depth (mm per year)",
    "Birth rate, crude (per 1,000 people)",
    "CO2 emissions (metric tons per capita)",
    "Death rate, crude (per 1,000 people)",
    "Electric power consumption (kWh per capita)",
    "GDP (current US$)",
    "Land area (sq. km)",
    "Life expectancy at birth, total (years)",
    "Population growth (annual %)"
]

with codecs.open(o, "wb") as out:
    writer = csv.writer(out)
    with codecs.open(d) as f:
        reader = csv.reader(f)
        first = True
        for row in reader:
            if first:
                writer.writerow(row)
                first = False
                continue
            if row[2] in KEEP:
                writer.writerow(row)
