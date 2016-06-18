#!/usr/bin/env python
# https://pypi.python.org/pypi/biomart
from biomart import BiomartServer

#Connect to a Biomart Server
server = BiomartServer( "http://www.biomart.org/biomart" )

# set verbose to True to get some messages
server.verbose = True
