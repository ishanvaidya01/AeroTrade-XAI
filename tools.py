from langchain.tools import tool
import requests

@tool(description="Calculate the total cost of a route in USD")
def get_route_cost(route_id: str, mode: str) -> float:
    base_costs = {
        "air": 50000.0,
        "sea": 10000.0,
        "rail": 20000.0,
        "road": 15000.0,
        "sea-air": 35000.0,
        "sea-rail": 18000.0
    }
    if mode not in base_costs:
        print(f"WARNING: Unknown mode '{mode}' in get_route_cost. Using default fallback.")
    base = base_costs.get(mode, 25000.0)
    seed = sum(ord(c) for c in route_id)
    cost = base + (seed * 100)
    
    try:
        response = requests.get("https://open.er-api.com/v6/latest/EUR", timeout=2)
        if response.status_code == 200:
            rate = response.json().get("rates", {}).get("USD", 1.08)
            cost = cost * rate
    except Exception:
        pass
        
    return cost

@tool(description="Calculate the total transit time of a route in days")
def get_route_time(route_id: str, mode: str) -> float:
    base_time = {
        "air": 2.0,
        "sea": 30.0,
        "rail": 15.0,
        "road": 7.0,
        "sea-air": 12.0,
        "sea-rail": 22.0
    }
    if mode not in base_time:
        print(f"WARNING: Unknown mode '{mode}' in get_route_time. Using default fallback.")
    base = base_time.get(mode, 14.0)
    seed = sum(ord(c) for c in route_id)
    return max(1.0, base + (seed % 5) - 2.0)

@tool(description="Calculate the risk score of a route between 0 and 1")
def get_route_risk(route_id: str, mode: str) -> float:
    base_risk = {
        "air": 0.1,
        "sea": 0.4,
        "rail": 0.3,
        "road": 0.5,
        "sea-air": 0.25,
        "sea-rail": 0.35
    }
    if mode not in base_risk:
        print(f"WARNING: Unknown mode '{mode}' in get_route_risk. Using default fallback.")
    base = base_risk.get(mode, 0.3)
    seed = sum(ord(c) for c in route_id)
    risk = base + ((seed % 10) / 50.0)
    
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true", timeout=2)
        if response.status_code == 200:
            wind = response.json().get("current_weather", {}).get("windspeed", 0)
            if wind > 20:
                risk += 0.15
    except Exception:
        pass
        
    return min(1.0, max(0.01, risk))

@tool(description="Calculate the carbon emissions of a route in tons")
def get_route_carbon(route_id: str, mode: str) -> float:
    base_carbon = {
        "air": 500.0,
        "sea": 50.0,
        "rail": 80.0,
        "road": 120.0,
        "sea-air": 300.0,
        "sea-rail": 60.0
    }
    if mode not in base_carbon:
        print(f"WARNING: Unknown mode '{mode}' in get_route_carbon. Using default fallback.")
    base = base_carbon.get(mode, 100.0)
    seed = sum(ord(c) for c in route_id)
    return base + (seed * 2)
