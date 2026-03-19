from dataclasses import dataclass

@dataclass
class ServiceInfo:
    version: str
    service: str
    author: str