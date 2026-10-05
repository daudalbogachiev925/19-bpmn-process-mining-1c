def render_bpmn(transitions, output='process.bpmn'):
    xml = ['<?xml version="1.0"?>',
           '<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL">',
           '<process id="p1" isExecutable="false">']
    nodes = set()
    for a, b in transitions:
        nodes.add(a); nodes.add(b)
    for i, n in enumerate(nodes):
        xml.append(f'<task id="t{i}" name="{n}"/>')
    for i, (a, b) in enumerate(transitions):
        xml.append(f'<sequenceFlow id="f{i}" sourceRef="t{list(nodes).index(a)}" '
                   f'targetRef="t{list(nodes).index(b)}"/>')
    xml.append('</process></definitions>')
    open(output, 'w').write('\n'.join(xml))
