---
layout: getting_started
title: Getting Started
active: getting-started
---

<div class="container-fluid">
  <div class="row">
    <div class="col-md-6 getting-started-left">
      <h3>For Analysts & Managers</h3>
      <p>The Analysts & Manager tutorial track will walk you through understanding the STIX data model and how content is expressed in it at a high level. You won't have to deal with XML or Python at all.</p>

      <div class="well">
        <h4><a href="http://stix.mitre.org/about/documents/STIX_Whitepaper_v1.1.pdf">STIX Whitepaper</a></h4>
        <p>The STIX Whitepaper explains why STIX was developed, what problems it solves, and how it solves those problems. It also goes into detail on the individual components of STIX and how they fit together.</p>
        <a class="btn btn-primary" href="http://stix.mitre.org/about/documents/STIX_Whitepaper_v1.1.pdf">Go »</a>
      </div>

      <div class="well">
        <h4>Analyst Walkthrough (Coming Soon)</h4>
        <p>The analyst walkthrough will take you through a sample STIX document using the STIXViz tool. It will explain what the different pieces are and how they fit together.<p>
        <a class="btn btn-default disabled" href="#">Go »</a>
      </div>

      <div class="well">
        <h4>Analyst Modeling Exercise (Coming Soon)</h4>
        <p>The analyst modeling exercise will walk you through a fictional threat report and discuss how it's mapped into the STIX data model. It discussions decisions about which components to use and how to relate the components together.</p>
        <a class="btn btn-default disabled" href="#">Go »</a>
      </div>

    </div>

    <div class="col-md-6 getting-started-right">
      <h3>For Developers</h3>

      <p>The Developer tutorial track gets into the nitty gritty of STIX XML and the python-stix APIs that make working with it easier. The analyst tutorials give important context as to why things are the way they are and should be completed first.</p>

      <div class="well">
        <h4><a href="http://stix.readthedocs.org/en/latest/getting_started.html">Python STIX Getting Started</a></h4>
        <p>This guide walks through the basics of working with STIX using the python-stix library. Those working in languages other than Python or not using the libraries should follow the sample walkthrough and authoring tutorial.</p>
        <a class="btn btn-primary" href="http://stix.readthedocs.org/en/latest/getting_started.html">Go »</a>
      </div>

      <div class="well">
        <h4><a href="sample-walkthrough">Sample Walkthrough</a></h4>
        <p>The sample walkthrough will walk through a sample STIX document at the XML level. It's meant for those working without the python-stix libraries either in other XML tooling or reading raw STIX XML.<p>
        <a class="btn btn-primary" href="sample-walkthrough">Go »</a>
      </div>

      <div class="well">
        <h4><a href="authoring-tutorial">Authoring Tutorial</a></h4>
        <p>The authoring tutorial builds on the sample walkthrough to help you produce the content that you've already seen represented. Again, it's meant for those working with XML in non-python-stix tooling or those writing XML by hand.</p>
        <a class="btn btn-primary" href="authoring-tutorial">Go »</a>
      </div>
    </div>
  </div>
  <h2>Further Reading</h2>
  <div class="row">
    <div class="col-md-6">
      <div class="well">
        <h4><a href="../validation">Validation</a></h4>
        <p>Checking whether STIX content is valid is an important part of helping to ensure compatibility. The STIX Validation rules outline how STIX documents can be validated against either STIX in general or against a specific profile.</p>

        <a class="btn btn-primary" href="../validation">Go »</a>
      </div>

      <div class="well">
        <h4><a href="../suggested-practices">Suggested Practices</a></h4>
        <p>Suggested practices (often called best practices) are guidelines that will help you create STIX content that conforms to the STIX design goals and ensures the best compatibility with other STIX tooling.</p>

        <a class="btn btn-primary" href="../suggested-practices">Go »</a>
      </div>

      <div class="well">
        <h4><a href="../security-considerations">Security Considerations</a></h4>
        <p>Security considerations are a list of security issues that might arise when processing STIX content. The guide is non-exhaustive and does not take the place of security coding practices or other security processes but can be a good starting point.</p>

        <a class="btn btn-primary" href="../security-considerations">Go »</a>
      </div>
    </div>
    <div class="col-md-6">
      <div class="well">
        <h4><a href="../utilities">Utilities</a></h4>
        <p>The utilities page has information on both STIX-provided and community-provided utilities for working with STIX. It includes both user-level utilities such as visualization tools and developer-focused tooling such as bindings and APIs.</p>

        <a class="btn btn-primary" href="../utilities">Go »</a>
      </div>

      <div class="well">
        <h4><a href="../profiles">Profiles</a></h4>
        <p>STIX Profiles are a mechanism to allow communities of interest to define how they intend to use STIX. They're most often used to define which parts of the STIX/CybOX data models are in scope.</p>

        <a class="btn btn-primary" href="../profiles">Go »</a>
      </div>

      <div class="well">
        <h4><a href="../idioms">Idioms</a></h4>
        <p>STIX idioms describe how common patterns in threat intelligence (for example, C2 IPs for a trojan) are represented in STIX. They're similar to programming language idioms in that they document common patterns for representing content in STIX.</p>

        <a class="btn btn-primary" href="../idioms">Go »</a>
      </div>
    </div>
  </div>
</div>

## Contact Us!

We're always happy to set up either teleconferences or in-person meetings (in the Boston, MA and Washington, DC area) to go through an introductory session, a more in-depth training/development session, or to walk you through how to map your existing content into STIX. If that's something you're interested in, reach out to us at [stix@mitre.org](mailto:stix@mitre.org) and let us know.

We also host occasional training sessions that are free and open to the public. Information on these can be found on the [training](http://stix.mitre.org/training/index.html) page.
