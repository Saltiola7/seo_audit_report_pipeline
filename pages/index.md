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

## Traffic Estimation
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009144946.png)
Congratulations for a great launch of you new website in terms of SEO.

## Structured Data: Rich Result Validation Errors
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009211022.png)

The majority of the site has schema markup validation errors. I would dive into Google Search Console to the Product Listings & Merchant Listings tabs to diagnose this further. I also extracted a spreadsheetful of data about them.

![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009211728.png)
[Spreadsheet about Rich Result Validation Errors & Warnings](https://docs.google.com/spreadsheets/d/1cmYC9lcMCvqsbeXKIBPQwRhcGioMYAvuZ3ud_l9Fitg/edit?usp=sharing)

![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009203520.png)
These impact directly the Rich Results in Google and hence bottleneck the traffic from its full potential. Currently there are rich results available, but it could potentially be higher if this would be fixed.

**Here's a breakdown of the key issues and their impact:**

**1. Product Information Gaps:**

* **Missing Prices:** Many product listings are missing price information, a crucial detail for potential customers. Without clear pricing, customers may get frustrated and look elsewhere.  This is preventing Google from showing your products in rich result formats like Google Shopping.
* **Missing Images:** Several products lack images, making it harder for customers to visualize what they're buying. Just like a menu without pictures, this can discourage engagement and lead to missed opportunities. This also prevents your products from showing up in image search results and Google Shopping.
* **Incomplete Product Details:** Inconsistent or missing product descriptions and poorly formatted SKUs make it difficult for Google to match your products to relevant search queries. This is like an incomplete library catalog – it makes it harder for customers to find exactly what they're looking for.

**2. Missing Opportunities for Rich Results:**

* **No Star Ratings:** The absence of aggregate rating data means you're missing out on those eye-catching star ratings that appear under search results. These ratings build trust and can significantly increase click-through rates.
* **No Individual Reviews:** You can further enhance your product listings by including individual reviews. These offer more detailed insights for potential customers, increasing their confidence in making a purchase.

**3. GTINs for Wider Reach:**

* **Missing GTINs (Global Trade Item Numbers):** These unique identifiers are crucial for product recognition across retailers and marketplaces. Without them, your products may be excluded from certain platforms and comparisons, limiting their reach.


## Competition
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009145333.png)
There is still a long way to go to fill the keyword & backlink gaps to competition

## SERPs
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009152451.png)
Not optimized meta titles & meta descriptions

![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009191829.png)
Inconsistent brand name, Alevo or Athelgen? Both is confusing.

![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009191926.png)
None of the product pages have star reviews in the search result.

## Social Media
### Instagram
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009152707.png)
I would consider replacing linktree with a dedicated same style page in your website itself, to got the SEO & engagement benefits, instead of boosting linkr.ee domain.

Not very consistent content calendar around 15-20 posts per year, could be that amount per month.

### LinkedIn
Also not consistent posting.
No LinkedIn Insights tag for doing audience segmenting

## Wholesale
There could be a wholesale quick shop for retailers.

## Programmatic Landing Pages per Category x city
![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgrowthmindedmarketing.com%2Fwp-content%2Fuploads%2F2024%2F01%2FProgrammatic-SEO-example-1024x683.png&f=1&nofb=1&ipt=dbc1e5acd320314cb2f4f582c6de0d2c79c4ae1fbbdeb7a4d5cd1225c3338f34&ipo=images)

![](https://www.areaten.com/wp-content/uploads/2023/09/oegp2-consumer-insights-consumer-trends-local-search-to-store-visit-statis.jpg)
To get more local search traffic from all the cities you do business in.

Could also have a map of resellers nearest to that city if they dont want to deal with shipping, customs etc.

## Multilingual site?
If you do business internationally it could significantly increase traffic to have multilingual site.

## Contact Us
There is no appointment booking form.
The contact form could also be as a chatbot, which could also significantly increase lead generation, since users are prompted to input their emails to get response, and they would have less friction to chat than to fill a contact form.

## Social Proof
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009144018.png)
There are no reviews, though there is the review section in product pages.

I recommend implementing a call to review email campaign, which after 14-30 days would send email to customers to give a review of the product(s) they purchased.

You may also first direct users to a landing page, which filters 4-5 star reviews that are saved to the city in public and 1-3 star reviews are only received as feedback.

Right now I did not see any star reviews in the search results pages. Maybe they are hidden or maybe they do not exist.

![](https://www.business2community.com/wp-content/uploads/2020/07/how-to-ask-for-reviews-review-request-email.png)

## Products that could be merged into variants
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009145554.png)
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009145624.png)
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009145649.png)
![](https://stockholm-video-cdn.b-cdn.net/screenshot_20241009145706.png)

To reduce duplicate content and ease inventory management.

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
