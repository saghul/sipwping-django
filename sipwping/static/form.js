function cb_submit(data) {
    var status = $('div#_status')
    status.empty();
    if ('error' in data) {
        var s = sprintf('<div class=\"notice _status\">%s</div>', data.error);
    } else {
        if (data.status.code > 199 && data.status.code < 300) {
            var s = sprintf('<div class=\"success _status\">%d %s</div>', data.status.code, data.status.reason);
        } else {
            var s = sprintf('<div class=\"error _status\">%d %s</div>', data.status.code, data.status.reason);
        }
    }
    status.append(s);
}

function ajax_submit() {
    var status = $('div#_status')
    status.empty();
    status.append('<div class=\"_status _status_loading\">&nbsp;</div>');
    var data = $('form#search_form').serializeObject();
    Dajaxice.sipwping.ajax_form(cb_submit, {'form':data});
}

$(document).ready(function() {
    $('form#search_form').submit(function(e) {
        ajax_submit();
        e.preventDefault();
    });
});

