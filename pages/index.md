---
title: moreliving.com.au SEO Audit
---

<!-- <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div> -->



## Social Proof
- Testimonials
- Reviews
- 

## Summary of SERP & On-Page Analysis

{#if summary_table < 0}
```sql summary_table
SELECT
  'Missing Meta Descriptions' AS Metric,
  COUNT(CASE WHEN T1.meta_description_1_length = 0 THEN T1.address ELSE NULL END) AS Total_Count
FROM internal_html_clean AS T1
UNION ALL
SELECT
  'Short/Long Meta Descriptions',
  COUNT(CASE WHEN (T2.meta_description_1_length < 70 OR T2.meta_description_1_length > 155) AND T2.meta_description_1_length > 0 THEN T2.address ELSE NULL END)
FROM internal_html_clean AS T2
UNION ALL
SELECT
  'Duplicate Meta Descriptions',
  (
    SELECT
      COUNT(*)
    FROM (
      SELECT
        meta_description_1
      FROM internal_html_clean
      WHERE
        meta_description_1_length > 0
      GROUP BY
        meta_description_1
      HAVING
        COUNT(*) > 1
    ) AS t1
  )
FROM (
  SELECT
    1
) AS dummy_table
UNION ALL
SELECT
  'Missing Meta Titles',
  COUNT(CASE WHEN T3.title_1_length = 0 THEN T3.address ELSE NULL END)
FROM internal_html_clean AS T3
UNION ALL
SELECT
  'Short/Long Meta Titles',
  COUNT(CASE WHEN (T4.title_1_length < 150 OR T4.title_1_length > 160) AND T4.title_1_length > 0 THEN T4.address ELSE NULL END)
FROM internal_html_clean AS T4
UNION ALL
SELECT
  'Duplicate Meta Titles',
  (
    SELECT
      COUNT(*)
    FROM (
      SELECT
        title_1
      FROM internal_html_clean
      WHERE
        title_1_length > 0
      GROUP BY
        title_1
      HAVING
        COUNT(*) > 1
    ) AS t2
  )
FROM (
  SELECT
    1
) AS dummy_table
UNION ALL
SELECT
  'Titles Same as H1s',
  COUNT(CASE WHEN T5.title_1_length > 0 AND T5.title_1 = T5.h1_1 THEN T5.address ELSE NULL END)
FROM internal_html_clean AS T5
UNION ALL
SELECT
  'Missing H1s',
  COUNT(CASE WHEN T6.h1_1_length = 0 THEN T6.address ELSE NULL END)
FROM internal_html_clean AS T6
UNION ALL
SELECT
  'Missing H2s',
  COUNT(CASE WHEN T7.h2_1_length = 0 THEN T7.address ELSE NULL END)
FROM internal_html_clean AS T7
UNION ALL
SELECT
  'H1s Over 70 Characters',
  COUNT(CASE WHEN T8.h1_1_length > 70 AND T8.h1_1_length > 0 THEN T8.address ELSE NULL END)
FROM internal_html_clean AS T8
UNION ALL
SELECT
  'Duplicate H1s',
  (
    SELECT
      COUNT(*)
    FROM (
      SELECT
        h1_1
      FROM internal_html_clean
      WHERE
        h1_1_length > 0
      GROUP BY
        h1_1
      HAVING
        COUNT(*) > 1
    ) AS t3
  )
FROM (
  SELECT
    1
) AS dummy_table
UNION ALL
SELECT
  'Duplicate H2s',
  (
    SELECT
      COUNT(*)
    FROM (
      SELECT
        h2_1
      FROM internal_html_clean
      WHERE
        h2_1_length > 0
      GROUP BY
        h2_1
      HAVING
        COUNT(*) > 1
    ) AS t4
  )
FROM (
  SELECT
    1
) AS dummy_table
UNION ALL
SELECT
  'Low Word Count Pages',
  COUNT(CASE WHEN T9.word_count < 200 THEN T9.address ELSE NULL END)
FROM internal_html_clean AS T9
ORDER BY
  Total_Count DESC;
```
{/if}

Below is a table and a chart, which shows the total count of pages per metric. I breakdown each metric in the next pages.

<DataTable data={summary_table}>
    <Column id=Metric/>
    <Column id=Total_Count/>
</DataTable>

<BarChart
    data={summary_table}
    x=Metric
    y=Total_Count
    swapXY=true
/>
