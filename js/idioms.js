function filter_idiom_table(by_tag) {
    if (by_tag === "None") {
        $("#idiom-table > tbody > tr").show();
    } else {
        $("#idiom-table > tbody > tr:has('span[data-tag=\"" + by_tag + "\"]')").show();
        $("#idiom-table > tbody > tr:not(:has('span[data-tag=\"" + by_tag + "\"]'))").hide();
    }
}

$(document).ready(function() {
    $("button[data-toggle='popover']").popover()
    $("#tag-filterer > li > a.tag-filter").click(function() {
        var label = this.textContent.trim();
        filter_idiom_table(label);
    })
    
    var idiom_table = $("#idiom-table");
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
    
    if (window.location.hash) {
        filter_idiom_table(window.location.hash.substring(1));
    }
});
