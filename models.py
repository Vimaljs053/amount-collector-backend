from pydantic import BaseModel
from typing import Dict, List

class FineData(BaseModel):
    data: Dict[str, List[int]]

