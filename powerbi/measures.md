# Core Measures
Net Revenue = SUMX(Orders, Orders[quantity]*Orders[unit_price]*(1-Orders[discount]))
Orders = DISTINCTCOUNT(Orders[order_id])
AOV = DIVIDE([Net Revenue],[Orders])
Active Customers = CALCULATE(DISTINCTCOUNT(Customers[customer_id]),Customers[status]="Active")
