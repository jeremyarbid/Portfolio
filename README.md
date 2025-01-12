# Project Summary
The BTC Price Tracker project is designed to track Bitcoin prices and store the data in a PostgreSQL database, with a setup to automate data collection via Python scripts and GitHub integration. The goal is to keep track of Bitcoin price movements over time and allow for easy updates, pushing code changes to a GitHub repository, and leveraging automated cron jobs for periodic updates.

#### Bitcoin Price Data Collection:
Python scripts were created to fetch Bitcoin price data from an API and store it in a PostgreSQL database.
#### PostgreSQL Database: 
The btc_prices table was created to store Bitcoin price data along with a date_key field for easy querying.
The calendar table was created to normalize date-related data for easier querying and analysis.
#### Cron Job Setup: 
A cron job was set up to automate the running of the Python script at a scheduled time each day, ensuring the database is updated regularly with the latest Bitcoin prices.
#### GitHub Repository: 
A GitHub repository was created to host the project. This includes all the scripts, SQL files, and configuration settings.
#### Environment Variable for Directory Path: 
The project was made portable by storing the project directory path in an environment variable, allowing the script to be reused without hardcoding paths.
