from pydantic import BaseModel


class HistoryRequest(BaseModel):
    isotope_number: int