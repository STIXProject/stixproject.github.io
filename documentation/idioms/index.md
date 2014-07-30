---
layout: flat_for_idioms
title: STIX Idioms
---

<link href="/css/idioms.css" rel="stylesheet"/>

The idioms on this page provide guidance on how to represent common cyber threat
information in STIX. They are grouped based on the situation in which they would
be useful, as well as by the STIX types that they use.  
<br/>
<span class="alert alert-info">
	Each idiom has labels indicating which constructs and use cases to which that idiom is adapted!
</span>

<div class="row">
  <div class="col-md-12">
    {% assign tag = "c2,campaign,coa,exploit_target,incident,indicator,package,malware,observable,threat_actor,ttp,victim" %}
    <table id="idiom-table" class="table table-striped">
      <thead>
        <tr>
          <th>
            <h3>Idiom
              <small class="dropdown">
                <button class="btn btn-info dropdown-toggle" type="button" id="filterMenu" data-toggle="dropdown">
                  Filter By... <span class="caret"></span>
                </button>
                <ul id="tag-filterer" class="dropdown-menu" role="menu" aria-labelledby="filterMenu">
                  <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">None</a></li>
                  <li role="presentation" class="divider"></li>
                  {% capture tag_list %}
                    {{include.tag}}
                  {% endcapture %}
                  {% assign tag_list = tag_list | split:"," | sort %}
                  {% for tag in tag_list %}
                    <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{tag}}</a></li>
                  {% endfor %}
                </ul>
              </small>
            </h3>
          </th>
          <th>
            <h3>Details</h3>
          </th>
        </tr>
      </thead>
      <tbody>
        {% for page in site.pages %}
          {% assign my_tags = "" %}
          {% assign tag_len = 0 %}
          {% for tag in page.tags %}
            {% if include.tag contains tag %}
              {% capture tag_len %}{{my_tags | size}}{% endcapture %}
              {% capture my_tags %}
                {% if tag_len != "0" %}
                  {{my_tags}}|
                {% endif %}
                {{tag}}
              {% endcapture %}
            {% endif %}
          {% endfor %}
          {% if tag_len != 0 %}
            <tr>
              <td>
                <h4>
                  <a href='{{page.url}}'>{{page.title}}</a>
                  <small>
                    <span class="tag-labels-container">
                      {% assign page_tags = page.tags | sort%}
                      {% for tag in page_tags %}
                        {% if include.tag contains tag %}
                          <span data-tag="{{tag}}" class="label label-{{tag}}">
                            {{tag}}
                          </span>
                        {% endif %}
                      {% endfor %}
                    </span>
                  </small>
                </h4>
              </td>
              <td>
                <button class="btn btn-info" data-toggle="popover" data-placement="left" data-trigger="hover" title="{{page.title}}" data-content="{{page.summary | escape}}">
                  <span class="glyphicon glyphicon-question-sign"><span>
                </button>
              </td>
            </tr>
          {% endif %}
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>
