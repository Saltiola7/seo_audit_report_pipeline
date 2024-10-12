---
title: On-Page
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

## Heading Levels

![](https://www.seobility.net/en/wiki/images/7/7d/H1-H6-headings.png)


{#if missing_h1.length !== 0} 

### Missing
#### Description
Pages which have a missing headings, the content is empty or has a whitespace. H1 headings should describe the main title and purpose of the page and are considered to be one of the stronger on-page ranking signals. H2 headings are often used to describe sections or topics within a document. They act as signposts for the user, and can help search engines understand the page.

#### How To Fix
Ensure important pages have concise, descriptive and unique H1 heading and logical and describtive H2's to help users, and enable search engines to score and rank the page for relevant search queries.

### H1's

```sql missing_h1
select
  address,
from internal_html_clean
where
  internal_html_clean.h1_1_length = 0
```

<DataTable data={missing_h1}>
    <Column id=address/>
</DataTable>

{/if}

{#if missing_h2.length !== 0}
### H2's

```sql missing_h2
select
  address,
from internal_html_clean
where
  internal_html_clean.h2_1_length = 0
  AND address IS NOT NULL
  AND address != ''
```

<DataTable data={missing_h2}>
    <Column id=address/>
</DataTable>

{/if}

{#if h1_over_70.length !== 0} 

### H1's Over 70 Characters
#### Description
Pages which have H1's over the configured length. There is no hard limit for characters in an H1, however they should be clear and concise for users and long headings might be less helpful

#### How To Fix 
Write concise H1's for users, including target keywords where natural for users - without keyword stuffing.

```sql h1_over_70
SELECT
    address,
    h1_1_length AS length,
    h1_1 AS h1
FROM internal_html_clean
WHERE h1_1_length > 70
  AND h1_1_length > 0  -- Added condition to exclude length 0 
ORDER BY
    length ASC;
```

<DataTable data={h1_over_70}>
    <Column id=address/>
    <Column id=length/>
    <Column id=h1/>
</DataTable>

{/if}

### Duplicates
#### Description
Pages which have duplicate same level headings. It's important to have distinct, unique and useful headings. If every page has the same heading, then it can make it more challenging for users and the search engines to understand one page from another.

#### How To Fix
Update duplicate headings as necessary, so important pages contain a unique and descriptive headings for users and search engines. If these are duplicate pages, then fix the duplicated pages by linking to a single version, and redirect or use canonicals where appropriate.

{#if duplicate_h1.length !== 0} 

### H1's

```sql duplicate_h1
SELECT
    address,
    h1_1_length AS length,
    h1_1 AS h1
FROM internal_html_clean
WHERE 
    h1_1_length > 0
    AND h1_1 IN (
        SELECT h1_1
        FROM internal_html_clean
        WHERE h1_1_length > 0
        GROUP BY h1_1
        HAVING COUNT(*) > 1
    )
ORDER BY
    length ASC;
```

<DataTable data={duplicate_h1}>
    <Column id=address/>
    <Column id=h1/>
</DataTable>

{/if}

{#if duplicate_h2.length !== 0} 

### H2's
 
```sql duplicate_h2
SELECT
    address,
    h2_1_length AS length,
    h2_1 AS h2
FROM internal_html_clean
WHERE 
    h2_1_length > 0
    AND h2_1 IN (
        SELECT h2_1
        FROM internal_html_clean
        WHERE h2_1_length > 0
        GROUP BY h2_1
        HAVING COUNT(*) > 1
    )
ORDER BY
    length ASC;
```

<DataTable data={duplicate_h2}>
    <Column id=address/>
    <Column id=h2/>
</DataTable>

{/if}


{#if low_word_count.length !== 0} 

## Low Content Pages

#### Description
Pages with a word count that is below the default 200 words. The word count is based upon the content area settings used in the analysis which can be configured via 'Config > Content > Area'. There isn't a minimum word count for pages in reality, but the search engines do require descriptive text to understand the purpose of a page. This filter should only be used as a rough guide to help identify pages that might be improved by adding more descriptive content in the context of the website and page's purpose. Some websites, such as ecommerce, will naturally have lower word counts, which can be acceptable if a products details can be communicated efficiently.

#### How To Fix
Consider including additional descriptive content to help the user and search engines better understand the page.

```sql low_word_count
select
  address,
  word_count
from internal_html_clean
where
  internal_html_clean.word_count < 200
```

<DataTable data={low_word_count}>
    <Column id=address/>
    <Column id=word_count/>
</DataTable>

{/if}

<!--
Excluded
- multiple same level headings
- non-sequential orderd headings
  AND address IS NOT NULL
  AND address != '' -- this is used to exclude the home directory, which should be made just as "/" instead of empty value
-->

