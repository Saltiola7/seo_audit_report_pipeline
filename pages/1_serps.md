---
title: SERPs
---

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/51w_1vntg2A?si=xBkQdblvM-m-LjL7" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>


<br>

![](https://prosglobalinc.com/wp-content/uploads/2022/11/SERPs.jpg)


Optimising SERP's is crucial for Click-Through Rate (CTR).

![ctr](https://stockholm-video-cdn.b-cdn.net/assets/audits/math/ctr.svg)

The traffic that is coming from the SERP's, looking mostly at the highest listings and their metatitles & metadescriptions when making decision for which one to click.

## CTR by...
### Industry

| Industry | Average CTR (Search) |
|---|---|
| Travel | 9.19% |
| Sports & Recreations | 8.82% |
| E-commerce | 5.50% |
| Restaurants & Food | 7.60% |
| Real Estate | 8.55% |
| Industrial & Commercial | 5.61% |
| Home & Home Improvement | 4.62% |
| Health & Fitness | 6.15% |
| Finance & Insurance | 5.70% |
| Education & Instruction | 6.17% |
| Career & Employment | 5.93% |
| B2B | 5.17% |
| Beauty & Personal Care | 5.92% |
| Automotive | 5.65% |
| Attorneys & Legal Services | 4.24% |
| Arts & Entertainment | 11.43% | 

### Ranking

| Google Search Feature | CTR |
|---|---|
| Ad Position 1 | 2.1% |
| Ad Position 2 | 1.4% |
| Ad Position 3 | 1.3% |
| Ad Position 4 | 1.2% |
| Search Position 1 | 39.8%* |
| Search Position 2 | 18.7%** |
| Search Position 3 | 10.2% |
| Search Position 4 | 7.2% |
| Search Position 5 | 5.1% |
| Search Position 6 | 4.4% |
| Search Position 7 | 3.0% |
| Search Position 8 | 2.1% |
| Search Position 9 | 1.9% |
| Search Position 10 (if present) | 1.6% | 

*If snippet, then 42.9%; If local pack present, then 23.7%
**If snippet, then 27.4%; If local pack present, then 15.1%

### SERP Feature

| Google SERP Feature | Example | CTR |
|---|---|---|
| Snippet | ![](https://firstpagesage.com/wp-content/uploads/2022/01/snippet-example-300x178.png) | 42.9% (1st)<br>27.4% (2nd) |
| #1 Organic Result | ![](https://firstpagesage.com/wp-content/uploads/2022/01/organic-result-example-300x181.png) | 39.8% |
| Ad Result | ![](https://firstpagesage.com/wp-content/uploads/2022/01/ad-result-example-300x202.png) | 1.2 – 2.1% |
| Image Result | ![](https://firstpagesage.com/wp-content/uploads/2022/01/image-result-example-300x193.png) | 1.4% – 4.9% |
| Video Result | ![](https://firstpagesage.com/wp-content/uploads/2022/01/video-result-example-300x171.png) | 2.3% – 6.4% |
| “People Also Ask” Box | ![](https://firstpagesage.com/wp-content/uploads/2022/01/also-ask-example-300x197.png) | 3.0% |
| Knowledge Panel | ![](https://firstpagesage.com/wp-content/uploads/2022/01/knowledge-panel-example-300x194.png) | 1.4% |

## Meta Descriptions

![](https://sitechecker.pro/wp-content/uploads/2023/06/what-is-meta-description.png)

{#if missing_metadescription.length !== 0} 

### Missing
#### Description
Pages which have a missing meta description, the content is empty or has a whitespace. This is a missed opportunity to communicate the benefits of your product or service and influence click through rates for important URLs. Many website platforms automatically generate a missing meta description from the page content, which is not optimal.

#### How To Fix
It's important to write unique and descriptive meta descriptions on key pages to communicate the purpose of the page to users, and entice them to click on your result over the competition. It can also mean Google use this description for snippets in the search results for some queries, rather than make up their own based upon the content of the page.

```sql missing_metadescription
select
  address,
from internal_html_clean
where
  meta_description_1_length = 0
```

<DataTable data={missing_metadescription}>
    <Column id=address/>
</DataTable>

{/if}

{#if short_long_metadescription.length !== 0}

### Less Than 70 and More Than 155 Characters

#### Description
Pages which have meta descriptions below or above the optimal length. This isn't strictly an issue, but an opportunity. There is additional room to communicate benefits, USPs or call to actions. Or opportunity to optimise longer ones as characters over 155 long might be truncated in Google's search results.

#### How To Fix
Consider updating the meta description to take advantage of the space left to include additional benefits, USPs or call to actions to improve click through rates (CTR) meanwhile keeping them concise to ensure important words are not truncated in the search results, and not visible to users.

```sql short_long_metadescription
SELECT
    address,
    meta_description_1_length AS length,
    meta_description_1 AS meta_description
FROM internal_html_clean
WHERE (meta_description_1_length < 70 OR meta_description_1_length > 155)
  AND meta_description_1_length > 0
ORDER BY
    length ASC;
```

<DataTable data={short_long_metadescription}>
    <Column id=address/>
    <Column id=length/>
    <Column id=meta_description/>
</DataTable>

{/if}

{#if duplicate_metadescription.length !== 0} 

### Duplicates

#### Description
Pages which have duplicate meta descriptions. It's really important to have distinct and unique meta descriptions that communicate the benefits and purpose of each page. If they are duplicate or irrelevant, then they will be ignored by search engines in their snippets.

#### How To Fix
Update duplicate meta descriptions as necessary, so important pages contain a unique and descriptive title for users and search engines. If these are duplicate pages, then fix the duplicated pages by linking to a single version, and redirect or use canonicals where appropriate.

```sql duplicate_metadescription
SELECT
    address,
    meta_description_1_length AS length,
    meta_description_1 AS meta_description
FROM internal_html_clean
WHERE 
    meta_description_1_length > 0
    AND meta_description_1 IN (
        SELECT meta_description_1
        FROM internal_html_clean
        WHERE meta_description_1_length > 0
        GROUP BY meta_description_1
        HAVING COUNT(*) > 1
    )
ORDER BY
    length ASC;
```

<DataTable data={duplicate_metadescription}>
    <Column id=address/>
    <Column id=meta_description/>
</DataTable>

{/if}

## Meta Titles

![](https://www.seobility.net/en/wiki/images/6/64/Meta-Title.png)

{#if missing_metatitle.length !== 0} 
### Missing

#### Description
Pages which have a missing page title element, the content is empty, or has a whitespace. Page titles are read and used by both users and the search engines to understand what a page is about. They are important for SEO as page titles are used in rankings, and vital for user experience, as they are displayed in browsers, search engine results and on social networks.

#### How To Fix
It's essential to write concise, descriptive and unique page titles on every indexable URL to help users, and enable search engines to score and rank the page for relevant search queries.

```sql missing_metatitle
select
  address,
from internal_html_clean
where
  internal_html_clean.title_1_length = 0
  AND address IS NOT NULL
  AND address != ''
```

<DataTable data={missing_metatitle}>
    <Column id=address/>
</DataTable>

{/if}

{#if short_long_metatitle.length !== 0} 
### Less Than 30 and More Than 60 Characters

#### Description
Pages which have page titles under the configured limit. This isn't necessarily an issue, but it does indicate there might be room to target additional keywords or communicate your USPs.
Pages which have page titles that exceed the configured limit. Characters over this limit might be truncated in Google's search results and carry less weight in scoring.  
<!-- #todo fix sentence -->

#### How To Fix
Consider updating the page title to take advantage of the space left to include additional target keywords or USPs.
Write concise page titles to ensure important words are not truncated in the search results, not visible to users and potentially weighted less in scoring.
<!-- #todo fix sentence -->

```sql short_long_metatitle
SELECT
    address,
    title_1_length AS length,
    title_1 AS meta_title
FROM internal_html_clean
WHERE (title_1_length < 150 OR title_1_length > 160)
  AND title_1_length > 0  -- Added condition to exclude length 0 
ORDER BY
    length ASC;
```

<DataTable data={short_long_metatitle}>
    <Column id=address/>
    <Column id=length/>
    <Column id=meta_title/>
</DataTable>

{/if}

{#if duplicate_metatitle.length !== 0} 

### Duplicates

#### Description
Pages which have duplicate page titles. It's really important to have distinct and unique page titles for every page. If every page has the same page title, then it can make it more challenging for users and the search engines to understand one page from another.

#### How To Fix
Update duplicate page titles as necessary, so each page contains a unique and descriptive title for users and search engines. If these are duplicate pages, then fix the duplicated pages by linking to a single version, and redirect or use canonicals where appropriate.

```sql duplicate_metatitle
SELECT
    address,
    title_1_length AS length,
    title_1 AS meta_title
FROM internal_html_clean
WHERE 
    title_1_length > 0
    AND title_1 IN (
        SELECT title_1
        FROM internal_html_clean
        WHERE title_1_length > 0
        GROUP BY title_1
        HAVING COUNT(*) > 1
    )
ORDER BY
    length ASC;
```

<DataTable data={duplicate_metatitle}>
    <Column id=address/>
    <Column id=meta_title/>
</DataTable>

{/if}

{#if title_same_as_h1.length !== 0} 

### Same as H1

#### Description
Page titles which match the h1 heading on the page exactly. This is not necessarily an issue, but may point to a potential opportunity to target alternative keywords, synonyms, or related key phrases.

#### How To Fix
This is not necessarily an issue, but may point to a potential opportunity to target alternative keywords, synonyms, or related key phrases.

```sql title_same_as_h1
SELECT
    address,
    title_1 AS meta_title,
    h1_1 AS h1
FROM internal_html_clean p
WHERE
    title_1_length > 0
    AND title_1 = h1_1
```

<DataTable data={title_same_as_h1}>
    <Column id=address/>
    <Column id=meta_title/>
    <Column id=h1/>
</DataTable>

{/if}
