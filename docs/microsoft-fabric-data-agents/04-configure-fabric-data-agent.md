- [Chat with your data using Microsoft Fabric data agents](#chat-with-your-data-using-microsoft-fabric-data-agents)
  - [What you’ll learn](#what-youll-learn)
  - [Before you start](#before-you-start)
  - [Exercise scenario](#exercise-scenario)
  - [Instructions for Fabric Data Agents Guidance](#instructions-for-fabric-data-agents-guidance)
    - [Prompts](#prompts)
  - [Data Source Description for Fabric Data Agents Guidance](#data-source-description-for-fabric-data-agents-guidance)
    - [Example](#example)
  - [Examples for Fabric Data Agents Guidance](#examples-for-fabric-data-agents-guidance)
    - [Golden Dataset](#golden-dataset)
  - [Additional Resources](#additional-resources)


# Chat with your data using Microsoft Fabric data agents

![opening](../../media/lab-00-opening.webp)

A Microsoft Fabric data agent enables natural interaction with your data by allowing you to ask questions in plain English and receive structured, human-readable responses. By eliminating the need to understand query languages like SQL (Structured Query Language), DAX (Data Analysis Expressions), or KQL (Kusto Query Language), the data agent makes data insights accessible across the organization, regardless of technical skill level.

This exercise should take approximately less than **10** minutes to complete.

## What you’ll learn

By completing this lab, you will:

* Understand the purpose and benefits of Microsoft Fabric data agents for natural language data analysis.
* Learn how to create and configure a Fabric workspace and data warehouse.
* Gain hands-on experience loading and exploring a star schema sales dataset.
* See how data agents translate plain English questions into SQL queries.
* Develop skills to ask effective analytical questions and interpret AI-generated results.
* Build confidence in leveraging AI tools to democratize data access and insights.

## Before you start

You need a **Microsoft Fabric Capacity (F2 or higher)** with Copilot enabled to complete this exercise.

## Exercise scenario

We will create a sales data warehouse, load some data into it and then create a Fabric data agent. We will then ask it a variety of questions and explore how the data agent translates natural language into SQL queries to provide insights. This hands-on approach will demonstrate the power of AI-assisted data analysis without requiring deep SQL knowledge. Let’s start!

## Instructions for Fabric Data Agents Guidance

You can provide specific instructions to guide the AI’s behavior, helping it better understand how to interpret and respond to queries. Any predefined examples (for example, sample questions and answers) or specific instructions, help refine the AI's understanding of the question, and guide how the AI interacts with the data. You can write up to 15,000 characters in plain English-language text.

To add instructions, click the Data agent instructions button to open the instructions pane on the right. Apply the following prompt with any database to guide the desired behavior.

### Prompts

- You are a senior data analyst and SQL expert specializing in [XXX] data, responsible for translating natural language questions into accurate, executable SQL queries for the [XXX] database. The data source contains the following tables: [Table Name] (brief description), with no additional tables or columns beyond the provided schema. Correctly infer user intent, including metrics, filters, time ranges, aggregations, and necessary joins, applying standard SQL best practices with clear aliases and explicit JOIN conditions while avoiding SELECT * unless explicitly requested. If a request is ambiguous, make reasonable analytical assumptions and reflect them in your explanation. For every request, return three items: (1) Logic Brief — one sentence describing key filters, joins, or assumptions; (2) SQL Query — a clean, readable, and fully executable SQL statement; and (3) Interpretation — a brief analyst-style explanation of what the results represent, including the unit of analysis and business meaning.

## Data Source Description for Fabric Data Agents Guidance

Describe what's in this data source, what it represents, and why someone might use it to answer a question.

### Example

```
- VendorID: Vendor identifier.
- lpep_pickup_datetime: Trip start time.
- lpep_dropoff_datetime: Trip end time.
- store_and_fwd_flag: Delayed transmission flag.
- RatecodeID: Fare rate code.
- PULocationID: Pickup zone ID.
- DOLocationID: Drop-off zone ID.
- passenger_count: Passenger count.
- trip_distance: Distance in miles.
- fare_amount: Base fare.
- extra: Surcharges.
- mta_tax: MTA tax.
- tip_amount: Card tip.
- tolls_amount: Tolls.
- ehail_fee: E-hail fee.
- improvement_surcharge: System surcharge.
- total_amount: Total fare.
- payment_type: Payment method.
- trip_type: Hail type.
- congestion_surcharge: Congestion fee.
- source_file: Source file name.
```

## Examples for Fabric Data Agents Guidance

You can improve the accuracy of Fabric data agent responses by providing example queries specific to each data source, such as lakehouses, warehouses, or KQL databases. This technique, known as Few-Shot Learning in generative AI, helps guide the agent to produce answers that more closely match your expectations.

Power BI semantic model data don't support adding sample query/question pairs at this time.

### Golden Dataset

Based on the Factory team's best practices, we recommend preparing at least 30 SQL pairs that include natural language questions and corresponding SQL queries to effectively guide the agent's responses.

| Question (Prompt)                                  | Expected SQL Query                                                                                                                           | Expected Output |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| How many green taxi trips that took place in 2019? | SELECT COUNT(*) AS total_green_taxi_trips_2019 FROM [year_2019].[green_tripdata_2019];                                                       | 13              |
| What percentage of trips include a tip in 2021?    | SELECT COUNT(CASE WHEN tip_amount > 0 THEN 1 END) * 100.0 / COUNT(*) AS pct_tipped FROM [year_2021].[green_tripdata_2021];                   | B2              |
| What are the longest trips by distance in 2022?    | SELECT TOP 10 trip_distance, lpep_pickup_datetime, lpep_dropoff_datetime FROM [year_2022].[green_tripdata_2022] ORDER BY trip_distance DESC; | C3              |


## Additional Resources

1. [Fabric data agent scenario (preview) - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial)
2. [Chat with your data using Microsoft Fabric data agents | mslearn-fabric](https://microsoftlearning.github.io/mslearn-fabric/Instructions/Labs/22d-copilot-fabric-data-agents.html#create-a-workspace)