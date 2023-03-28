#!/usr/bin/env python3

__author__ = 'Tim'
import json
import sys
import config

spec = {"device": [], "packet": []}


# Load given specFile. Specfile was created from original
# RESOL Configuration File XML shippes with RSC (Resol Service Center)
# using XML to JSON converter at http://www.utilities-online.info/xmltojson
def load_spec_file(spec_file):
    global spec
    with open(spec_file) as json_data:
        data = json.load(json_data)
        try:
            spec['device'].extend(data['vbusSpecification']['device'])
            spec['packet'].extend(data['vbusSpecification']['packet'])
        except Exception as e:
            sys.exit('Cannot load Spec: ' + str(e))

    if config.debug:
        for device in spec['device']:
            print(device)

        for packet in spec['packet']:
            print(packet)
            for field in packet['field']:
                print("  " + str(field))

    json_data.close()


if config.spec_files and len(config.spec_files) > 0:
    for spec_file in config.spec_files:
        load_spec_file(config.spec_dir + spec_file)
else:
    load_spec_file(config.spec_file)
