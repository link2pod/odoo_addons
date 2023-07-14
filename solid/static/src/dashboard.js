/** @odoo-module **/

import { Component } from "@odoo/owl";
//import {session } from "web.session";
const session = require("web.session");
//import { Layout } from "@web/search/layout";
//import { getDefaultConfig } from "@web/views/view";

export class Dashboard extends Component {
    async setup() {
        console.log(this,session)
        console.log(session.user_context, session.userContext)

        // args = [route,params,settings={}]
        const statistics = await session.rpc('/my/statistics')
        console.log(statistics)
        const web_id = statistics.web_id
        this.web_id = web_id
    }
}

//Dashboard.components = { Layout };
Dashboard.template = "solid.dashboard";
