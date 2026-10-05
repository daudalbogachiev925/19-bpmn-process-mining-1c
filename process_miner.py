from collections import defaultdict
import statistics

def mine(log):
    by_case = defaultdict(list)
    for e in log:
        by_case[e['document_ref']].append(e)

    transitions = defaultdict(int)
    durations = defaultdict(list)

    for case, events in by_case.items():
        events.sort(key=lambda x: x['changed_at'])
        for a, b in zip(events, events[1:]):
            transitions[(a['status'], b['status'])] += 1
            durations[(a['status'], b['status'])].append(
                (b['changed_at'] - a['changed_at']).total_seconds())

    avg = {k: statistics.mean(v) for k, v in durations.items()}
    return transitions, avg
