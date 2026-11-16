---
title: "SEO Dealing with crawlers"
group: "SEO"
weight: 78
legacy: true
---
**Be aware of rel="nofollow" for linksCombat comment spam with "nofollow"Setting the value of the "rel" attribute of a link to "nofollow" will tell Google that certain links on your site shouldn't be followed or pass your page's reputation to the pages linked to** . Nofollowing a link is adding rel="nofollow" inside of the link's anchor tag **(1)** .

When would this be useful? If your site has a blog with public commenting turned on, links within those comments could pass your reputation to pages that you may not be comfortable vouching for. Blog comment areas on pages are highly susceptible to comment spam **(2)** . Nofollowing these user-added links ensures that you're not giving your page's hard-earned reputation to a spammy site.

![seo-guide22](legacy/iulv-38jifcri0u2l-3yxa3.jpg)

**Automatically add "nofollow" to comment columns and message boards**

Many blogging software packages automatically nofollow user comments, but those that don't can most likely be manually edited to do this. This advice also goes for other areas of your site that may involve user-generated content, such as guestbooks, forums, shoutboards, referrer listings, etc. If you're willing to vouch for links added by third parties (e.g. if a commenter is trusted on your site), then there's no need to use nofollow on links; however,**linking to sites that Google considers spammy can affect the reputation of your own site** . The Webmaster Help Center has more tips on [**avoiding comment spam**](https://support.google.com/webmasters/answer/81749?hl=en), like using CAPTCHAs and turning on comment moderation **(3)** .

![seo-guide23](legacy/iulv-2qm4b421lbtd-48knv.jpg)

**About using "nofollow" for individual contents, whole pages, etc.**

Another use of nofollow is **when you're writing content and wish to reference a website, but don't want to pass your reputation on to it** . For example, imagine that you're writing a blog post on the topic of comment spamming and you want to call out a site that recently comment spammed your blog. You want to warn others of the site, so you include the link to it in your content; however, you certainly don't want to give the site some of your reputation from your link. This would be a good time to use nofollow.

Lastly, if you're interested in nofollowing all of the links on a page, you can use "nofollow" in your robots meta tag, which is placed inside the

`<head>` tag of that page's HTML **(4)** . The Webmaster Central Blog provides a helpful post on [**using the robots meta tag**](http://googlewebmastercentral.blogspot.ro/2007/03/using-robots-meta-tag.html). This method is

written as `<meta name="robots" content="nofollow">`.

![seo-guide24](legacy/iulv-25uy133wcckv-73spe.jpg)

**Your Cabanova Website,rel="nofollow" for links and User Generated Content**

The rel="nofollow" attribute can't be applied for links at the Cabanova Sitebuilder level.

User generated Content on your Website (Guestbook and Contact Form) is spam-fight friendly.

A Spam Filter within our server filters submitted contact forms before delivering them the site owner email address.

Regarding the Guestbook, the posts can be fully controled and won't be published prior to your approval.

To learn more about Guestbook click [**here**](../guestbook/).

**Make effective use of robots.txtRestrict crawling where it's not needed with robots.txtA "robots.txt" file tells search engines whether they can access and therefore crawl parts of your site(1)** . This file, which must be named "robots.txt", is placed in the root directory of your site **(2)** .

![seo-guide21](legacy/iulv-3vxwsds37chi-kkhnd.jpg)

You may not want certain pages of your site crawled because they might not be useful to users if found in a search engine's search results. If you do want to prevent search engines from crawling your pages, Google Webmaster Tools has a friendly [**robots.txt generator**](http://googlewebmastercentral.blogspot.ro/2008/03/speaking-language-of-robots.html) to help you create this file. Note that if your site uses subdomains and you wish to have certain pages not crawled on a particular subdomain, you'll have to create a separate robots.txt file for that subdomain. For more information on robots.txt, we suggest this Webmaster Help Center guide on [**using robots.txt files**](https://support.google.com/webmasters/answer/6062608?hl=en&rd=1)

There are a handful of other ways to prevent content appearing in search results, such as adding "NOINDEX" to your robots meta tag,

using .htaccess to password protect directories, and using Google Webmaster Tools to remove content that has already been crawled.

Google engineer Matt Cutts walks through the [**caveats of each URL blocking method in a helpful video**](http://googlewebmastercentral.blogspot.ro/2008/01/remove-your-content-from-google.html).

**Your Cabanova Website and robots.txt**

We don't provide a function which would allow to generate a robot.txt file directly from the Sitebuilder but if necessary, you can generate a robot.txt file using the Google robot.txt Generator and provide us with it.

We'll then add it to the root directory of your Website at our server level.

The following link provides you with a detailed procedure on how to generate a robot.txt file: [**Click here to go to the link**](https://support.google.com/webmasters/answer/6062608?hl=en&rd=1)

**Best PracticesUse more secure methods for sensitive content**

You shouldn't feel comfortable using robots.txt to block sensitive or confidential material. One reason is that search engines could still reference the URLs you block (showing just the URL, no title or snippet) if there happen to be links to those URLs somewhere on the Internet (like referrer logs). Also, non-compliant or rogue search engines that don't acknowledge the Robots Exclusion Standard could

disobey the instructions of your robots.txt. Finally, a curious user could examine the directories or subdirectories in your robots.txt file and guess the URL of the content that you don't want seen. Encrypting the content or password-protecting it with .htaccess are more secure alternatives.

**Avoid:**

- allowing search result-like pages to be crawled

- users dislike leaving one search result page and landing on another search result page that doesn't add significant value for them

- allowing URLs created as a result of proxy services to be crawled.
