#  Enterprise Sales & Customer Analytics

## Business Problem

Fragmented customer, product, order, sales representative and customer interaction data prevents leadership from obtaining a reliable view of revenue performance, customer value, sales effectiveness and conversion.

This project simulates an enterprise analytics environment where data from multiple operational sources must be investigated, standardised and transformed into trusted analytical datasets for business decision-making.

## Dataset Scale

The full synthetic enterprise dataset contains more than 4.6 million records across multiple relational tables.

| Dataset               | Full-scale records |
| --------------------- | -----------------: |
| Customers             |            100,000 |
| Products              |              5,000 |
| Sales Representatives |              2,000 |
| Orders                |          1,000,000 |
| Customer Interactions |          1,000,000 |
| **Total**             |          **4.6M+** |

The full-scale dataset is generated locally using `scripts/generate_data.py` and is intentionally not committed to GitHub because of its size. Representative sample datasets are included in the repository.

## Business Questions

The analysis is designed to answer the following questions:

* Which customers and segments drive the most revenue?
* Which products and categories perform best and worst?
* Where are revenue trends weakening?
* Which customers demonstrate high value or potential retention risk?
* Which sales representatives and regions perform most effectively?
* Where does the customer interaction funnel lose prospects?
* Which data-quality issues could undermine reporting and decision-making?

## Data Quality Investigation

The synthetic generator deliberately introduces realistic enterprise data-quality problems, including:

* Duplicate customer records
* Invalid or broken keys
* Zero and negative quantities
* Discounts exceeding valid thresholds
* Inconsistent status values
* Relational inconsistencies

The project therefore treats data quality as part of the analytical problem rather than assuming the source data is already clean.

## Analytical Workflow

The project follows an end-to-end analytical workflow:

1. Enterprise source data
2. Data profiling and quality investigation
3. SQL investigation and standardisation
4. dbt staging
5. dbt intermediate transformations
6. dbt analytical marts
7. Power BI semantic model
8. Business analysis and decision support

## Analytical Stack

### Python

Used to generate the enterprise-scale synthetic relational dataset and deliberately reproduce realistic data-quality scenarios.

### SQL

Used for data-quality investigation, reconciliation, revenue analysis, customer-value analysis, sales representative performance and interaction-funnel analysis.

### dbt

Used to structure the transformation layer into:

* Staging models
* Intermediate models
* Analytical marts
* Data-quality tests

### Power BI

The analytical layer is designed around an executive semantic model supporting:

1. Executive Overview
2. Revenue and Product Performance
3. Customer Value and Retention Risk
4. Sales Representative Performance
5. Interaction Funnel
6. Data Quality and Trust

### GitHub Actions

Used to support automated project quality checks and maintain repository standards.

## Project Structure

```text
.github/
└── workflows/
    └── quality.yml

data/
├── generated/
│   └── .gitkeep
└── sample/
    ├── customers.csv
    ├── interactions.csv
    ├── orders.csv
    ├── products.csv
    └── sales_reps.csv

dbt/
├── dbt_project.yml
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
└── tests/

docs/
├── architecture.md
├── business_questions.md
├── data_dictionary.md
├── data_quality_strategy.md
├── portfolio_story.md
└── images/
    └── enterprise-sales-customer-analytics.png

powerbi/
├── dashboard_wireframe.md
├── measures.md
└── semantic_model.md

scripts/
└── generate_data.py

sql/
├── 01_data_quality.sql
├── 02_revenue_performance.sql
├── 03_customer_value.sql
├── 04_sales_rep_performance.sql
├── 05_interaction_funnel.sql
└── 06_data_quality_reconciliation.sql
```

## Reproducibility

The documented enterprise-scale generation command is:

```bash
python scripts/generate_data.py --scale-factor 1.0
```

For development and testing, a smaller scale factor can be used to generate a reduced dataset.

Generated enterprise-scale files are excluded from version control through `.gitignore`.

## Portfolio Focus

This project demonstrates an end-to-end approach to solving an enterprise analytics problem:

**Investigate → Validate → Transform → Model → Analyse → Communicate**

Rather than focusing only on dashboard creation, the project demonstrates how an analyst can move from fragmented operational data and data-quality problems toward trusted analytical outputs and business decision support.

![Enterprise Sales & Customer Analytics](docs/images/enterprise-sales-customer-analytics.png)

<img width="1376" height="768" alt="enterprise-sales-customer-analytics" src="https://github.com/user-attachments/assets/8e2c922e-001f-4374-a355-78a1b9f34015" />
