---   www.se-data.co.uk   ---
"# se-app" 
This web app is brought to you by Bartosz Bobnis

This app created as personal coding project is handled by Python on the back- end using Flask, Bokeh and Pandas libraries demonstrating their versatile possibilities. Each search is dynamically processed and data is uniquely gathered from Yahoo Finance via Pandas Datareader module. Front end has been written in HTML and styled in CSS manually.

Data used for this project was scraped from the web using beautiful soup and is stored in SQL database. All data concerning actual S&P 500 list used by this web app is dynamically quoted from database using SQLite.

Some of the HTML templates are created dynamically by functions depending on user input- like drop-down template which is edited and saved
on the server before rendering for each quote- function finds the difference between input and existing template and replaces markers with
data generated from database, ready to use in drop-down menu. Variables are managed by Flask-Sessions and error handling is based on
"try-except" blocks returning user to the last possible point in case of pressing "refresh" or "go back" button which otherwise would 
result in crashing as well as other related errors.
