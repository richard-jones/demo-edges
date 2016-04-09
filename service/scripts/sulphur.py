from octopus.lib import paths, dataobj, clcsv
import os, codecs, json, uuid, csv
import esprit

d = paths.rel2abs(__file__, "..", "..", "data", "election")
price = os.path.join(d, "price.csv")

class Price(dataobj.DataObj):
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "created_date" : {"coerce" : "utcdatetime"},
                "last_updated" : {"coerce" : "utcdatetime"},
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
