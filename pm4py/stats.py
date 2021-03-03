from typing import Dict, Union, List, Tuple

import pandas as pd

from pm4py.objects.log.log import EventLog, Trace
from pm4py.util.pandas_utils import check_is_dataframe, check_dataframe_columns


def get_start_activities(log: Union[EventLog, pd.DataFrame]) -> Dict[str, int]:
    """
    Returns the start activities from a log object

    Parameters
    ---------------
    log
        Log object

    Returns
    ---------------
    start_activities
        Dictionary of start activities along with their count
    """
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        from pm4py.statistics.start_activities.pandas import get
        return get.get_start_activities(log)
    else:
        from pm4py.statistics.start_activities.log import get
        return get.get_start_activities(log)


def get_end_activities(log: Union[EventLog, pd.DataFrame]) -> Dict[str, int]:
    """
    Returns the end activities of a log

    Parameters
    ---------------
    log
        Lob object

    Returns
    ---------------
    end_activities
        Dictionary of end activities along with their count
    """
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        from pm4py.statistics.end_activities.pandas import get
        return get.get_end_activities(log)
    else:
        from pm4py.statistics.end_activities.log import get
        return get.get_end_activities(log)


def get_attributes(log: Union[EventLog, pd.DataFrame]) -> List[str]:
    """
    Returns the attributes at the event level of the log

    Parameters
    ---------------
    log
        Log object

    Returns
    ---------------
    attributes_list
        List of attributes contained in the log
    """
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        return list(log.columns)
    else:
        from pm4py.statistics.attributes.log import get
        return list(get.get_all_event_attributes_from_log(log))


def get_trace_attributes(log: Union[EventLog, pd.DataFrame]) -> List[str]:
    """
    Gets the attributes at the trace level of a log object

    Parameters
    ----------------
    log
        Log object

    Returns
    ---------------
    trace_attributes_list
        List of attributes at the trace level
    """
    from pm4py.util import constants
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        return [x for x in list(log.columns) if x.startswith(constants.CASE_ATTRIBUTE_PREFIX)]
    else:
        from pm4py.statistics.attributes.log import get
        return list(get.get_all_trace_attributes_from_log(log))


def get_attribute_values(log: Union[EventLog, pd.DataFrame], attribute: str) -> Dict[str, int]:
    """
    Returns the values for a specified attribute

    Parameters
    ---------------
    log
        Log object
    attribute
        Attribute

    Returns
    ---------------
    attribute_values
        Dictionary of values along with their count
    """
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        from pm4py.statistics.attributes.pandas import get
        return get.get_attribute_values(log, attribute)
    else:
        from pm4py.statistics.attributes.log import get
        return get.get_attribute_values(log, attribute)


def get_variants(log: Union[EventLog, pd.DataFrame]) -> Dict[str, List[Trace]]:
    """
    Gets the variants from the log

    Parameters
    --------------
    log
        Event log

    Returns
    --------------
    variants
        Dictionary of variants along with their count
    """
    import pm4py
    if pm4py.util.variants_util.VARIANT_SPECIFICATION == pm4py.util.variants_util.VariantsSpecifications.STRING:
        import warnings
        warnings.warn('pm4py.get_variants is deprecated. Please use pm4py.get_variants_as_tuples instead.')
    if pm4py.util.variants_util.VARIANT_SPECIFICATION == pm4py.util.variants_util.VariantsSpecifications.LIST:
        raise Exception('Please use pm4py.get_variants_as_tuples')
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        from pm4py.statistics.variants.pandas import get
        return get.get_variants_count(log)
    else:
        from pm4py.statistics.variants.log import get
        return get.get_variants(log)


def get_variants_as_tuples(log: Union[EventLog, pd.DataFrame]) -> Dict[Tuple[str], List[Trace]]:
    """
    Gets the variants from the log
    (where the keys are tuples and not strings)

    Parameters
    --------------
    log
        Event log

    Returns
    --------------
    variants
        Dictionary of variants along with their count
    """
    import pm4py
    # the behavior of PM4Py is changed to allow this to work
    pm4py.util.variants_util.VARIANT_SPECIFICATION = pm4py.util.variants_util.VariantsSpecifications.LIST
    if check_is_dataframe(log):
        check_dataframe_columns(log)
        from pm4py.statistics.variants.pandas import get
        return get.get_variants_count(log)
    else:
        from pm4py.statistics.variants.log import get
        return get.get_variants(log)
