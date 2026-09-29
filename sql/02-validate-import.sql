-- check table structure
PRAGMA table_info(transactions);

-- Confirm table exists
SELECT name
FROM sqlite_master
WHERE type = 'table';


-- Confirm imported row count
SELECT COUNT(*) AS row_count
FROM transactions;

-- Inspect the first 5 rows 
SELECT * 
FROM transactions
ORDER BY transaction_id
LIMIT 5;