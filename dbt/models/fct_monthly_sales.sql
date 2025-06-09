-- models/fct_monthly_sales.sql
SELECT
    month,
    total_revenue,
    total_orders,
    unique_customers
FROM {{ ref('int_monthly_sales') }}