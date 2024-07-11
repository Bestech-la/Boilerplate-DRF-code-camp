from enum import Enum

class Aggregation(Enum):
    COUNT = "count"
    SUM = "sum"
    AVERAGE = "average"
    MIN = "min"
    MAX = "max"
    DISTINCT = "distinct"
    PERCENT = "percent"
    PERCENTILE = "percentile"