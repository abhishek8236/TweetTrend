# TweetTrend

A Project to stream the tweeter data to s3\localdirectory\kafka\kinesis and analyze the trend using spark (batch) or spark-streaming (realtime).

## Prerequisites:
* Tweeter dev-account with credentials to access twitter APIs (consumer key-secret, access token-secret)

* AWS account and user with secret id-key and required roles

* Python + tweepy preinstalled  (if pip installed: ‘pip install tweepy’)

* Spark cluster

* Hadoop cluster if plan to use Hive, Pig


## Steps:
* Using Nifi or tweepy to stream the data to one of the mentioned storage location (Depending on batch or real-time analyzation)

* Choose the right tool to analyze the trend depending on the requirement, infrastructure, cost etc.

* Use a BI tool, APIs or Micro services to analyze the trend or integrate it with any 3rd party applications
