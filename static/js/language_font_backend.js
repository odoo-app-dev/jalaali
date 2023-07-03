odoo.define('odoo_jalaali.language_font', function (require) {
    "use strict";
    var core = require('web.core');
    var time = require('web.time');
    var session = require('web.session');
    var _t = core._t;
    if(!session.is_frontend){
        console.log(session)
        if(session.user_context.lang == 'fa_IR'){
                            const head = document.querySelector('head');
                    head.innerHTML += `
                    <style>
                        body{
                            font-family: IRANSans;
                        }
                        h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
                            font-family: IRANSans;

                        }
                        .dropdown-item, .note-editable, .odoo-editor-editable{
                            font-family: IRANSans !important;
                        }
                        .oe_form_field_html{
                            font-family: IRANSans !important;
                        }

                        p, td, th, div{
                            font-family: IRANSans !important;
                        }

                    </style>
                    `

        }
    }
});