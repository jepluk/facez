import json
from dataclasses import dataclass, fields

class DynamicObject:
    def __init__(self, dc):
        for key, value in dc.items():
            if isinstance(value, dict):
                value = DynamicObject(value)  # Rekursi untuk nested dictionary
            elif isinstance(value, list):
                value = [DynamicObject(item) if isinstance(item, dict) else item for item in value]  # Rekursi untuk list of dicts
            setattr(self, key, value)
