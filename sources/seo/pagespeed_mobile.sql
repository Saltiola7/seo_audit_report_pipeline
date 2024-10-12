SELECT * FROM pagespeed_mobile
WHERE (url LIKE '%${domain_name}/%' 
   OR url LIKE '%${domain_name}');