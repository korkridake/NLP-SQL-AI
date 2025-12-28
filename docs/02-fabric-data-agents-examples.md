# Examples for Fabric Data Agents Guidance

You can improve the accuracy of Fabric data agent responses by providing example queries specific to each data source, such as lakehouses, warehouses, or KQL databases. This technique, known as Few-Shot Learning in generative AI, helps guide the agent to produce answers that more closely match your expectations.

Power BI semantic model data don't support adding sample query/question pairs at this time.

## Golden Dataset

| Question (Prompt)                                  | Expected SQL Query                                                                     | Expected Output |
|----------------------------------------------------|----------------------------------------------------------------------------------------|-----------------|
| How many green taxi trips that took place in 2019? | SELECT COUNT(*) AS total_green_taxi_trips_2019 FROM [year_2019].[green_tripdata_2019]; | 13              |
| A2                                                 | B2                                                                                     | C2              |
| A3                                                 | B3                                                                                     | C3              |



# Additional Resources

1. [Fabric data agent scenario (preview) - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial#provide-examples)