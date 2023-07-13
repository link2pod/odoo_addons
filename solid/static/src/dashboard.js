/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Layout } from "@web/search/layout";
import { getDefaultConfig } from "@web/views/view";

export class Dashboard extends Component {
    setup() {
        this.display = {
            controlPanel: { "top-right": false, "bottom-right": false },
        };
    }
}

Dashboard.components = { Layout };
Dashboard.template = "solid.dashboard";
