var wdi = {
    wdiEdge : false,

    create : function() {

        var e = edges.newEdge({
            selector: "#wdi",
            template: election.newWDITemplate(),
            search_url: octopus.config.search_base_url + "wdi/_search",
            baseQuery : es.newQuery({
                size: 0
            }),
            components : [
                // The country selector facet
                edges.newORTermSelector({
                    id: "country",
                    field : "counry.exact",
                    display: "Select one or more countries to compare",
                    size: 700,
                    lifecycle: "static",
                    renderer : edges.bs3.newORTermSelectorRenderer({
                        showCount: false,
                        hideEmpty: false,
                        open: true,
                        togglable: false
                    })
                }),
                // the indicator selector facet
                edges.RefiningANDTermSelector({
                    id: "indicators",
                    field: "indicator.exact",
                    display: "Indicator",
                    size: 20,
                    orderBy: "term",
                    orderDir: "asc"
                }),
                // indicator line chart
                edges.newSimpleLineChart({
                    id: "indicator-series",
                    aggregations : [
                        es.newTermsAggregation({
                            raw: {
                                "countries": {
                                    "terms": { "field": "country.exact" },
                                    "aggs": {
                                        "years": {
                                            "terms": {"field": "year"},
                                            "aggs": {
                                                "values": {
                                                    "stats": {"field": "value"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        })
                    ],
                    dataFunction : edges.ChartDataFunctions.termsStats({
                        useAggregations : [],
                        seriesKeys : {},
                        seriesFor : {}
                    })
                })
            ]
        });

        election.electionEdge = e;
    },

    newWDITemplate : function(params) {
        if (!params) { params = {} }
        wdi.WDITemplate.prototype = edges.newTemplate(params);
        return new wdi.WDITemplate(params);
    },
    WDITemplate : function(params) {
        this.namespace = "wdi-template";

        this.draw = function(edge) {
            this.edge = edge;

            var frag = '<div class="row">\
                <div class="col-md-9"><div id="indicators"></div></div>\
            </div>\
            <div class="row">\
                <div class="col-md-9">\
                    <div id="indicator-series"></div>\
                </div>\
                <div class="col-md-3">\
                    <div id="countries"></div>\
                </div>\
            </div>';

            edge.context.html(frag);
        }
    }
};


jQuery(document).ready(function($) {
    election.create();
});