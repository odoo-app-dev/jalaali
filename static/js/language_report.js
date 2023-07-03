odoo.define('odoo_jalaali.WebClient', function (require) {

"use strict";
            console.log('odoo_jalaali.WebClient')

    var AbstractWebClient = require('web.AbstractWebClient');

    AbstractWebClient = AbstractWebClient.include({

        start: function (parent) {
            console.log('odoo_jalaali.WebClient start')
            this.set('title_part', {"zopenerp": "Your title!"});

            this._super(parent);

        },

    });

});