#! /usr/bin/python
import pprint
import pysolr
import sys

def search(): 
  host       = "localhost"
  port       = "8983"
  collection = "it4853-1"
  q          = "*"
  fl         = "*"
  qt         = "select"
  fq         = ""
  rows       = "10"
  url        = 'http://' + host + ':' + port + '/solr/' + collection 

  solr       = pysolr.Solr(url, search_handler="/"+qt, timeout=5)
  results    = solr.search(q, **{
      'fl': fl,
      'fq': fq,
      'rows': rows
  })
  
  return results
  #print("Number of hits: {0}".format(len(results)))
  #for i in results:
  #  pprint.pprint(i)