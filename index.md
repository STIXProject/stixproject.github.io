---
layout: flat
title: STIX Project Documentation
tagline: User and developer documentation for STIX
no_in_page_title: true
---

<div class="row">
  <div class="col-md-5">
    <h1 id="logo">STIX <img src="/images/stix.gif" alt="STIX Logo" /></h1>
    <div id="carousel" class="carousel slide" data-ride="carousel" data-interval="10000">
      <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
        <li data-target="#carousel" data-slide-to="7"></li>
        <li data-target="#carousel" data-slide-to="8"></li>
        <li data-target="#carousel" data-slide-to="9"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div class="item active">
          <img src="/images/sample.png" alt="STIX" class="component-img"/>
          <div><strong>STIX</strong> is a language for structuring and representing cyber threat intelligence. It consists of definitions of 8 key concepts in cyber threat intelligence and the relationships between them. <a href="/data-model/{{site.current_version}}/">Learn more.</a></div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/indicator/IndicatorType/"><img src="/images/Indicator.png" alt="Indicator" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/indicator/IndicatorType/"><strong>Indicators</strong></a> describe patterns of malicious activity to look for along with context for what it means if you see them.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/ttp/TTPType/"><img src="/images/TTP.png" alt="TTP" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/ttp/TTPType/"><strong>TTPs</strong></a> describe tactics and techniques of the adversary, such as leveraged <a href="/data-model/{{site.current_version}}/ttp/AttackPatternType/">attack patterns</a>, <a href="/data-model/{{site.current_version}}/ttp/MalwareInstanceType/">malware</a>, <a href="/data-model/{{site.current_version}}/ttp/ToolsType/">tools</a>, <a href="/data-model/1.1.1/ttp/InfrastructureType/">infrastructure</a>, and <a href="/data-model/{{site.current_version}}/ttp/VictimTargetingType/">victim targeting</a>.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/incident/IncidentType/"><img src="/images/Incident.png" alt="Incident" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/incident/IncidentType/"><strong>Incidents</strong></a> describe cybersecurity incidents and their relationships with other parts of the STIX architecture.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/cybox/ObservableType/"><img src="/images/Observable.png" alt="Observable" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/cybox/ObservableType/"><strong>Observables</strong></a> describe patterns or instances of things you might see in cyber, such as IP addresses, files, registry keys, and e-mails.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/campaign/CampaignType/"><img src="/images/Campaign.png" alt="Campaign" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/campaign/CampaignType/"><strong>Campaigns</strong></a> describe ongoing patterns of behavior by an adversary.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/ta/ThreatActorType/"><img src="/images/Threat Actor.png" alt="Threat Actor" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/ta/ThreatActorType/"><strong>Threat Actors</strong></a> describe identity and other information about the adversary.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/et/ExploitTargetType/"><img src="/images/Exploit Target.png" alt="Exploit Target" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/et/ExploitTargetType/"><strong>Exploit Targets</strong></a> describe vulnerabilities and mis-configurations that malicious actors use to target systems and networks.</div>
        </div>
        <div class="item">
          <a href="/data-model/{{site.current_version}}/coa/CourseOfActionType/"><img src="/images/Course of Action.png" alt="Course of Action" class="component-img"/></a>
          <div><a href="/data-model/{{site.current_version}}/coa/CourseOfActionType/"><strong>Courses of Action</strong></a> describe actions that are taken or might be taken to mitigate threat activity.</div>
        </div>
        <div class="item">
          <a href="http://us-cert.gov/taxii"><img src="/images/dhs.jpg" alt="DHS" class="component-img"/></a>
          <div><a href="http://us-cert.gov/taxii"><strong>DHS</strong></a> leads the STIX project in an effort to increase capability and interoperability in the cyber threat intelligence space.</div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-md-1 spacer"></div>
  <div class="col-md-6 front-matter">
    <h2>What is STIX?</h2>
    <p>STIX (Structured Threat Information eXpression) is a structured language for describing cyber threat intelligence.</p>
    <a class="btn btn-primary btn-lg" href="http://stix.mitre.org/language/version1.1.1/">Download Latest Release</a>
    <h2>Who is STIX?</h2>
    <p>You are. STIX is an open, community-driven effort sponsored by DHS.</p>
    <a class="btn btn-primary btn-lg" href="http://stix.mitre.org/community/registration.html">Join the Conversation</a>
  </div>
</div>

<hr id="fold" />

<div class="row">
  <div class="col-md-4">
    <h3>Tutorials</h3>
    <p>Follow along with our guided tutorials to learn about the STIX data model
       and how to use it.</p>
    <p><a class="btn btn-primary" role="button" href="/getting-started">Documentation »</a></p>
  </div>
  <div class="col-md-4">
    <h3>Examples and Patterns</h3>
    <p>See examples of common design patterns in STIX and
    learn how to create and understand idiomatic STIX content.</p>
    <p><a class="btn btn-primary" role="button" href="/documentation/idioms">Idioms »</a></p>
  </div>
  <div class="col-md-4">
    <h3>Documentation</h3>
    <p>Learn about tools that support STIX, suggested practices for using STIX, and other in-depth
    documentation.</p>
    <p><a class="btn btn-primary" role="button" href="/documentation">Documentation »</a></p>
  </div>
</div>

<hr />

<p class="lead text-center">
	Have questions, comments, or feedback? Want to set up a teleconference or in-person meeting?
	<br/>
	<strong>Reach out to us at <a href="mailto:stix-taxii@hq.dhs.gov">stix-taxii@hq.dhs.gov</a>!</strong>
</p>

<div class="row">
    <div class="col-md-4">
      <h3 class="text-center">Teleconferences</h3>
	  <div class="contact-icon">
		  <span class="glyphicon glyphicon-earphone">
		  </span>
	  </div>
      <p>We're always happy to set up a teleconference to go through an introductory session, a more in-depth training/development session, or to walk you through how to map your existing content into STIX.</p>
	  <p>Get in touch with us via email to arrange one!</p>
    </div>
    <div class="col-md-4">
      <h3 class="text-center">In-Person Meetings</h3>
	  <div class="contact-icon">
		  <span class="glyphicon glyphicon-user">
		  </span>
	  </div>
      <p>Prefer an in-person meeting? We can meet with you in person for any of the purposes we would also cover via teleconference. Send us an email to schedule a meeting.</p>
    </div>
    <div class="col-md-4">
      <h3 class="text-center">Training Sessions</h3>
	  <div class="contact-icon">
		  <span class="glyphicon glyphicon-pencil">
		  </span>
	  </div>
	  <p>We host occasional training sessions that are free and open to the public. Information on these can be found on the <a href="http://stix.mitre.org/training/index.html">training</a> page.</p>
    </div>
</div>
