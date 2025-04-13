from typing import List

import uvicorn
from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model.HistoryDeleteRequest import HistoryDeleteRequest
from service.isotope_service import get_history, get_isotopes, delete_history
from exceptions import IsotopeNotFound, HistoryNotFound
from model.HistoryResponse import HistoryResponse
from model.IsotopeResponse import IsotopeResponse
from service.isotope_service import visualize_isotope_percentage_by_number, save_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시에는 프론트 주소로 제한하세요
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, DELETE, OPTIONS 등 모두 허용
    allow_headers=["*"],
)
@app.get("/isotopes/{number}", response_model=IsotopeResponse)
async def root(number: int = Path(...)):
    try:
        save_history(number)
        return visualize_isotope_percentage_by_number(number)
    except IsotopeNotFound:
        raise HTTPException(status_code=404, detail="Isotope not found")
    except Exception as e:
        print(e)

@app.get("/isotopes", response_model=List[IsotopeResponse])
async def isotopes():
    try:
        save_history(0)
        return get_isotopes()
    except Exception as e:
        print(e)

@app.get("/histories", response_model=List[HistoryResponse])
async def histories():
    try:
        return get_history()
    except Exception as e:
        print(e)

@app.delete("/histories/{id}")
async def delete(id:int= Path(...)):
    try:
        delete_history(HistoryDeleteRequest(history_id=id))
    except HistoryNotFound:
        raise HTTPException(status_code=404, detail="History not found")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)