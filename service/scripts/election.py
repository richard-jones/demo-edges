from octopus.lib import paths, dataobj, clcsv
import os, codecs, json, uuid
import esprit

d = paths.rel2abs(__file__, "..", "..", "data", "election")
rfa = os.path.join(d, "RESULTS FOR ANALYSIS.csv")
out = os.path.join(d, "constituencies.json")
batch = os.path.join(d, "constituencies.es")

class Constituency(dataobj.DataObj):
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "constituency" : {"coerce" : "unicode"}
            },
            "lists" : {
                "result" : {"contains" : "object"}
            },
            "structs" : {
                "result" : {
                    "fields" : {
                        "party" : {"coerce" : "unicode"},
                        "votes" : {"coerce" : "integer"}
                    }
                }
            }
        }
        self._add_struct(struct)
        super(Constituency, self).__init__(raw, expose_data=True)

    def add_result(self, party, votes):
        # self.result = {"party" : party, "votes" : votes}
        self._add_to_list("result", {"party" : party, "votes" : votes})

class RFA(clcsv.SheetWrapper):
    EMPTY_STRING_AS_NONE = True

    COERCE = {
        "Constituency Name" : dataobj.to_unicode(),
        "Region" : dataobj.to_unicode(),
        "Country" : dataobj.to_unicode(),
        "Constituency ID" : dataobj.to_unicode(),
        "Constituency Type" : dataobj.to_unicode()
    }

    DEFAULT_COERCE = [dataobj.to_int()]

sheet = RFA(rfa)

IGNORE = [
    "Press Association ID Number",
    "Constituency Name",
    "Region",
    "Country",
    "Constituency ID",
    "Constituency Type",
    "Election Year",
    "Electorate",
    "Total number of valid votes counted",
    " Total number of valid votes counted "
]

obs = []
for o in sheet.objects(beyond_headers=True):
    do = Constituency()
    do.constituency = o.get("Constituency Name")
    for k, v in o.iteritems():
        if k not in IGNORE and v is not None:
            do.add_result(k, v)
    do.id = uuid.uuid4()
    obs.append(do.data)

bulk = esprit.raw.to_bulk(obs)

with codecs.open(out, "wb") as f:
    f.write(json.dumps(obs, indent=2))

with codecs.open(batch, "wb") as f:
    f.write(bulk)

