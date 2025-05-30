/** @odoo-module **/

import {download} from "@web/core/network/download"
import {registry} from "@web/core/registry"

async function aerooReportHandler (action, options, env){
    let cloned_action = _.clone(action);
    if (action.report_type === "aeroo"){
        const type = "aeroo";
        let url_ = `/report/${type}/${action.report_name}`;
        const actionContext = action.context || {};
        if (cloned_action.context.active_ids) {
            url_ += "/" + cloned_action.context.active_ids.join(',');
            // odoo does not send context if no data, but I find it quite useful to send it regardless data or no data
            url_ += "?context=" + encodeURIComponent(JSON.stringify(cloned_action.context));
        } else {
            url_ += "?options=" + encodeURIComponent(JSON.stringify(cloned_action.data));
            url_ += "&context=" + encodeURIComponent(JSON.stringify(cloned_action.context));
        }
        // esto es mas parecido a en otros modulos pero hace que, por ej, nuestro reporte de deuda o de catalogo, donde mandamos
        // variables por contexto, dejen de funcionar
        // if (action.data && JSON.stringify(action.data) !== "{}") {
        //     const options_ = encodeURIComponent(JSON.stringify(action.data));
        //     const context_ = encodeURIComponent(JSON.stringify(actionContext));
        //     url_ += `?options=${options_}&context=${context_}`;
        // } else {
        //     if (actionContext.active_ids) {
        //         url_ += `/${actionContext.active_ids.join(",")}`;
        //     }
        //     if (type === "html") {
        //         const context = encodeURIComponent(
        //             JSON.stringify(env.services.user.context)
        //         );
        //         url_ += `?context=${context}`;
        //     }
        // }
        // COPY actionManager._triggerDownload
        env.services.ui.block();
        try {
            await download({
                url: "/report/download",
                data: {
                    data: JSON.stringify([url_, action.report_type]),
                    context: JSON.stringify(env.services.user.context),
                },
            });
        } finally {
            env.services.ui.unblock();
        }
        const onClose = options.onClose;
        if (action.close_on_report_download) {
            return env.services.action.doAction(
                {type: "ir.actions.act_window_close"},
                {onClose}
            );
        } else if (onClose) {
            onClose();
        }
        // DIFF: need to inform success to the original method. Otherwise it
        // will think our hook function did nothing and run the original
        // method.
        return Promise.resolve(true);
    }
}

registry.category("ir.actions.report handlers").add("aeroo_handler", aerooReportHandler);
