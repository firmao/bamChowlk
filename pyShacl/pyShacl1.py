from pyshacl import validate
from os import path

shapes_file = path.abspath("dataGraph.ttl")
shapes_file_format = 'turtle'

data_file = path.abspath("dataGraph.json")
data_file_format = 'json-ld'

conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=True,
                                     serialize_report_graph=True)
print(conforms)
""" print(v_graph) """
print(v_text)
