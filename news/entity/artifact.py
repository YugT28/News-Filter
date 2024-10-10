from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    database_name:str
    table_name:str

