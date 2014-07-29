---
layout: flat
title: STIX Idioms
---

<link href="/css/idioms.css" rel="stylesheet"/>

The idioms on this page provide guidance on how to represent common cyber threat
information in STIX. They are grouped based on the situation in which they would
be useful, as well as by the STIX types that they use.  

<p class="alert alert-warning"><strong>Note: </strong> the same idiom may appear in one or more sections!</p>

<div class="row">
  <div class="col-md-6">
    <div class="panel-group">
      <div id="c2" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <span class="img-spacer"></span>
            <a data-toggle="collapse" href="#c2-body">
              Command and Control (C2)
            </a>
          </h2>
        </div>
        <div id="c2-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="c2" %}
          </div>
        </div>
      </div>
      <div id="campaign" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Campaign.png" width="36px" alt="Campaign Icon" />
            <a data-toggle="collapse" href="#campaign-body">
              Campaign
            </a>
          </h2>
        </div>
        <div id="campaign-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="campaign" %}
          </div>
        </div>
      </div>
      <div id="coa" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Course of Action.png" width="36px" alt="Course of Action Icon" />
            <a data-toggle="collapse" href="#coa-body">
              Course of Action
            </a>
          </h2>
        </div>
        <div id="coa-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="coa" %}
          </div>
        </div>
      </div>
      <div id="exploit-target" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Exploit Target.png" width="36px" alt="Exploit Target Icon" />
            <a data-toggle="collapse" href="#exploit-target-body">
              Exploit Target
            </a>
          </h2>
        </div>
        <div id="exploit-target-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="exploit_target" %}
          </div>
        </div>
      </div>
      <div id="incident" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Incident.png" width="36px" alt="Incident Icon" />
            <a data-toggle="collapse" href="#incident-body">
              Incident
            </a>
          </h2>
        </div>
        <div id="incident-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="incident" %}
          </div>
        </div>
      </div>
      <div id="indicator" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Indicator.png" width="36px" alt="Indicator Icon" />
            <a data-toggle="collapse" href="#indicator-body">
              Indicator
            </a>
          </h2>
        </div>
        <div id="indicator-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="indicator" %}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <div class="panel-group">
      <div id="packaging" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
          <span class="img-spacer"></span>
            <a data-toggle="collapse" href="#packaging-body">
              Packaging
            </a>
          </h2>
        </div>
        <div id="packaging-body" class="panel-collapse collapse in">
          <div class="panel-body">
        {% include tag_list.html tag="package" %}
          </div>
        </div>
      </div>
      <div id="malware" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Malware.png" width="36px" alt="Malware Icon">
            <a data-toggle="collapse" href="#malware-body">
              Malware
            </a>
          </h2>
        </div>
        <div id="malware-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="malware" %}
          </div>
        </div>
      </div>
      <div id="observable" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Observable.png" width="36px" alt="Observable Icon">
            <a data-toggle="collapse" href="#observable-body">
              Observable
            </a>
          </h2>
        </div>
        <div id="observable-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="observable" %}
          </div>
        </div>
      </div>
      <div id="threat-actor" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Threat Actor.png" width="36px" alt="Threat Actor Icon">
            <a data-toggle="collapse" href="#threat-actor-body">
              Threat Actor
            </a>
          </h2>
        </div>
        <div id="threat-actor-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="threat_actor" %}
          </div>
        </div>
      </div>
      <div id="ttp" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/TTP.png" width="36px" alt="TTP Icon">
            <a data-toggle="collapse" href="#ttp-body">
              TTP
            </a>
          </h2>
        </div>
        <div id="ttp-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="ttp" %}
          </div>
        </div>
      </div>
      <div id="victim" class="panel panel-primary">
        <div class="panel-heading">
          <h2 class="panel-title">
            <img src="/images/Victim Targeting.png" width="36px" alt="Victim Targeting Icon">
            <a data-toggle="collapse" href="#victim-body">
              Victim Targeting
            </a>
          </h2>
        </div>
        <div id="victim-body" class="panel-collapse collapse in">
          <div class="panel-body">
            {% include tag_list.html tag="victim" %}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
