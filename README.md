# milestones
Discovering cities, one place at a time

What it does
MileStones is a scavenger hunt that takes users from one location to the next, based on user feedback, allowing them to discover and 
explore new places that match their taste. Over the course of a vacation, the user is able to go from destination to destination, earning 
points and achieving milestones along the way! This intelligent app allows the user to explore a new city and enjoy activities that they 
love - with no planning necessary.

How we built it
General Overview: MileStones is built using the Yelp API and Watson Alchemy API, coded up in Python. At a high level, the user inputs their 
location, which is sent to the Yelp API to determine nearby attractions. Next, Watson's Alchemy API helps determine which attractions would 
be most suitable for the user, based on their preferences. The Technical Details: MileStones takes in a pair of geographic coordinates and 
uses the Yelp API to generate a list of URLs corresponding to businesses at or near that location. For each link generated, we use Watson's 
Alchemy API to examine the taxonomy of each page and determine keywords; we then use this information to compile a comprehensive list of 
possible categories. These categories are placed in a dictionary called “ranks” with initial value 0. At the start, we give the user two 
choices from the URLs. After they reach the location they choose, they select whether or not they liked the destination; if they did, the 
location’s categories’ values increase by 1 in ranks. We then identify the category with the max rank and give the user two new options: 
the first link that maps to that same category and another random location.
