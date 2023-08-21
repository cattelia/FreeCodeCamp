#Multi-Step Data Analysis
'''
Data Source -> Gather -> Raw Data -> Clean/Process  -> Visualize
                                                    -> Analyze

                                                    
Hadoop.apache.org
Spark.apache.org
AWS.amazon.com/redshift
community.pentaho.com
'''

'''
GEO Data

- Makes a Google Map from User Entered
- Uses the Google GEOData API
- Caches the data in a DB to avoid rate limiting and allow restarting
- Visualize in a browser using Google Maps API
'''
#The flow
#Google geodata -(geoload.py)-> geodata.sqlite -> geodump.py -> where.js -(visualize)-> where.html

#Page Rank
'''
Write a simple web page crawler
Compute a simple version of Google's Page Rank Algorithm
Visualize the resulting network
'''

#Web Crawler
'''
Retrieve a page
Look through the page for links
Add the links to a list of "to be retrieved" sites
Repeat...
'''

