-- models/stg_raw_retail_data.sql

SELECT
    invoiceno,
    stockcode,
    description,
    quantity,
    invoicedate,
    unitprice,
    customerid,
    country
FROM public.raw_retail_data