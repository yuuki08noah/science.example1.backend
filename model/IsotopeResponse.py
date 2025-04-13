from pydantic import BaseModel


class IsotopeResponse(BaseModel):
    number: int
    symbol: str
    name: str
    mass: dict
    weight: float
    svg_data: str

    def add_svg_data(self, svg_data: str):
        self.svg_data = svg_data