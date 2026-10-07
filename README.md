# Project 4 — Enterprise Sales & Customer Analytics

## Business Problem
Fragmented customer, product, order, sales-representative and interaction data prevents leadership from obtaining a reliable view of revenue, customer value, sales effectiveness and conversion performance.

## Dataset Scale
The full synthetic enterprise dataset contains **4.6M+ records across multiple relational tables**.

| Dataset | Full-scale records |
|---|---:|
| Customers | 100,000 |
| Products | 5,000 |
| Sales representatives | 2,000 |
| Orders | 1,000,000 |
| Customer interactions | 1,000,000 |
| **Total** | **4.6M+** |

The full dataset is generated locally with `scripts/generate_data.py`; it is not committed to GitHub. Small samples are included.

## Business Questions
- Which customers and segments drive revenue?
- Which products/categories perform best and worst?
- Where is revenue weakening?
- Which customers are high-value or at risk?
- Which sales representatives and regions convert effectively?
- Where does the interaction funnel lose prospects?
- Which data-quality issues threaten reporting trust?

## Data Quality Problems
The generator deliberately introduces duplicate customers, invalid keys, zero/negative quantities, discounts above 100%, inconsistent statuses and other relational/data-quality anomalies.

## Analytical Stack
Python • SQL • dbt • Power BI • GitHub Actions

## Architecture
Raw enterprise sources → profiling → data-quality investigation → SQL standardisation → dbt staging/intermediate/marts → Power BI semantic model → business investigation.

## Dashboard
1. Executive Overview
2. Revenue & Product Performance
3. Customer Value & Retention Risk
4. Sales Representative Performance
5. Interaction Funnel
6. Data Quality & Trust

## Reproducibility
`python scripts/generate_data.py --scale-factor 1.0` is the documented enterprise-scale run. Use a smaller scale factor for development.
