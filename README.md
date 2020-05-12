# Covid-19-project
This program can give you stats about the cases in a particular country OR.... 
Take keywords as input and the country name and scrape the search results keyword by keyword.
All the headings and descriptions of the search results are stored in a table using the 'plotly' module.
I tried integrating the links in the plotly table but it seems it is not made for links. Apparantly people over the internet also face the same issue.
But the links are printed below the table with indices. 
Then it opens each link one by one and checks all the paragraphs for any relevent keywords.
if found, the paragraphs are extracted and then stored in a '.txt' file.



That's it till now.
