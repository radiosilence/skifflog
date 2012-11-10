define(['jquery', 'foundation/jquery.cookie'], function($) {
    var csrf_token;
    function api_request(url, data, method, callback) {
        data = data || {}
        method = method || 'POST';
        callback = callback || function() {
            document.location.reload(true);
        };
        data.csrfmiddlewaretoken = csrf_token;
        $.ajax(url, {
            dataType: 'json',
            data: data,
            success: callback,
            failure: console.log,
            type: method,
        });
    }
    function pad(number, length) {
        var str = '' + number;
        while (str.length < length) {
            str = '0' + str;
        }
        return str;
    }
    function get_delta(start, end) {
        var start = start.getTime() / 1000;
        var end = end.getTime() / 1000;
        delta = end - start;
        var ms = Math.round((delta % 1) * 1000) - 1;
        var days = Math.round(delta / 86400);
        delta = delta % 86400;
        var hours = Math.round(delta / 3600);
        delta = delta % 3600;
        var minutes = Math.round(delta / 60);
        delta = delta % 60;
        var seconds = Math.round(delta);
        if (days == 0) {
            days = '';
        } else if (days == 1) {
            days = days + ' day, ';
        } else {
            days = days + ' days, '
        }
        return days
            + hours + ':'
            + pad(minutes, 2) + ':'
            + pad(seconds, 2)
            // + '.' + pad(ms, 3);
    }
    return function(
        csrfmiddlewaretoken,
        $arrive,
        $depart,
        $timer,
        $comment
    ) {
        var visit;
        csrf_token = csrfmiddlewaretoken;

        function set_arrive() {
            api_request('/arrive/');
        }
        function set_depart() {
            api_request('/depart/', {
                comment: $comment.val(),
            })
        }
        function update_timer() {
            if (!visit) {
                api_request('/check/', {}, 'GET', function(data) {
                    visit = data.visit;
                });
            } else {
                $timer.text(get_delta(new Date(visit), new Date()))
            }
        }
        window.ut = update_timer;
        if ($arrive.length > 0) {
            $arrive.on('click', function(event) {
                event.preventDefault();
                set_arrive();
            });
        }
        if ($depart.length > 0) {
            $depart.on('click', function(event) {
                event.preventDefault();
                set_depart();
            });
            setInterval(update_timer, 500);
        }
    }
});