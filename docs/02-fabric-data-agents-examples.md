# Examples for Fabric Data Agents Guidance

You can improve the accuracy of Fabric data agent responses by providing example queries specific to each data source, such as lakehouses, warehouses, or KQL databases. This technique, known as Few-Shot Learning in generative AI, helps guide the agent to produce answers that more closely match your expectations.

Power BI semantic model data don't support adding sample query/question pairs at this time.

## Golden Dataset

Based on the Factory team's best practices, we recommend preparing at least 30 SQL pairs that include natural language questions and corresponding SQL queries to effectively guide the agent's responses.

| Question (Prompt)                                  | Expected SQL Query                                                                                                                           | Expected Output |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| How many green taxi trips that took place in 2019? | SELECT COUNT(*) AS total_green_taxi_trips_2019 FROM [year_2019].[green_tripdata_2019];                                                       | 13              |
| What percentage of trips include a tip in 2021?    | SELECT COUNT(CASE WHEN tip_amount > 0 THEN 1 END) * 100.0 / COUNT(*) AS pct_tipped FROM [year_2021].[green_tripdata_2021];                   | B2              |
| What are the longest trips by distance in 2022?    | SELECT TOP 10 trip_distance, lpep_pickup_datetime, lpep_dropoff_datetime FROM [year_2022].[green_tripdata_2022] ORDER BY trip_distance DESC; | C3              |


# Additional Resources

1. [Fabric data agent scenario (preview) - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial#provide-examples)