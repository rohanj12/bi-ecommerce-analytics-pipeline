-- models/int_monthly_sales.sql

SELECT
    date_trunc('month', invoicedate::timestamp) AS month,
    SUM(quantity * unitprice) AS total_revenue,
    COUNT(DISTINCT invoiceno) AS total_orders,
    COUNT(DISTINCT customerid) AS unique_customers
FROM {{ ref('stg_raw_retail_data') }}
GROUP BY 1
ORDER BY 1