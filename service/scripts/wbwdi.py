"""
Use this to generate the json and es bulk from the wb wdi spreadsheet
"""
from octopus.lib import paths, dataobj, clcsv
import codecs, json, uuid
import esprit

wdi = paths.rel2abs(__file__, "..", "..", "data", "wbwdi", "wbwdi_selected.csv")
out = paths.rel2abs(__file__, "..", "..", "data", "wbwdi", "wbwdi_selected.json")
batch = paths.rel2abs(__file__, "..", "..", "data", "wbwdi", "wbwdi_selected.es")

class Indicator(dataobj.DataObj):
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "country" : {"coerce" : "unicode"},
                "indicator" : {"coerce" : "unicode"},
                "year" : {"coerce" : "integer"},
                "value" : {"coerce" : "float"}
            }
        }
        self._add_struct(struct)
        super(Indicator, self).__init__(raw, expose_data=True)

    def add_measure(self, year, value):
        if value is None:
            value = 0
        self._set_single("year", year, coerce=dataobj.to_int())
        self._set_single("value", value, coerce=dataobj.to_float())

class WDI(clcsv.SheetWrapper):
    EMPTY_STRING_AS_NONE = True

    HEADERS = {
        "Country Name" : "country",
        "Country Code" : "cc",
        "Indicator Name" : "indicator",
        "Indicator Code" : "ic"
    }

    COERCE = {
        "country" : dataobj.to_unicode(),
        "cc" : dataobj.to_unicode(),
        "indicator" : dataobj.to_unicode(),
        "ic" : dataobj.to_unicode()
    }

    DEFAULT_COERCE = [dataobj.to_float()]

sheet = WDI(wdi)

obs = []
for o in sheet.objects(beyond_headers=True):
    for k, v in o.iteritems():
        if k in WDI.HEADERS.values():
            continue
        if v is None:
            continue
        do = Indicator()
        do.country = o.get("country")
        do.indicator = o.get("indicator")
        do.add_measure(k, v)
        do.id = uuid.uuid4()
        obs.append(do.data)

bulk = esprit.raw.to_bulk(obs)

with codecs.open(out, "wb") as f:
    f.write(json.dumps(obs, indent=2))

with codecs.open(batch, "wb") as f:
    f.write(bulk)
