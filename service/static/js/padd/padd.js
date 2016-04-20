var padd = {
    paddEdge : false,

    create : function() {

        var e = edges.newEdge({
            selector: "#padd",
            template: padd.newPaddTemplate(),
            search_url: octopus.config.search_base_url + "constituencies/_search", // FIXME: we're actually not going to need to do any queries for this one
            baseQuery : es.newQuery({
                size: 0
            }),
            components : [
                edges.newMapView({
                    id: "states-map",
                    renderer : edges.d3.newGroupedUSStates({})
                })
            ]
        });

        padd.paddEdge = e;
    },



    newPaddTemplate : function(params) {
        if (!params) { params = {} }
        padd.PaddTemplate.prototype = edges.newTemplate(params);
        return new padd.PaddTemplate(params);
    },
    PaddTemplate : function(params) {
        this.namespace = "padd-template";

        this.draw = function(edge) {
            this.edge = edge;

            var frag = '<div class="row">\
                <div class="col-md-12">\
                    <div id="states-map"></div>\
                </div>\
            </div>';

            edge.context.html(frag);
        }
    }
};


jQuery(document).ready(function($) {
    padd.create();
});