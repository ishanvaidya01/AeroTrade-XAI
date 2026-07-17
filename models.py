from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class RouteOption(BaseModel):
    id: str
    name: str
    mode: str
    origin: str
    destination: str

class ToolTrace(BaseModel):
    tool_name: str
    input_args: Dict[str, Any]
    output: Any
    timestamp: str

class DecisionStep(BaseModel):
    step_description: str
    trace: Optional[ToolTrace] = None

class RejectedRoute(BaseModel):
    route_id: str
    rejection_reason: str

class RouteScores(BaseModel):
    cost: float
    time: float
    risk: float
    carbon: float

class TradeOffResult(BaseModel):
    chosen_route_id: str
    rejected_routes: List[RejectedRoute]
    route_scores: Dict[str, RouteScores]
    justification: str
