.headers on
.mode column
SELECT *
FROM (
	SELECT
		year,
		name,
		qty,
		RANK() OVER (PARTITION BY year ORDER BY qty desc) AS rank
	FROM(
		SELECT
			strftime('%Y', invoicedate) AS year,
			at.name,
			SUM(ii.quantity) AS qty
		FROM customers
		JOIN invoices i ON customers.customerid=i.customerid AND customers.state = 'CA'
		JOIN invoice_items ii ON ii.InvoiceId = i.InvoiceId
		JOIN tracks t ON ii.trackid = t.trackid
		JOIN albums a ON t.albumid = a.albumid
		JOIN artists at ON a.artistid = at.artistid
		GROUP BY year, at.name
		ORDER BY qty DESC) 
	) c
WHERE c.rank <=3;