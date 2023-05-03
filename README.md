# LA-traffic-Project
I am analyzing Highways that area I took the most often this year, that is from Downtown/Irvine to Riverside, focused on i10, 60, 71, 91.

With the PeMS, I can find average speed for each lane for each highways, in a given time. With LA collision data, I can find information of traffic accidents.

The main script is runnable from the
command line with 3 different inputs:
**Install Python first
You can run the project by
1. python scraper.py
The script invocation without input arguments just prints (to standard
output) the complete scraped dataset as rows of data.
2. python scraper.py –-scrape N
This script invocation with the flag --scrape N prints (to standard output)
the first N entries of the dataset.
3. python scraper.py --save <path_to_dataset>
This script invocation saves the complete scraped dataset into the file
passed as input (<path_to_dataset> is just a placeholder for the path to
the file). Sample invocations could be:
scraper.py –-save my_scraped_data.csv
scraper.py -–save dir1/dir2/football_stats.csv
4. python scraper.py --viz
This script would produce the visualization of graph of average speed for each lane.



Project proposal:

Datasets related to traffic in the Los Angeles area:
https://pems.dot.ca.gov/

Scrape data set: Los Angeles Traffic Speeds
The California Department of Transportation (Caltrans) provides real-time traffic speed data
for major highways and freeways in the state of California through its Performance Monitoring
System (PeMS). We can scrape this data from the Los Angeles region to collect information on
traffic speeds, congestion levels, and travel times. By analyzing this data, we can identify
congested areas and peak travel times, understand the impact of weather and events on traffic
patterns, and develop predictive models to help reduce congestion. I have already registered
account for this website/

API data set: Google Maps Traffic API
Google Maps provides an API for real-time traffic information, which includes data on traffic
speeds, congestion, and incidents. We can access this data for the Los Angeles area to analyze
traffic patterns, identify areas with high levels of congestion, and develop predictive models to
help prevent traffic accidents.

https://data.lacity.org/Public-Safety/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w
CSV data set: Los Angeles Traffic Collision Data
The City of Los Angeles provides data on traffic collisions that occurred within the city from
2010 to present in CSV format. This data includes information on the location, time, and
individuals. By analyzing this data, we can identify high-traffic areas with high collision rates
and develop predictive models to help prevent future accidents.
By combining the above datasets, we can analyze how traffic speeds and congestion levels are
related to traffic collisions and how they affect each other in the Los Angeles area. For example,
we can study how traffic patterns and congestion affect the likelihood of traffic accidents, and
how traffic accidents impact traffic flow and congestion. We can also develop predictive models
to identify areas with high levels of traffic congestion and accidents and suggest solutions to
improve traffic flow and reduce accidents. Another possible analysis is to look at the
relationship between traffic patterns and air pollution to understand how transportation choices
affect environmental health in Los Angeles.
