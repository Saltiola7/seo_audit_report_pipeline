SELECT *
FROM main.internal_html_clean
WHERE (Address LIKE '%${domain_name}/%' 
   OR Address LIKE '%${domain_name}')
  AND indexability_status NOT IN ('Canonicalised', 'Redirected', 'noindex'); 