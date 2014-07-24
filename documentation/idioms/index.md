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
    <div id="c2">
      <div class="idiom-header">
        <h3>Command and Control (C2)</h3>
      </div>
      {% include tag_list.html tag="c2" %}
    </div>

    <div id="malware">
      <div class="idiom-header">
        <img src="/images/Malware.png" class="component-img" alt="Malware Icon">
        <h3>Malware</h3>
      </div>
      {% include tag_list.html tag="malware" %}
    </div>
  </div>
  <div class="col-md-6">
    <div id="victim">
      <div class="idiom-header">
        <img src="/images/Victim Targeting.png" class="component-img" alt="Victim Targeting Icon">
        <h3>Victim Targeting</h3>
      </div>
      {% include tag_list.html tag="victim" %}
    </div>

    <div id="package">
      <div class="idiom-header">
        <h3>Packaging</h3>
      </div>
      {% include tag_list.html tag="package" %}
    </div>
  </div>
</div>

<hr />

<div class="row idiom-row">
  <div class="col-md-6">
    <div id="campaign">
      <div class="idiom-header">
        <img src="/images/Campaign.png" class="component-img" alt="Campaign Icon" />
        <h3>Campaign</h3>
      </div>
      {% include tag_list.html tag="campaign" %}
    </div>

    <div id="coa">
      <div class="idiom-header">
        <img src="/images/Course of Action.png" class="component-img" alt="Course of Action Icon" />
        <h3>Course of Action</h3>
      </div>
      {% include tag_list.html tag="coa" %}
    </div>

    <div id="exploit_target">
      <div class="idiom-header">
        <img src="/images/Exploit Target.png" class="component-img" alt="Exploit Target Icon" />
        <h3>Exploit Target</h3>
      </div>
      {% include tag_list.html tag="exploit_target" %}
    </div>

    <div id="incident">
      <div class="idiom-header">
        <img src="/images/Incident.png" class="component-img" alt="Incident Icon" />
        <h3>Incident</h3>
      </div>
      {% include tag_list.html tag="incident" %}
    </div>
  </div>
  <div class="col-md-6">
    <div id="indicator">
      <div class="idiom-header">
        <img src="/images/Indicator.png" class="component-img" alt="Indicator Icon" />
        <h3>Indicator</h3>
      </div>
      {% include tag_list.html tag="indicator" %}
    </div>

    <div id="threat_actor">
      <div class="idiom-header">
        <img src="/images/Threat Actor.png" class="component-img" alt="Threat Actor Icon" />
        <h3>Threat Actor</h3>
      </div>
      {% include tag_list.html tag="threat_actor" %}
    </div>

    <div id="ttp">
      <div class="idiom-header">
        <img src="/images/TTP.png" class="component-img" alt="TTP Icon" />
        <h3 name="ttp">TTP</h3>
      </div>
      {% include tag_list.html tag="ttp" %}
    </div>
  </div>
</div>
