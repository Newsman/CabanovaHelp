---
title: "Internationalized Domains"
group: "Domains and emails"
weight: 68
legacy: true
---
An **internationalized domain name (IDN)**  is an Internet domain name that contains at least one character that is in a language-specific alphabet, e.g. umlauts. At Cabanova we allow the registration of domains with characters "ü", "ö" and "ä" (umlauts) from the German alphabet.

**Not all applications such as browsers and email clients are able to deal with domains that contain umlauts properly.**

For example, some email clients will not be able to send/receive emails to/from accounts that contain language-specific characters. Some older browsers may not be able to display websites with domain names containing umlauts.

We recommend you to only use an internationalized domain as a secondary domain that redirects to your priimary domain, and to use a standard domain name as your primary domain.

**Example:**

Set **buecher.de**  as primary romain

Set **bücher.de**  to redirect to the primary domain

Check out our article [**how to set up your primary domain**](../primary-domain/).

**Here are some technical details**

The standard way domain names are encoded is in ASCII, the "American Standard Code for Information Interchange". Special characters such as umlauts are not used in the english language, so they are also not a part of the ASCII format. This would normally mean that domains cannot contain special characters. To solve this problem there is a standard called IDN, or "Internationalizing Domain names". IDN works by translating domain names that don't conform to the ASCII standard, into "ACE-Strings", which can in turn be interpreted in ASCII.

**Consequences:**

The domain name and the entry in the DNS are two different things with IDN.

**bücher.de**  is the domain name,

**xn--bcher-kva.de**  is the ACE string, and it is this string that is entered in the DNS.

For technical reasons, the character string that has been processed by the algorithm is several characters longer than the domain name itself. The domain name "www.buecher.ch" is seven characters long. The corresponding ACE string, however, is 13 characters long. IDN domains can be up to 63 characters long.

Cabanova does not guarantee that internationalized domain names (IDN) are suitable for use in conjuntion with programs such as browsers and email applications and does not accept any liability in this respect.
