##################################################
# overrides for the webapp deployment

DEBUG = True
PORT = 5029
SSL = False
THREADED = True

############################################
# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "edges"
ELASTIC_SEARCH_VERSION = "1.4.4"

# Classes from which to retrieve ES mappings to be used in this application
# (note that if ELASTIC_SEARCH_DEFAULT_MAPPINGS is sufficient, you don't need to
# add anything here
ELASTIC_SEARCH_MAPPINGS = [
    # "service.dao.MyDAO"
]

# initialise the index with example documents from each of the types
# this will initialise each type and auto-create the relevant mappings where
# example data is provided
ELASTIC_SEARCH_EXAMPLE_DOCS = [
    # "service.dao.MyDAO"
]

QUERY_ROUTE = {
    "query" : {                                 # the URL route at which it is mounted
        "constituencies" : {                             # the URL name for the index type being queried
            "auth" : False,                     # whether the route requires authentication
            "role" : None,                      # if authenticated, what role is required to access the query endpoint
            "filters" : [],            # names of the standard filters to apply to the query
            "dao" : "service.dao.ConstituencyDAO"       # classpath for DAO which accesses the underlying ES index
        }
    }
}

CLIENTJS_SEARCH_BASE_URL = "http://localhost:5029/query/"

############################################
# important overrides for account module

ACCOUNT_ENABLE = False
SECRET_KEY = "super-secret-key"

#############################################
# important overrides for storage module

#STORE_IMPL = "octopus.modules.store.store.StoreLocal"
#STORE_TMP_IMPL = "octopus.modules.store.store.TempStore"

from octopus.lib import paths
STORE_LOCAL_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "live")
STORE_TMP_DIR = paths.rel2abs(__file__, "..", "service", "tests", "local_store", "tmp")