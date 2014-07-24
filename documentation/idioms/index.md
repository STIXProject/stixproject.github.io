---
layout: flat
title: STIX Idioms
active: idioms
---

The idioms on this page provide guidance on how to represent common cyber threat
information in STIX. They are grouped based on the situation in which they would
be useful, as well as by the STIX types that they use.  **The same idiom may
appear in one or more sections.**


<div class="row">
  <div class="col-md-6">
    <h2>By Use Case</h2>
    <div class="well">
      <div id="c2">
        <h3>Command and Control (C2)</h3>
        {% include tag_list.html tag="c2" %}
      </div>

      <div id="malware">
        <h3>Malware</h3>
        <img src="/images/Malware.png" class="component-img" alt="Malware Icon">
        {% include tag_list.html tag="malware" %}
      </div>

      <div id="victim">
        <h3>Victim Targeting</h3>
        <img src="/images/Victim Targeting.png" class="component-img" alt="Victim Targeting Icon">
        {% include tag_list.html tag="victim" %}
      </div>
    </div>

    <h2>Other</h2>
    <div class="well">
      <div id="package">
        <h3>Package</h3>
        {% include tag_list.html tag="package" %}
      </div>
    </div>
  </div>

  <div class="col-md-6">
    <h2>By STIX Type</h2>
    <div class="well">
      <div id="campaign">
        <h3>Campaign</h3>
        <img src="/images/Campaign.png" class="component-img" alt="Campaign Icon" />
        {% include tag_list.html tag="campaign" %}
      </div>

      <div id="coa">
        <h3>Course of Action</h3>
        <img src="/images/Course of Action.png" class="component-img" alt="Course of Action Icon" />
        {% include tag_list.html tag="coa" %}
      </div>

      <div id="exploit_target">
        <h3>Exploit Target</h3>
        <img src="/images/Exploit Target.png" class="component-img" alt="Exploit Target Icon" />
        {% include tag_list.html tag="exploit_target" %}
      </div>

      <div id="incident">
        <h3>Incident</h3>
        <img src="/images/Incident.png" class="component-img" alt="Incident Icon" />
        {% include tag_list.html tag="incident" %}
      </div>

      <div id="indicator">
        <h3>Indicator</h3>
        <img src="/images/Indicator.png" class="component-img" alt="Indicator Icon" />
        {% include tag_list.html tag="indicator" %}
      </div>

      <div id="threat_actor">
        <h3>Threat Actor</h3>
        <img src="/images/Threat Actor.png" class="component-img" alt="Threat Actor Icon" />
        {% include tag_list.html tag="threat_actor" %}
      </div>

      <div id="ttp">
        <h3 name="ttp">TTP</h3>
        <img src="/images/TTP.png" class="component-img" alt="TTP Icon" />
        {% include tag_list.html tag="ttp" %}
      </div>
    </div>
  </div>
</div>
