import datetime

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    history_id: int
    isotope_number: int
    seen_at: datetime.datetime