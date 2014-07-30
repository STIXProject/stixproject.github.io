---
layout: flat
title: Security Considerations
---

<link href="/css/security.css" rel="stylesheet"/>

<p class="alert alert-danger"><strong>UNDER DEVELOPMENT:</strong> This guide is still under development. Please consider that it may be both inaccurate and/or incomplete.</p>

There are several potential avenues for attack when processing incoming STIX documents. The following list is non-exhaustive and should not take the place of a comprehensive security review that takes into account your unique technology stack and processes.

## Standard Attack Vectors

The following attack vectors can occur in any XML language and therefore do not rely on any specific STIX capabilities.

### <span class="label label-warning">XML Parsing Vulnerabilities</span>

There have historically been vulnerabilities in many XML parsing libraries that can cause either denial of service or, in rarer cases, actual exploits. As an example, see Microsoft's article on [XML Denial of Service Attacks and Defenses](http://msdn.microsoft.com/en-us/magazine/ee335713.aspx). The best defense for these types of attacks is, in short, to keep your XML parser up-to-date and ensure you perform full validation prior to attempting to process the document.

### <span class="label label-warning">Injection Attacks</span>

Since STIX content will end up being used somewhere, it's possible for injection attacks to be present in many places: description fields, titles, element values. These are, again, not specific to STIX. The best defense is to sanitize untrusted output (and anything from STIX should be considered untrusted). For more explanation on injection attacks, see [this OWASP article](https://www.owasp.org/index.php/Top_10_2010-A1-Injection).

## STIX and CybOX-Specific Attacks

The following types of attacks exploit capabilities built-in to the STIX and CybOX languages. Also note that although these use terminology suggesting malicious attacks, legitimate content could contain many of the same problems (especially denial of service through long execution time) so even trusted content should be handled carefully.

### <span class="label label-danger">Dereferencing Relationships</span>

STIX and CybOX both allow relationships between constructs using the `@idref` attribute. A malicious actor could use this capability to create an infinitely recursive relationship loop (in fact these are valid in STIX) or some other invalid relationship (between a component and itself, between components of different types, etc.). The best defense for this is to use strong error handling code when dereferencing relationships, understand how to avoid spinning endlessly on relationship cycles, and fail gracefully.

### <span class="label label-danger">Data Markings</span>

STIX data markings are implemented using XPath, meaning that the content producers will expect that the consumers execute this XPath against the content. Whenever executing third-party code, it's important to fail gracefully and build in appropriate timeouts to avoid denial of service attacks. In this case, an attacker could create an XPath expression that took processors several minutes to evaluate and overwhelm a consumer with documents. It's also possible to create injection attacks against XML databases or other places where STIX documents from multiple sources are combined (including composing a single STIX document from multiple others) with XPath expressions that execute outside their scope. The best defense is to ensure that the XPath is only executed within the correct scope (build a separate DOM if necessary), implement appropriate timeouts to mitigate DoS attacks, and as always, implement proper error handling to fail gracefully.

### <span class="label label-danger">CybOX Patterning</span>

CybOX patterning capability supports complicated patterning capabilities, including PCREs (Perl-Compatible Regular Expressions). Malicious content could contain both injection attacks (patterns operate outside their scope) or, more likely, denial of service attacks (patterns take overly long to evaluate). Even legitimate, trusted, content could contain patterns that take overly long to process against a given database or technology. Once again the best defense is to ensure the patterning is only applied to the correct scope and to apply a timeout capability to mitigate DoS attacks.

### <span class="label label-danger">STIX Indicators</span>

For obvious reasons (they get implemented at the system level), STIX indicators contain great potential to cause damage to a system or that system's business function. For example, a perfectly valid IP Watchlist could contain the IP to Google or the company's own website in order to flood the logs or even deny access. Therefore, those enacting STIX indicators should either have a manual review process or only include content from very trusted sources (trusted in the sense of not malicious but also trusted in the sense of competent).

### <span class="label label-danger">Simple DoS</span>

STIX documents contain many processing rules that are likely applied at ingest time. If a STIX repository is capable of having documents pushed to it then it would be possible to simply send a flood of valid STIX documents to that repository to overwhelm it...documents are cheap to send but expensive to process. Therefore, the defense is of course to rate-limit senders, apply queues as appropriate, and timeout if a document takes inordinately long to process.

### <span class="label label-info">Others?</span>

These are a simple list of attacks that we came up with off the top of our heads. What are we missing?
