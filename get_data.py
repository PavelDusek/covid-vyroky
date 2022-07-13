# coding: utf-8
import pandas as pd
import datetime
import jinja2
import json

#Get data
#Data licence: https://data.gov.cz/podm%C3%ADnky-u%C5%BEit%C3%AD/voln%C3%BD-p%C5%99%C3%ADstup/
df = pd.read_csv("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.csv")

#Prepare, clean and format data
df = df[['datum', 'pocet_hosp', 'stav_tezky', 'tezky_upv_ecmo', 'jip', 'kyslik', 'hfno', 'upv', 'ecmo', 'umrti', 'kum_umrti']]
df['datum'] = pd.to_datetime(df['datum'])
df = df.loc[ ( df['datum'] >= datetime.datetime(2020, 3, 10) ) & (df['datum'] <= datetime.datetime(2020, 10, 12) ) ]
df.fillna(0, inplace=True)
data = [
        {
            "datum": datetime.datetime.strftime(row["datum"], "%d.%m.%Y"),
            "pocet_hosp": row["pocet_hosp"],
            "stav_tezky": row["stav_tezky"]
        }
            for i, row in df.iterrows()
    ]

#Put data into D3.js template
with open("template.html") as f:
    template_html = f.read()
with open("comments.json") as f:
    j = f.read()
comments = json.loads(j)
with open("authors.json") as f:
    j = f.read()
authors = json.loads(j)

template = jinja2.Template(template_html)
html = template.render(data = data, comments = comments, authors = authors)
with open("index.html", "w") as f:
    f.write(html)
