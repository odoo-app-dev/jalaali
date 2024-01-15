odoo.define('odoo_jalaali.language_font_frontend', function (require) {
    "use strict";
    const publicWidget = require('web.public.widget');
    var core = require('web.core');
    var session = require('web.session');
    var _t = core._t;


//$.when( $.ready ).then(function() {
//    console.log(' language_font_frontend ready');
//    $('body').on('click', function(e){
//        console.log(session);
//    });
//});



    publicWidget.registry.LanguageFont = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    start: function(){
        let self = this;

//        console.log(' language_font_frontend language:')
        return this._super.apply(this, arguments)
            .then(function(){
            let language;
            let fontFamily = 'IRANSans';
//            console.log('language_font WEBSITE:', session, self)

            if (session.is_frontend){
                var context;
                self.trigger_up('context_get', {
                    callback: function (ctx) {
                        context = ctx;
                    },
                });
            console.log(context)
            if(context.lang == 'fa_IR'){
                if(session.user_id){
                self._rpc({
                        model: 'res.config.settings',
                        method: 'get_language_font',
                        args: [[]],
                })
                .then(data => console.log('language_font_frontend', data))
                .catch(err => console.log('language_font_frontend', err));
                }
//                document.querySelector('body').style.fontFamily = fontFamily;
                    const head = document.querySelector('head');
                    head.innerHTML += `
                    <style>
                        body{
                            font-family: IRANSans;
                        }
                        h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
                            font-family: IRANSans;

                        }
                        pre{
                            direction: ltr !important;
                        }

                    </style>
                    `




                language = context.lang;



            }

            }
            })

    },

    });
    return publicWidget.registry.LanguageFont;

});