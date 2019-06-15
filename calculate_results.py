def read_timestamps():
    import json
    from datetime import datetime
    with open( 'timestamps.json' ) as f:
        results = json.loads(f.read())
    for rider in results:
        for point in ['s1-start','s1-end','s2-start','s2-end','s3-start','s3-end','s4-start','s4-end']:
            if rider[point] != '':
                rider[point] = datetime.strptime(rider[point], '%Y-%m-%dT%H:%M')
    return results

def write_results(results, filename):
    import json
    with open(filename, 'w') as f:
        json.dump( {'data': results}, f, indent=2)

def calculate_results(timestamps):
    from datetime import timedelta
    last_result_key = None
    for stage in xrange(1,5):
        for rider in timestamps:
            start_key = 's{}-start'.format(stage)
            end_key = 's{}-end'.format(stage)
            result_key = 's{}-result'.format(stage)
            if rider[start_key] and rider[end_key] and (last_result_key is None or last_result_key in rider):
                rider[result_key] = rider.get(last_result_key, timedelta(0)) + rider[end_key] - rider[start_key]
        last_result_key = result_key
    return timestamps

def format_results(results):
    from collections import OrderedDict
    formatted_results = []
    for rider in results:
        rider_results = OrderedDict()
        rider_results['Rider'] = rider['displayName']
        rider_results['CP1'] = format_timedelta(rider.get('s1-result', ''))
        rider_results['CP2'] = format_timedelta(rider.get('s2-result', ''))
        rider_results['CP3'] = format_timedelta(rider.get('s3-result', ''))
        rider_results['CP4'] = format_timedelta(rider.get('s4-result', ''))
        formatted_results.append( rider_results )
    return formatted_results

def format_timedelta( td ):
    from datetime import timedelta
    if not isinstance(td, timedelta):
        return td
    hours = (td.days * 24) + (td.seconds / 3600)
    minutes = (td.seconds % 3600) / 60
    return '{:03d}H {:02d}M'.format(hours, minutes)

if __name__ == "__main__":
    ts = read_timestamps()
    r = calculate_results(ts)
    fr = format_results(r)
    write_results(fr, 'output/19.json')
