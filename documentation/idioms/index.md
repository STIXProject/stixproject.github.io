---
layout: flat
title: STIX Idioms
active: idioms
---

The idioms on this page provide guidance on how to represent common cyber threat
information in STIX. They are grouped based on the situation in which they would
be useful, as well as by the STIX types that they use.  **The same idiom may
appear in one or more sections.**

<div class="row idiom-row">
  <div class="col-md-6">
    <div class="idiom-header" id="c2">
      <h3>Command and Control (C2)</h3>
    </div>
    {% include tag_list.html tag="c2" %}

    <div class="idiom-header" id="malware">
      <img src="/images/Malware.png" class="component-img" alt="Malware Icon">
      <h3>Malware</h3>
    </div>
    {% include tag_list.html tag="malware" %}
  </div>
  <div class="col-md-6">
    <div class="idiom-header" id="victim">
      <img src="/images/Victim Targeting.png" class="component-img" alt="Victim Targeting Icon">
      <h3>Victim Targeting</h3>
    </div>
    {% include tag_list.html tag="victim" %}

    <div class="idiom-header" id="package">
      <h3>Packaging</h3>
    </div>
    {% include tag_list.html tag="package" %}
  </div>
</div>

<hr />

<div class="row idiom-row">
  <div class="col-md-6">
    <div class="idiom-header" id="campaign">
      <img src="/images/Campaign.png" class="component-img" alt="Campaign Icon" />
      <h3>Campaign</h3>
    </div>
    {% include tag_list.html tag="campaign" %}

    <div class="idiom-header" id="coa">
      <img src="/images/Course of Action.png" class="component-img" alt="Course of Action Icon" />
      <h3>Course of Action</h3>
    </div>
    {% include tag_list.html tag="coa" %}

    <div class="idiom-header" id="exploit_target">
      <img src="/images/Exploit Target.png" class="component-img" alt="Exploit Target Icon" />
      <h3>Exploit Target</h3>
    </div>
    {% include tag_list.html tag="exploit_target" %}

    <div class="idiom-header" id="incident">
      <img src="/images/Incident.png" class="component-img" alt="Incident Icon" />
      <h3>Incident</h3>
    </div>
    {% include tag_list.html tag="incident" %}
  </div>
  <div class="col-md-6">
    <div class="idiom-header" id="indicator">
      <img src="/images/Indicator.png" class="component-img" alt="Indicator Icon" />
      <h3>Indicator</h3>
    </div>
    {% include tag_list.html tag="indicator" %}

    <div class="idiom-header" id="threat_actor">
      <img src="/images/Threat Actor.png" class="component-img" alt="Threat Actor Icon" />
      <h3>Threat Actor</h3>
    </div>
    {% include tag_list.html tag="threat_actor" %}

    <div class="idiom-header" id="ttp">
      <img src="/images/TTP.png" class="component-img" alt="TTP Icon" />
      <h3 name="ttp">TTP</h3>
    </div>
    {% include tag_list.html tag="ttp" %}
  </div>
</div>
