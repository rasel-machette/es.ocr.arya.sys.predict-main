from pydantic import BaseModel
from typing import List, Optional

class PDFFile(BaseModel):
    data: str
    fieldnames: List[str]