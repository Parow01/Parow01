# umaralertbot/data_aggregator/data_aggregator_main.py

def aggregate_data(data_sources):
    """
    Combines multiple data source dictionaries into a single summary.
    """
    aggregated = {}
    for source in data_sources:
        for key, value in source.items():
            if key not in aggregated:
                aggregated[key] = []
            aggregated[key].append(value)
    return aggregated
