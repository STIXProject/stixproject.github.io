var typeSuggestor = new Bloodhound({
  datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name)},
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: window.typeSuggestions,
  limit: 10,
  sorter: function(a, b) {
    return a.name.length - b.name.length;
  }
});

typeSuggestor.initialize();

$('.doc-types').typeahead({
  minLength: 3,
  highlight: true,
  autoselect: true
},
{
  source: typeSuggestor.ttAdapter(),
  displayKey: 'name',
  templates: {
    suggestion: function(suggestion) {
      return "<p>" + suggestion.name + "<span class='subdued'>" + suggestion.schema + "</span></p>"
    }
  }
});

$('.doc-types').on('typeahead:selected', function(evt, suggestion) {
  document.location.href = window.location.protocol + "//" + window.location.host + suggestion.link;
});

$('#nav-version select').on('change', function() {
  var oldLocation = document.location.href;
  var newLocation = oldLocation.replace(/data-model\/[^\/]+\//, "data-model/" + $(this).val() + "/");
  document.location.href = newLocation;
});

$('table').addClass('table'); // Makes all tables bootstrap tables

$(document).ready(function() {
    $('.dropdown-toggle').dropdown()
    $('.coming-soon').tooltip()
    $('.idiom-construct').tooltip()
    $('#globe').tooltip()
});


$('#expand-all').click(function() { 
    var me = $(this);
    if ("collapsed" === me.data("allState")) {
        me.data("allState", "expanded");
        me.text("Hide all Examples");
        $(".toggleLink.collapsed").click();
    } else {
        me.data("allState", "collapsed");
        me.text("Show all Examples");
        $(".toggleLink:not(.collapsed)").click();
    }
});

$(".collapsible").on('hide.bs.collapse', changeText);
$(".collapsible").on('show.bs.collapse', changeText);

function changeText() {
    var me = $("[data-toggle='collapse'][href='#" + this.id + "']");
    var disabledText = me.data("disabledText");
    var enabledText = me.data("enabledText");
    if (disabledText) {
        me.data("disabledText", "");
        me.data("enabledText", me.text());
        me.text(disabledText);
    } else if (enabledText) {
        me.data("enabledText", "");
        me.data("disabledText", me.text());
        me.text(enabledText);
    }
}

$(function() {
  return $("h2, h3, h4, h5, h6").each(function(i, el) {
    var $el, icon, id;
    $el = $(el);
    id = $el.attr('id');
    icon = '<i class="glyphicon glyphicon-link"></i>';
    if (id) {
      return $el.prepend($("<a />").addClass("header-link").attr("href", "#" + id).html(icon));
    }
  });
});
