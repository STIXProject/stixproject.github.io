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
})

$('table').addClass('table'); // Makes all tables bootstrap tables

$(document).ready(function() {
    $('.dropdown-toggle').dropdown()
    $('.coming-soon').tooltip()
    $("button[data-toggle='popover']").popover()
    $("#tag-filterer > li > a.tag-filter").click(function() {
        var label = this.textContent.trim();
        if (label === "None") {
            $("#idiom-table > tbody > tr").show();
        } else {
            $("#idiom-table > tbody > tr:has('span.label-" + label + "')").show();
            $("#idiom-table > tbody > tr:not(:has('span.label-" + label + "'))").hide();
        }
    })
    
    var idiom_table = $("#idiom-table");
    if (idiom_table.length > 0) {
        var rows = $(idiom_table).find('tbody > tr').get();
        rows.sort(function(a, b) {
            var keyA = $(a).find("td > h4 > a").text();
            var keyB = $(b).find("td > h4 > a").text();
            if (keyA > keyB) {
                return 1;
            } else if (keyA < keyB) {
                return -1;
            } else {
                return 0;
            }
        });
        $.each(rows, function(index, row) {
            $(idiom_table).children('tbody').append(row);
        });
    }
});
