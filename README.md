# Identifying Events based on keyword search using Twitter Data

Our goal is to build an application to find and display information regarding sports events specific to a keyword search performed by an end user operating the application.After identifying
the cricket sport events occurring in a given locality, the events are to be classified into groups based on the positive and negative tweets from the users. Data sets containing tweet
data for cricket sport events are collected and filtered based on the keywords that would be used to derive a solution. Twitter API can be used to implement the feature of extracting real
time data by that could be used to get the information of the events the end-user is trying to access.

In the end user application, we would allow the user to enter a query for a selected location of the user and perform a search regarding the event they will be targeting to know the results
about. Once they submit the query, the results from specific event will be fetched after performing relevant operations by developing an ontology. These events will be based on recently
generated twitter data and would be picked from the real-time available data. Finally, the query results would be classified into two groups on how audience around are discussing on
the trends(positive or negative) and are published to the end users that would let them infer upon the opinion of the people discussing about the selected event.

In the end goal, we planned to query the results with one click of a button. We have added on click to filter different types of queries. So one click of a button will fire different
queries in SparkQl and the output will be the results in a tabular format related to the queries. The output will be filtered from different categories and those categories are runs,
tournaments, players, country teams, league teams, and dates. Hence the output will be filtered based on different keywords and those keywords will be used to return or represent the rdf
triples from our ontology, and instances from ontology will be filtered using SparkQl.
