/** @odoo-module **/

import { Component } from "@odoo/owl";
//import {session } from "web.session";
const session = require("web.session");
//import { Layout } from "@web/search/layout";
//import { getDefaultConfig } from "@web/views/view";

export class Dashboard extends Component {
    setup() {
        console.log(this,session)

        // args = [route,params,settings={}]
        const statistics = session.rpc('/my/statistics')
        console.log(statistics)
        statistics.then((stats) => console.log(stats))
        /*
        this.rpc = useService("rpc"); // for calls to the server
        /*
        onWillStart(async () => {
            const result = await this.rpc("/my/usage", {a: 1, b: 2});
            console.log(result);
        });
        */
    }
}

//Dashboard.components = { Layout };
Dashboard.template = "solid.dashboard";
