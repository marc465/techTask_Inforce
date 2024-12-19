-- Query 1: Retrieve the count of users who signed up on each day.
-- Additional: Ordered by signup_date
SELECT signup_date, count(*) FROM public.users
GROUP BY signup_date
ORDER BY signup_date;

-- Query 2: List all unique email domains present in the database.
-- Additional: Ordered by domain
SELECT domain FROM public.users
GROUP BY domain
ORDER BY domain;

-- Additional Query 2: Ordered by most popular domain
SELECT domain FROM public.users
GROUP BY domain
ORDER BY count(domain) DESC;

-- Query 3: Retrieve the details of users whose `signup_date` is within the last 7 days.
-- Additional: Ordered by signup_date
SELECT * FROM public.users
WHERE signup_date >= to_date('2024-12-17', 'YYYY-MM-DD') - INTERVAL '7 days'
ORDER BY signup_date DESC

-- Query 4: Find the user(s) with the most common email domain.
SELECT * FROM public.users
WHERE domain IN (
	SELECT domain FROM public.users
	GROUP BY domain
	ORDER BY COUNT(domain) DESC
	LIMIT 1
);

-- Query 5: Delete records where the email domain is not from a specific list
-- (e.g., keep only emails from `gmail.com`, `yahoo.com`, and `example.com`)
DELETE FROM public.users
WHERE domain NOT IN ('gmail.com', 'yahoo.com', 'example.com');
