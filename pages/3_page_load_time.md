---
title: Page Load Time
---

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/_zdhQJeFxr4?si=tDY45WLJc7Xw3tSG"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>
<br>

{#if pagespeed_data.length < 0}
```sql pagespeed_data
SELECT * FROM pagespeed_mobile;
```
{/if}

**Testimonial after PageSpeed Optimization**
>"Its just stupid fast -- never seen anything so fast"  
>C. Lynch, True Hemp Science, WooCommerce Site

## TL;DR
- Optimize image resolution, compression, formatting & size attributes. Implement Content Delivery Network (CDN). Page Caching. Cache Preloading. Minify code. Prioritize the loading order of code and assets. Optimize fonts.
- All the issues on this page can be simply fixed by implementing all the features of [FlyingPress](https://flyingpress.com/?ref=zspw) if you are on Wordpress. I have optimized dozens of sites to go from over 10s page load time to 1 second.
- When using other CMS, there are further resources that help in troubleshooting and resolving issues for all Websites below.
- In many cases the page builder or website platform itself is the reason for slow page load speeds. In that case only focus on what you can improve and if you want even faster, you need to consider moving to another platform, where you have more control over pagespeed.

## Google's Metrics on Page Load Time
![](https://stockholm-video-cdn.b-cdn.net/assets/audits/consumer-insights-mobile-site-load-time-statistics.jpg)
![](https://stockholm-video-cdn.b-cdn.net/assets/audits/google-bounce-rate-chart.jpg)

## Tools for Diagnostics & Optimization
I recommend using these tools to do diagnostics and optimization of page load times
- [PageSpeed Insights](https://pagespeed.web.dev/)
  - Single page analysis
- [FlyingPress](https://flyingpress.com/?ref=zspw)
  - Optimization for Wordpress
- [Unlighthouse](https://unlighthouse.dev/)
  - Analyzes all the pages of the whole website
- [ImageOptim](https://imageoptim.com/)
  - Optimize images

# PageSpeed Insights Test Scores

{#if performance_score.length < 0}
```sql performance_score
select CAST(performance_score * 100 AS INTEGER) as performance_score
from pagespeed_mobile;
```
{/if}

**Performance Score:** <Value
  data={performance_score}
  value=performance_score
  fmt="0,0 'ms'"
  progressBar=false
  color={performance_score[0].performance_score > 90 ? "green" : performance_score[0].performance_score >= 50 ? "orange" : "red"}
/> / 100

#### Description
In general, only metrics contribute to your Lighthouse Performance score, not the results of Opportunities or Diagnostics. That said, improving the opportunities and diagnostics likely improve the metric values, so there is an indirect relationship.
[Read more](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring/?utm_source=lighthouse&utm_medium=lr)

## Metrics

**First Contentful Paint (FCP):** <Value
  data={pagespeed_data}
  value=fcp
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].fcp < 1800 ? "green" : pagespeed_data[0].fcp < 3000 ? "orange" : "red"}
/> ms

#### Description
First Contentful Paint marks the time at which the first text or image is painted. Images, non-white canvas elements, and SVGs on your page are considered DOM content; anything inside an iframe isn't included.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?utm_source=lighthouse&utm_medium=lr)

#### How To Fix
One issue that's particularly important for FCP is font load time. Check out the [Ensure text remains visible during webfont load](https://developer.chrome.com/docs/lighthouse/performance/font-display) post for ways to speed up your font loads.

**Largest Contentful Paint (LCP):** <Value
  data={pagespeed_data}
  value=lcp
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].lcp < 2500 ? "green" : pagespeed_data[0].lcp < 4000 ? "orange" : "red"}
/> ms

#### Description
Largest Contentful Paint marks the time at which the largest text or image is painted. This approximates when the main content of the page is visible to users. See [Largest Contentful Paint defined](https://web.dev/lcp/#what-is-lcp) for more details on how LCP is determined.
[Read more](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?utm_source=lighthouse&utm_medium=lr)

#### How To Fix
If the LCP is an image, the timing can be broken down into four phases. Knowing which phases take the longest can help you [optimize your LCP](https://web.dev/optimize-lcp/). Lighthouse will display the LCP element along with the phase breakdown in the "Largest Contentful Paint element" diagnostic.

{#if cls.length !== 0 && cls[0].cls >= 1}
{#if third_party_code.length < 0}
```sql cls
select cls from pagespeed_mobile
```
{/if}

**Cumulative Layout Shift (CLS):** <Value
  data={pagespeed_data}
  value=cls
  progressBar=false
  color={pagespeed_data[0].cls < 0.1 ? "green" : pagespeed_data[0].cls < 0.25 ? "orange" : "red"}
/>

#### Description
Cumulative layout shift measures the movement of visible elements within the viewport. Unexpected movement of page content usually happens when resources load asynchronously or DOM elements are dynamically added to the page before existing content. The cause of layout shifts might be images or videos with unknown dimensions, fonts that render larger or smaller than its initial fallback, or third-party ads or widgets that dynamically resize themselves.

- Good: CLS score of 0.1 or less.
- Needs improvement: CLS score between 0.1 and 0.25.
- Poor: CLS score of 0.25 or more.

[Read more](https://web.dev/articles/cls?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
Give images and elements specific sizes so browsers don't need to guess the right size.

{/if}

**Speed Index:** <Value
  data={pagespeed_data}
  value=speed_index
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].speed_index < 3400 ? "green" : pagespeed_data[0].speed_index < 5800 ? "orange" : "red"}
/> ms

#### Description
Speed Index measures how quickly content is visually displayed during page load. Lighthouse first captures a video of the page loading in the browser and computes the visual progression between frames. Lighthouse then uses the [Speedline Node.js module](https://github.com/paulirish/speedline) to generate the Speed Index score.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
While anything you do to improve page load speed will improve your Speed Index score, addressing any issues discovered by these Diagnostic audits should have a particularly big impact:

- [Minimize main thread work](https://developer.chrome.com/docs/lighthouse/performance/mainthread-work-breakdown)
- [Reduce JavaScript execution time](https://developer.chrome.com/docs/lighthouse/performance/bootup-time)
- [Ensure text remains visible during webfont load](https://developer.chrome.com/docs/lighthouse/performance/font-display)

**Total Blocking Time (TBT):** <Value
  data={pagespeed_data}
  value=tbt
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].tbt < 200 ? "green" : pagespeed_data[0].tbt < 600 ? "orange" : "red"}
/> ms

#### Description
TBT measures the total amount of time that a page is blocked from responding to user input, such as mouse clicks, screen taps, or keyboard presses. The sum is calculated by adding the blocking portion of all [long tasks](https://web.dev/long-tasks-devtools/) between [First Contentful Paint](https://web.dev/fcp/) and [Time to Interactive](https://web.dev/interactive/).
[Read more](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?utm_source=lighthouse&utm_medium=lr)

#### How To Fix
See [What is causing my long tasks?](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks) to learn how to diagnose the root cause of long tasks with the Performance panel of Chrome DevTools.

In general, the most common causes of long tasks are:

- Unnecessary JavaScript loading, parsing, or execution. While analyzing your code in the Performance panel you might discover that the main thread is doing work that isn't really necessary to load the page. [Reducing JavaScript payloads with code splitting](https://web.dev/reduce-javascript-payloads-with-code-splitting/), [removing unused code](https://web.dev/remove-unused-code/), or [efficiently loading third-party JavaScript](https://web.dev/efficiently-load-third-party-javascript/) should improve your TBT score.
- Inefficient JavaScript statements. For example, after analyzing your code in the Performance panel, suppose you see a call to document.querySelectorAll('a') that returns 2000 nodes. Refactoring your code to use a more specific selector that only returns 10 nodes should improve your TBT score.

## Diagnostics

{#if render_blocking_resources.length !== 0 && render_blocking_resources[0].render_blocking_resources >= 1}
{#if render_blocking_resources.length < 0}
```sql render_blocking_resources
select render_blocking_resources from pagespeed_mobile
```
{/if}

**Eliminate Render-Blocking Resources:** <Value
  data={render_blocking_resources}
  value=render_blocking_resources
  fmt="0,0 'ms'"
  progressBar=false
  emptySet="pass"
  emptyMessage="-"
  color={render_blocking_resources[0].render_blocking_resources < 300 ? "green" : render_blocking_resources[0].render_blocking_resources < 600 ? "orange" : "red"}
/> ms

#### Description
Resources are blocking the first paint. Consider delivering critical JS/CSS inline and deferring all non-critical JS/styles. The goal is to reduce the impact of these render-blocking URLs by inlining critical resources, deferring non-critical resources, and removing anything unused.
The first step towards reducing the impact of render-blocking resources is to identify what's critical and what's not. Use the Coverage tab in Chrome DevTools to identify non-critical CSS and JS. When you load or run a page, the tab tells you how much code was used, versus how much was loaded
![](https://developer.chrome.com/static/docs/lighthouse/performance/render-blocking-resources/image/chrome-devtools-coverage-60f77a25e4012_1920.png)

You can reduce the size of your pages by only shipping the code and styles that you need.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
Once you've identified critical code, move that code from the render-blocking URL to an inline script tag in your HTML page. When the page loads, it will have what it needs to handle the page's core functionality.

If there's code in a render-blocking URL that's not critical, you can keep it in the URL, and then mark the URL with async or defer attributes.

Code that isn't being used at all should be removed.

How to eliminate render-blocking stylesheets
Similar to inlining code in a script tag, inline critical styles required for the first paint inside a style block at the head of the HTML page. Then load the rest of the styles asynchronously using the preload link [see Defer unused CSS](https://web.dev/articles/defer-non-critical-css).

Consider automating the process of extracting and inlining "Above the Fold" CSS using the [Critical tool](https://github.com/addyosmani/critical/blob/master/README.md).

Another approach to eliminating render-blocking styles is to split up those styles into different files, organized by media query. Then add a media attribute to each stylesheet link. When loading a page, the browser only blocks the first paint to retrieve the stylesheets that match the user's device [see Render-Blocking CSS](https://web.dev/articles/critical-rendering-path/render-blocking-css).

Finally, you'll want to minify your CSS to remove any extra whitespace or characters [see Minify CSS](https://web.dev/articles/minify-css). This ensures that you're sending the smallest possible bundle to your users.

{/if}

{#if third_party_code.length !== 0 && third_party_code[0].third_party_code >= 50}
{#if third_party_code.length < 0}
```sql third_party_code
select third_party_code from pagespeed_mobile
```
{/if}

**Third-Party Code:** <Value
  data={pagespeed_data}
  value=third_party_code
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].third_part_code < 200 ? "green" : pagespeed_data[0].third_party_code < 400 ? "orange" : "red"}
/> ms

#### Description
Third-party code can significantly impact load performance. Limit the number of redundant third-party providers and try to load third-party code after your page has primarily finished loading.
Third-party scripts provide a variety of useful features that make the web more dynamic, interactive, and interconnected. Some of them might even be crucial to your website's function or revenue stream. But using them may slow down the site.
Ideally, you'll want to ensure third-party scripts aren't impacting your site's [critical rendering path](https://web.dev/articles/critical-rendering-path).

Third-party JavaScript often refers to scripts that can be embedded into any site directly from a third-party vendor. Examples include:
- Social sharing buttons (Facebook, X, LinkedIn, Mastodon)
- Video player embeds (YouTube, Vimeo)
- Advertising iframes
- Analytics & metrics scripts
- A/B testing scripts for experiments
- Helper libraries, such as date formatting, animation, or functional libraries

[Read more](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
If a third-party script is slowing down your page load, you have several options to improve performance:

- Load the script using the async or defer attribute to avoid blocking document parsing.
- If the third-party server is slow, consider self-hosting the script.
- If the script doesn't add clear value to your site, remove it.
- Use [Resource Hints](https://developer.chrome.com/docs/lighthouse/performance/uses-rel-preconnect) like link rel=preconnect or link rel=dns-prefetch to perform a DNS lookup for domains hosting third-party scripts.

{/if}

{#if javascript_execution_time.length !== 0 && javascript_execution_time[0].javascript_execution_time >= 50}
{#if javascript_execution_time.length < 0}
```sql javascript_execution_time
select javascript_execution_time from pagespeed_mobile
```
{/if}

**JavaScript Execution Time:** <Value
  data={pagespeed_data}
  value=javascript_execution_time
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].javascript_execution_time < 300 ? "green" : pagespeed_data[0].javascript_execution_time < 600 ? "orange" : "red"}
/> ms

#### Description
Consider reducing the time spent parsing, compiling and executing JS. You may find delivering smaller JS payloads helps with this.

#### How To Fix
- [Only send the code that your users need by implementing code splitting.](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting)
- [Minify and compress your code.](https://web.dev/articles/reduce-network-payloads-using-text-compression)
- [Remove unused code.](https://web.dev/articles/remove-unused-code)
- [Reduce network trips by caching your code with the PRPL pattern.](https://web.dev/articles/apply-instant-loading-with-prpl)

{/if}

{#if main_thread_work.length !== 0 && main_thread_work[0].main_thread_work >= 50}
{#if main_thread_work.length < 0}
```sql main_thread_work
select main_thread_work from pagespeed_mobile
```
{/if}

**Main Thread Work:** <Value
  data={pagespeed_data}
  value=main_thread_work
  fmt="0,0 'ms'"
  progressBar=false
  color={pagespeed_data[0].main_thread_work < 300 ? "green" : pagespeed_data[0].main_thread_work < 600 ? "orange" : "red"}
/> ms

#### Description
Consider reducing the time spent parsing, compiling and executing JS. You may find delivering smaller JS payloads helps with this.
#### How To Fix
##### Script evaluation
- [Optimize third-party JavaScript](https://web.dev/articles/fast#optimize_your_third_party_resources)
- [Debounce your input handlers](https://web.dev/articles/debounce-your-input-handlers)
- [Use web workers](https://web.dev/articles/off-main-thread)
##### Style and layout
- [Reduce the scope and complexity of style calculations](https://web.dev/articles/reduce-the-scope-and-complexity-of-style-calculations)
- [Avoid large, complex layouts and layout thrashing](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing)
##### Rendering
- [Stick to compositor only properties and manage layer count](https://web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count)
- [Simplify paint complexity and reduce paint areas](https://web.dev/articles/simplify-paint-complexity-and-reduce-paint-areas)
##### Parsing HTML and CSS
- [Extract critical CSS](https://web.dev/articles/extract-critical-css)
- [Minify CSS](https://web.dev/articles/minify-css)
- [Defer non-critical CSS](https://web.dev/articles/defer-non-critical-css)
##### Script parsing and compilation
- [Reduce JavaScript payloads with code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting)
- [Remove unused code](https://web.dev/articles/remove-unused-code)
##### Garbage collection
- [Monitor your web page's total memory usage with measureMemory()](https://web.dev/articles/monitor-total-page-memory-usage)

{/if}

{#if unused_css.length !== 0 && unused_css[0].unused_css >= 50}
{#if unused_css.length < 0}
```sql unused_css
select unused_css from pagespeed_mobile
```
{/if}

**Unused CSS:** <Value
  data={pagespeed_data}
  value=unused_css
  fmt="0.0 'KB'"
  progressBar=false
  color={pagespeed_data[0].unused_css < 10 ? "green" : pagespeed_data[0].unused_css < 30 ? "orange" : "red"}
/> ms

#### Description
By default, a browser must download, parse, and process all external stylesheets that it encounters before it can display, or render, any content to a user's screen. It wouldn't make sense for a browser to attempt to display content before the stylesheets have been processed, because the stylesheets may contain rules that affect the styling of the page.
Each external stylesheet must be downloaded from the network. These extra network trips can significantly increase the time that users must wait before they see any content on their screens.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/unused-css-rules/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
Reduce unused rules from stylesheets and defer CSS not used for above-the-fold content to decrease bytes consumed by network activity.

Inline critical CSS and defer non-critical CSS
Similar to inlining code in a script tag, inline critical styles required for the first paint inside a style block at the head of the HTML page. Then load the rest of the styles asynchronously using the preload link.

Consider automating the process of extracting and inlining "Above the Fold" CSS using the [Critical tool](https://github.com/addyosmani/critical/blob/master/README.md).

Learn more in [Defer non-critical CSS](https://web.dev/articles/defer-non-critical-css).

Consider reducing, or switching, the number of WordPress plugins loading unused CSS in your page.

{/if}

{#if unminified_css.length !== 0 && unminified_css[0].unminified_css >= 50}
{#if unminified_css.length < 0}
```sql unminified_css
select unminified_css from pagespeed_mobile
```
{/if}

**Unminified CSS:** <Value
  data={pagespeed_data}
  value=unminified_css
  fmt="0.0 'KB'"
  progressBar=false
  color={pagespeed_data[0].unminified_css < 10 ? "green" : pagespeed_data[0].unminified_css < 30 ? "orange" : "red"}
/> ms

#### Description
Minifying CSS files can reduce network payload sizes.
[Read more](https://developer.chrome.com/docs/lighthouse/performance/unminified-css/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
A number of [WordPress plugins](https://wordpress.org/plugins/search/minify+css/) can speed up your site by concatenating, minifying, and compressing your styles. You may also want to use a build process to do this minification up-front if possible.

{/if}

{#if modern_image_formats.length !== 0 && modern_image_formats[0].modern_image_formats >= 50}
{#if modern_image_formats.length < 0}
```sql modern_image_formats
select modern_image_formats from pagespeed_mobile
```
{/if}

**Modern Image Formats:** <Value
  data={pagespeed_data}
  value=modern_image_formats
  fmt="0.0 'KB'"
  progressBar=false
  color={pagespeed_data[0].modern_image_formats < 10 ? "green" : pagespeed_data[0].modern_image_formats < 30 ? "orange" : "red"}
/> ms

#### Description
Image formats like [WebP](https://developers.google.com/speed/webp/) and [AVIF](https://codelabs.developers.google.com/codelabs/avif) often provide better compression than PNG or JPEG, which means faster downloads and less data consumption.
AVIF and WebP are image formats that have superior compression and quality characteristics compared to their older JPEG and PNG counterparts. Encoding your images in these formats rather than JPEG or PNG means that they will load faster and consume less cellular data.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/uses-webp-images/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
Consider using a [plugin](https://wordpress.org/plugins/search/convert+webp/) or service that will automatically convert your uploaded images to the optimal formats

{/if}

{#if image_optimization.length !== 0 && image_optimization[0].image_optimization >= 50}
{#if image_optimization.length < 0}
```sql image_optimization
select image_optimization from pagespeed_mobile
```

{/if}

**Image Optimization:** <Value
  data={pagespeed_data}
  value=image_optimization
  fmt="0.0 'KB'"
  progressBar=false
  color={pagespeed_data[0].image_optimization < 10 ? "green" : pagespeed_data[0].image_optimization < 30 ? "orange" : "red"}
/> ms

#### Description
Optimised images load faster and consume less mobile data.
[Read more](https://developer.chrome.com/docs/lighthouse/performance/uses-optimized-images/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
- [Using image CDNs](https://web.dev/articles/image-cdns)
- [Compressing images](https://web.dev/articles/use-imagemin-to-compress-images)
- [Replacing animated GIFs with video](https://web.dev/articles/replace-gifs-with-videos)
- [Lazy loading images](https://web.dev/articles/codelab-use-lazysizes-to-lazyload-images)
- [Serving responsive images](https://web.dev/articles/serve-responsive-images)
- [Serving images with correct dimensions](https://web.dev/articles/serve-images-with-correct-dimensions)
- [Using WebP images](https://web.dev/articles/serve-images-webp)

Consider using an [image optimization WordPress plugin](https://wordpress.org/plugins/search/optimize+images/) that compresses your images while retaining quality.

{/if}

{#if unsized_images.length !== 0 && unsized_images[0].unsized_images >= 50}
{#if unsized_images.length < 0}
```sql unsized_images
select unsized_images from pagespeed_mobile
```
{/if}

**Unsized Images:** <Value
  data={pagespeed_data}
  value=unsized_images
  fmt="0,0"
  progressBar=false
  color={pagespeed_data[0].unsized_images == 0 ? "green" : "red"}
/> ms

#### Description
Serve images that are appropriately-sized to save mobile data and improve load time.

Ideally, your page should never serve images that are larger than the version that's rendered on the user's screen. Anything larger than that just results in wasted bytes and slows down page load time.

The main strategy for serving appropriately sized images is called "responsive images". With responsive images, you generate multiple versions of each image, and then specify which version to use in your HTML or CSS using media queries, viewport dimensions, and so on. Additionally, [RespImageLint](https://ausi.github.io/respimagelint/) is a helpful bookmarklet for identifying the optimal srcset and sizes values for your images. See [Serve responsive images](https://web.dev/serve-responsive-images) to learn more about these attributes.

[Image CDNs](https://web.dev/articles/image-cdns) are another main strategy for serving appropriately sized images. You can think of image CDNs like web service APIs for transforming images.

Another strategy is to use vector-based image formats, like SVG. With a finite amount of code, an SVG image can scale to any size. See [Replace complex icons with SVG](https://web.dev/articles/responsive-images#replace_complex_icons_with_svg) to learn more.

Tools like [gulp-responsive](https://www.npmjs.com/package/gulp-responsive) or [responsive-images-generator](https://www.npmjs.com/package/responsive-images-generator) can help automate the process of converting an image into multiple formats. There are also image CDNs which let you generate multiple versions, either when you upload an image, or request it from your page.


[Read more](https://developer.chrome.com/docs/lighthouse/performance/uses-responsive-images/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
Upload images directly through the media library to ensure that the required image sizes are available, and then insert them from the media library or use the image widget to ensure the optimal image sizes are used (including those for the responsive breakpoints). Avoid using Full Size images unless the dimensions are adequate for their usage. See [Inserting images into posts and pages](https://wordpress.org/support/article/inserting-images-into-posts-and-pages/).

{/if}

{#if lcp_element.length !== 0 && lcp_element[0].lcp_element >= 50}
{#if lcp_element.length < 0}
```sql lcp_element
select lcp_element from pagespeed_mobile
```
{/if}

**LCP Element:** <Value
  data={pagespeed_data}
  value=lcp_element
  progressBar=false
/> ms

#### Description
This is the largest contentful element painted within the viewport.

[Read more](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?utm_source=lighthouse&utm_medium=lr)
#### How To Fix
If the LCP is an image, the timing can be broken down into four phases. Knowing which phases take the longest can help you [optimize your LCP](https://web.dev/optimize-lcp/). Lighthouse will display the LCP element along with the phase breakdown in the "Largest Contentful Paint element" diagnostic.

{/if}


<!--
<DataTable data={pagespeed_data}/>
Potential savings sum ms
Table from where user can download the data

which part of pagespeed insights was the one below?

{#if responsive_images.length !== 0 && responsive_images[0].responsive_images !== 0}
{#if responsive_images.length < 0}
```sql responsive_images
select responsive_images from pagespeed_mobile
```
{/if}

**Responsive Images:** <Value
  data={pagespeed_data}
  value=responsive_images
  fmt="0,0"
  progressBar=false
  color={pagespeed_data[0].responsive_images == 0 ? "green" : "red"}
/> ms

#### Description

#### How To Fix

{/if}

When inspecting the test results further we see some actionable advice that could make the site load faster:
1. Images
   - Currently Squarespace only supports heavier png and jpg formats, not next-gen formats like webP, which are only possible via 3rd party solutions like Cloudinary CDN at this time.
   - The images could be compressed locally before uploading to the web with something like ImageOptim.
2. Font
   - Currently the fonts are loaded from Google CDN's every time a user comes to the page, which adds to the site loading 0.75 seconds. Fixing this alone, would bring the site to under 3 seconds of load time.
   - To fix this, its possible to load the font files directly to Squarespace website platform so its not necessary to load from Google every time.
   - Also the font file itself can be stripped from unnecessary symbols.
3. Analytics Tags
   - In GTM different analytics tags can also be prioritised so that the page will be loaded first with essential analytics and then secondary analytics like LinkedIn Insights, Facebook Pixel, etc.

![](https://cdn.cronitor.io/static/img/blog/page-load-time/page-load-timeline.png) 

-->
