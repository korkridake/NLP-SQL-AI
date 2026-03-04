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
- [📈 1. Revenue Concentration \& Pareto Analysis](#-1-revenue-concentration--pareto-analysis)
    - [❓ Executive Question:](#-executive-question)
- [💰 2. Revenue Per Zone Contribution](#-2-revenue-per-zone-contribution)
    - [❓ Executive Question:](#-executive-question-1)
- [🚕 3. Profitability Per Mile by Time of Day](#-3-profitability-per-mile-by-time-of-day)
    - [❓ Executive Question:](#-executive-question-2)
- [📊 4. High-Value Customer Behavior (Proxy via Tip Rate)](#-4-high-value-customer-behavior-proxy-via-tip-rate)
    - [❓ Executive Question:](#-executive-question-3)
- [📆 5. Weekday vs Weekend Performance](#-5-weekday-vs-weekend-performance)
    - [❓ Executive Question:](#-executive-question-4)
- [🔥 6. Peak Congestion Impact](#-6-peak-congestion-impact)
    - [❓ Executive Question:](#-executive-question-5)
- [📉 7. Revenue Volatility Analysis](#-7-revenue-volatility-analysis)
    - [❓ Executive Question:](#-executive-question-6)
- [🏆 8. Top Revenue Routes (Weighted by Profitability)](#-8-top-revenue-routes-weighted-by-profitability)
    - [❓ Executive Question:](#-executive-question-7)
- [📦 9. Customer Spend Distribution (Percentiles)](#-9-customer-spend-distribution-percentiles)
    - [❓ Executive Question:](#-executive-question-8)
- [🚦 10. Driver Productivity Proxy (Trips per Active Hour)](#-10-driver-productivity-proxy-trips-per-active-hour)
    - [❓ Executive Question:](#-executive-question-9)
- [🧠 11. Cannibalization Risk Analysis](#-11-cannibalization-risk-analysis)
    - [❓ Executive Question:](#-executive-question-10)
- [📈 12. Long-Term Trend \& Seasonality](#-12-long-term-trend--seasonality)
    - [❓ Executive Question:](#-executive-question-11)
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
| How many green taxi trips that took place in 2019? | SELECT COUNT(*) AS total_green_taxi_trips_2019 FROM [year_2019].[green_tripdata_2019];                                                       | 6,300,814              |
| What percentage of trips include a tip in 2021?    | SELECT COUNT(CASE WHEN tip_amount > 0 THEN 1 END) * 100.0 / COUNT(*) AS pct_tipped FROM [year_2021].[green_tripdata_2021];                   | 34.430711621000              |
| What are the longest trips by distance in 2022?    | SELECT TOP 1 trip_distance, lpep_pickup_datetime, lpep_dropoff_datetime FROM [year_2022].[green_tripdata_2022] ORDER BY trip_distance DESC; | 360068.14	          |
| Which drop-off zones generate the highest revenue? | SELECT DOLocationID, SUM(total_amount) AS total_revenue FROM [year_2019].[green_tripdata_2019] GROUP BY DOLocationID ORDER BY total_revenue DESC; |  74            |

# 📈 1. Revenue Concentration & Pareto Analysis

### ❓ Executive Question:

**What percentage of total revenue comes from the top 10% highest-grossing trips?**

```sql
WITH ranked_trips AS (
    SELECT total_amount,
           NTILE(10) OVER (ORDER BY total_amount DESC) AS revenue_decile
    FROM nyc_taxi
)
SELECT 
    SUM(CASE WHEN revenue_decile = 1 THEN total_amount END) 
        / SUM(total_amount) * 100 AS pct_revenue_top_10_percent
FROM ranked_trips;
```

👉 Shows revenue concentration risk.

---

# 💰 2. Revenue Per Zone Contribution

### ❓ Executive Question:

**Which pickup zones contribute most to total company revenue, and what is their cumulative contribution?**

```sql
WITH zone_revenue AS (
    SELECT PULocationID,
           SUM(total_amount) AS revenue
    FROM nyc_taxi
    GROUP BY PULocationID
),
ranked AS (
    SELECT *,
           SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_revenue,
           SUM(revenue) OVER () AS total_revenue
    FROM zone_revenue
)
SELECT PULocationID,
       revenue,
       cumulative_revenue / total_revenue * 100 AS cumulative_pct
FROM ranked
ORDER BY revenue DESC;
```

👉 Identifies geographic dependency.

---

# 🚕 3. Profitability Per Mile by Time of Day

### ❓ Executive Question:

**During which hours are trips most profitable per mile?**

```sql
SELECT EXTRACT(HOUR FROM lpep_pickup_datetime) AS hour,
       AVG(total_amount / NULLIF(trip_distance, 0)) AS avg_revenue_per_mile
FROM nyc_taxi
GROUP BY hour
ORDER BY avg_revenue_per_mile DESC;
```

👉 Supports surge pricing or driver allocation strategy.

---

# 📊 4. High-Value Customer Behavior (Proxy via Tip Rate)

### ❓ Executive Question:

**Do longer trips result in higher tip percentages?**

```sql
SELECT 
    CASE 
        WHEN trip_distance < 2 THEN 'Short (<2mi)'
        WHEN trip_distance < 5 THEN 'Medium (2-5mi)'
        ELSE 'Long (>5mi)'
    END AS distance_bucket,
    AVG(tip_amount / NULLIF(fare_amount, 0)) * 100 AS avg_tip_pct
FROM nyc_taxi
GROUP BY distance_bucket;
```

👉 Helps optimize pricing tiers.

---

# 📆 5. Weekday vs Weekend Performance

### ❓ Executive Question:

**How does revenue and trip volume differ between weekdays and weekends?**

```sql
SELECT 
    CASE 
        WHEN EXTRACT(DOW FROM lpep_pickup_datetime) IN (0,6) 
        THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    COUNT(*) AS trip_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_revenue_per_trip
FROM nyc_taxi
GROUP BY day_type;
```

👉 Operational staffing optimization.

---

# 🔥 6. Peak Congestion Impact

### ❓ Executive Question:

**What percentage of total revenue comes from congestion surcharges?**

```sql
SELECT 
    SUM(congestion_surcharge) AS total_congestion_fees,
    SUM(congestion_surcharge) / SUM(total_amount) * 100 AS pct_of_total_revenue
FROM nyc_taxi;
```

👉 Regulatory dependency exposure.

---

# 📉 7. Revenue Volatility Analysis

### ❓ Executive Question:

**What is the day-to-day revenue growth rate?**

```sql
WITH daily_revenue AS (
    SELECT DATE(lpep_pickup_datetime) AS trip_date,
           SUM(total_amount) AS revenue
    FROM nyc_taxi
    GROUP BY trip_date
)
SELECT trip_date,
       revenue,
       (revenue - LAG(revenue) OVER (ORDER BY trip_date)) 
           / LAG(revenue) OVER (ORDER BY trip_date) * 100 
           AS daily_growth_pct
FROM daily_revenue
ORDER BY trip_date;
```

👉 Detects sudden drops or spikes.

---

# 🏆 8. Top Revenue Routes (Weighted by Profitability)

### ❓ Executive Question:

**Which routes generate the highest average revenue per trip and have meaningful volume?**

```sql
SELECT PULocationID,
       DOLocationID,
       COUNT(*) AS trip_count,
       AVG(total_amount) AS avg_revenue,
       SUM(total_amount) AS total_revenue
FROM nyc_taxi
GROUP BY PULocationID, DOLocationID
HAVING COUNT(*) > 100
ORDER BY avg_revenue DESC
LIMIT 10;
```

👉 Strategic route targeting.

---

# 📦 9. Customer Spend Distribution (Percentiles)

### ❓ Executive Question:

**What are the 50th, 75th, and 95th percentile trip revenues?**

(PostgreSQL)

```sql
SELECT
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY total_amount) AS p50,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_amount) AS p75,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_amount) AS p95
FROM nyc_taxi;
```

👉 Pricing segmentation insight.

---

# 🚦 10. Driver Productivity Proxy (Trips per Active Hour)

### ❓ Executive Question:

**What is the average number of trips per active hour?**

```sql
WITH hourly_trips AS (
    SELECT DATE_TRUNC('hour', lpep_pickup_datetime) AS hour,
           COUNT(*) AS trips
    FROM nyc_taxi
    GROUP BY hour
)
SELECT AVG(trips) AS avg_trips_per_hour
FROM hourly_trips;
```

👉 Supply-demand balance.

---

# 🧠 11. Cannibalization Risk Analysis

### ❓ Executive Question:

**Are short trips disproportionately contributing to congestion but low revenue?**

```sql
SELECT 
    COUNT(*) FILTER (WHERE trip_distance < 1) * 100.0 / COUNT(*) 
        AS pct_short_trips,
    SUM(total_amount) FILTER (WHERE trip_distance < 1) 
        / SUM(total_amount) * 100 AS pct_revenue_from_short_trips
FROM nyc_taxi;
```

👉 Urban planning implications.

---

# 📈 12. Long-Term Trend & Seasonality

### ❓ Executive Question:

**Is there monthly seasonality in revenue?**

```sql
SELECT DATE_TRUNC('month', lpep_pickup_datetime) AS month,
       SUM(total_amount) AS revenue
FROM nyc_taxi
GROUP BY month
ORDER BY month;
```

👉 Budget forecasting.

## Additional Resources

1. [Fabric data agent scenario (preview) - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial)
2. [Chat with your data using Microsoft Fabric data agents | mslearn-fabric](https://microsoftlearning.github.io/mslearn-fabric/Instructions/Labs/22d-copilot-fabric-data-agents.html#create-a-workspace)