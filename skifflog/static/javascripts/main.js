requirejs.config({
    shim: {
        'foundation/jquery.foundation.topbar': {
            deps: ['jquery'],
        },
        'foundation/jquery.cookie': {
            deps: ['jquery']
        },
        'foundation/jquery.event.move': {
            deps: ['jquery']
        },
        'foundation/jquery.event.swipe': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.accordion': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.alerts': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.buttons': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.clearing': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.forms': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.joyride': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.magellan': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.mediaQueryToggle': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.navigation': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.orbit': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.reveal': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.tabs': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.tooltips': {
            deps: ['jquery']
        },
        'foundation/jquery.foundation.topbar': {
            deps: ['jquery']
        },
        'foundation/jquery.offcanvas': {
            deps: ['jquery']
        },
        'foundation/jquery.placeholder': {
            deps: ['jquery']
        },
        'foundation/app': {
            deps: [
                'foundation/jquery.cookie',
                'foundation/jquery.event.move',
                'foundation/jquery.event.swipe',
                'foundation/jquery.foundation.accordion',
                'foundation/jquery.foundation.alerts',
                'foundation/jquery.foundation.buttons',
                'foundation/jquery.foundation.clearing',
                'foundation/jquery.foundation.forms',
                'foundation/jquery.foundation.joyride',
                'foundation/jquery.foundation.magellan',
                'foundation/jquery.foundation.mediaQueryToggle',
                'foundation/jquery.foundation.navigation',
                'foundation/jquery.foundation.orbit',
                'foundation/jquery.foundation.reveal',
                'foundation/jquery.foundation.tabs',
                'foundation/jquery.foundation.tooltips',
                'foundation/jquery.foundation.topbar',
                'foundation/jquery.offcanvas',
                'foundation/jquery.placeholder',
            ]
        }
    }
});
require([ 'jquery'
        , 'skifflog'
        , 'foundation/jquery.cookie'
        , 'foundation/jquery.event.move'
        , 'foundation/jquery.event.swipe'
        , 'foundation/jquery.foundation.accordion'
        , 'foundation/jquery.foundation.alerts'
        , 'foundation/jquery.foundation.buttons'
        , 'foundation/jquery.foundation.clearing'
        , 'foundation/jquery.foundation.forms'
        , 'foundation/jquery.foundation.joyride'
        , 'foundation/jquery.foundation.magellan'
        , 'foundation/jquery.foundation.mediaQueryToggle'
        , 'foundation/jquery.foundation.navigation'
        , 'foundation/jquery.foundation.orbit'
        , 'foundation/jquery.foundation.reveal'
        , 'foundation/jquery.foundation.tabs'
        , 'foundation/jquery.foundation.tooltips'
        , 'foundation/jquery.foundation.topbar'
        , 'foundation/jquery.offcanvas'
        , 'foundation/jquery.placeholder'
        , 'foundation/app'
        ], function($, skifflog) {
    $(function() {
        skifflog(
            $('input[name=csrfmiddlewaretoken]').val(),
            $('#arrive'),
            $('#depart'),
            $('#timer'),
            $('#comment')
        );
        $('ul.errorlist li').addClass('alert label');
    });
});