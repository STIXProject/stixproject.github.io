---
layout: flat_for_idioms
title: STIX Idioms
---

<link href="/css/idioms.css" rel="stylesheet"/>


An `idiom` is an example of using STIX for a typical use case, and includes sample Python code and XML.

<div class="row">
  <div class="col-md-12">
    {% assign use_case_list = "Command and Control,Malware,Packaging,Victim Targeting" %}
    {% assign construct_list = "Campaign,Course of Action,Exploit Target,Incident,Indicator,Observable,Threat Actor,TTP" %}
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
                  <li role="presentation" class="dropdown-header">Use Cases</li>
                  {% assign use_cases = use_case_list | split:"," | sort %}
                  {% for use_case in use_cases %}
                    <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{use_case}}</a></li>
                  {% endfor %}
                  <li role="presentation" class="divider"></li>
                  <li role="presentation" class="dropdown-header">STIX Types</li>
                  {% assign constructs = construct_list | split:"," | sort %}
                  {% for construct in constructs %}
                    <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{construct}}</a></li>
                  {% endfor %}
                </ul>
              </small>
            </h3>
          </th>
          <th>
            <h3>Use Cases</h3>
          </th>
          <th>
            <h3>STIX Types</h3>
          </th>
          <th>
            <h3>Description</h3>
          </th>
        </tr>
      </thead>
      <tbody>
        {% for page in site.pages %}
          {% if page.use_cases | size != 0  or page.constructs | size != 0 %}
            <tr>
              <td>
                <h4>
                  <a href='{{page.url | remove: "/index.html"}}'>{{page.title}}</a>
                </h4>
              </td>
              <td>
                <span class="tag-labels-container">
                  {% for use_case in page.use_cases %}
                    {% assign tag = use_case | replace:' ','-' | downcase %}
                    <span data-tag="{{use_case}}" class="label label-{{tag}}">
                      {{use_case}}
                    </span>
                  {% endfor %}
                </span>
              </td>
              <td>
                {% for construct in page.constructs %}
                {% assign tag = construct | replace:' ','-' | downcase %}
                <span class="idiom-construct" data-tag="{{construct}}" data-toggle="tooltip"
                    data-placement="top" title="{{construct}}">
                  <img src="/images/{{construct}}.png" width="40px" alt="{{construct}} Icon" />
                </span>
                {% endfor %}
              </td>
              <td>
                <button class="btn btn-info" data-toggle="popover" data-placement="left" data-trigger="hover" title="{{page.title}}" data-content="{{page.summary | escape}}">
                  <span class="glyphicon glyphicon-question-sign"></span>
                </button>
              </td>
            </tr>
          {% endif %}
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>
