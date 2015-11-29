#!/usr/bin/env bash
curl -XPOST http://localhost:9200/edges --data-binary "@mapping.json"