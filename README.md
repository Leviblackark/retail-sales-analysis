# Retail Sales Analysis

### Project Overview

This project analyses sales transaction data from a fictional coffee shop business operating across three store locations.

The aim is to investigate product performance, daily sales trends and differences in sales performance between stores. 

SQL, Python (pandas), Excel and Power BI will be used throughout the project to explore, process, analyse and visualise the data, demonstrating how these tools can work together in a data analysis workflow.

The final goal is to develop an interactive dashboard and present key findings that could help the business better understand its sales performance.

### Core Analysis

| Analysis Area | Business Question |
| --- | --- |
| Product Performance | Which products generate the highest and lowest sales revenue, and how does their performance change during the reporting period? |
| Sales Trends | Which days generate the highest and lowest sales revenue, and are there recurring patterns in daily sales? |
| Store Performance | How does sales performance vary between stores and geographical locations? |

### Future Extensions

| Analysis Area | Business Question | 
| --- | --- |
| Operating Costs | How do monthly operating costs compare with sales revenue, and how does the relationship change throughout the year? |
| Staffing Efficiency | How many hours are worked by staff relative to sales revenue, and how does this vary across stores and time periods? |

## Dataset
```mermaid
flowchart LR
    A[data/] --> B[raw/]
    B --> C[Coffee Shop sale.xlsx]

    A --> D[processed/]
```


**Name:** Coffee Shop Sales <br>
**Source:** Maven Analytics <br>
**Business:** Maven Roasters (fictional) <br>
**Reporting period:** January–June 2023 <br>
**License:** Public Domain <br>
**Original format:** Excel (.xlsx)

## Tools and Technologies

This project displays use of these tools:
```mermaid
flowchart TD
    A[Raw Excel Dataset] --> B[SQL / SQLite]
    B --> C[Python / pandas]
    C --> D[Excel]
    C --> E[Power BI]
    D --> F[Business Insight]
    E --> F
```
## Project Status


In progress - Initial project setup and dataset preparation. SQL analysis, Python exploration, Excel reporting and Power BI dashboard development will be completed in subsequent stages 