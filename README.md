# covid-vyroky
Predictions and comments of covid-19 pandemic in the Czech Republic by publicly active people in context of actual data.

## Files
* get_data.py is a python script, that downloads hospitalization statistics from the Internet, loads comments from comments.json and information about their authors from authors.json. Then it uses jinja2 engine to put this data into a template (template.html). This template uses D3.js to visualize the results.
