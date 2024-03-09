import json
with open('sample-data.json') as f:
    data = json.load(f)
template = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
{}
"""
interface_data = []
for it in data['imdata']:
    interface = it['l1PhysIf']['attributes']
    dn = interface['dn']
    description = interface['descr']
    speed = interface['speed']
    mtu = interface['mtu']
    interface_data.append((dn, description, speed, mtu))

formatted_data = "\n".join(f"{dn:<55} {description:<16} {speed:<8} {mtu:<7}" for dn, description, speed, mtu in interface_data)

print(template.format(formatted_data))