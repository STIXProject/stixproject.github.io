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
		<div class="panel-group" id="leftAccordion">
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<span class="img-spacer"></span>
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#c2">
		          Command and Control (C2)
		        </a>
		      </h2>
		    </div>
		    <div id="c2" class="panel-collapse collapse in">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="c2" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
      			<img src="/images/Campaign.png" width="36px" alt="Campaign Icon" />
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#campaign">
		          Campaign
		        </a>
		      </h2>
		    </div>
		    <div id="campaign" class="panel-collapse collapse">
		      <div class="panel-body">
    			  {% include tag_list.html tag="campaign" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
      			<img src="/images/Course of Action.png" width="36px" alt="Course of Action Icon" />
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#coa">
		          Course of Action
		        </a>
		      </h2>
		    </div>
		    <div id="coa" class="panel-collapse collapse">
		      <div class="panel-body">
    			  {% include tag_list.html tag="coa" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
      			<img src="/images/Exploit Target.png" width="36px" alt="Exploit Target Icon" />
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#et">
		          Exploit Target
		        </a>
		      </h2>
		    </div>
		    <div id="et" class="panel-collapse collapse">
		      <div class="panel-body">
    			  {% include tag_list.html tag="exploit_target" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
      			<img src="/images/Incident.png" width="36px" alt="Incident Icon" />
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#incident">
		          Incident
		        </a>
		      </h2>
		    </div>
		    <div id="incident" class="panel-collapse collapse">
		      <div class="panel-body">
    			  {% include tag_list.html tag="incident" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-primary">
		    <div class="panel-heading">
		      <h2 class="panel-title">
      			<img src="/images/Indicator.png" width="36px" alt="Indicator Icon" />
		        <a data-toggle="collapse" data-parent="#leftAccordion" href="#indicator">
		          Indicator
		        </a>
		      </h2>
		    </div>
		    <div id="indicator" class="panel-collapse collapse">
		      <div class="panel-body">
    			  {% include tag_list.html tag="indicator" %}
		      </div>
		    </div>
		  </div>
		</div>
	</div>
	<div class="col-md-6">
		<div class="panel-group" id="rightAccordion">
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<span class="img-spacer"></span>
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#packaging">
				  Packaging
		        </a>
		      </h2>
		    </div>
		    <div id="packaging" class="panel-collapse collapse in">
		      <div class="panel-body">
		    {% include tag_list.html tag="package" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<img src="/images/Malware.png" width="36px" alt="Malware Icon">
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#malware">
				  Malware
		        </a>
		      </h2>
		    </div>
		    <div id="malware" class="panel-collapse collapse">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="malware" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<img src="/images/Observable.png" width="36px" alt="Observable Icon">
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#observable">
				  Observable
		        </a>
		      </h2>
		    </div>
		    <div id="observable" class="panel-collapse collapse">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="observable" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<img src="/images/Threat Actor.png" width="36px" alt="Threat Actor Icon">
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#threatactor">
				  Threat Actor
		        </a>
		      </h2>
		    </div>
		    <div id="threatactor" class="panel-collapse collapse">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="threat_actor" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<img src="/images/TTP.png" width="36px" alt="TTP Icon">
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#ttp">
				  TTP
		        </a>
		      </h2>
		    </div>
		    <div id="ttp" class="panel-collapse collapse">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="ttp" %}
		      </div>
		    </div>
		  </div>
		  <div class="panel panel-info">
		    <div class="panel-heading">
		      <h2 class="panel-title">
				<img src="/images/Victim Targeting.png" width="36px" alt="Victim Targeting Icon">
		        <a data-toggle="collapse" data-parent="#rightAccordion" href="#collapseThree">
					Victim Targeting
		        </a>
		      </h2>
		    </div>
		    <div id="collapseThree" class="panel-collapse collapse">
		      <div class="panel-body">
		    	  {% include tag_list.html tag="victim" %}
		      </div>
		    </div>
		  </div>
		</div>
	</div>
</div>
