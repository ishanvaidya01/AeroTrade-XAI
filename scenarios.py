from models import RouteOption

SCENARIOS = [
    {
        "id": "scenario_1",
        "name": "Port Strike in Singapore",
        "description": "A major labor strike at the Port of Singapore has halted all maritime transshipment operations, causing severe backlogs across Southeast Asia.",
        "routes": [
            RouteOption(id="r1_1", name="Air Freight Direct", mode="air", origin="Shenzhen", destination="Frankfurt"),
            RouteOption(id="r1_2", name="Sea-Air via Dubai", mode="sea-air", origin="Shenzhen", destination="Frankfurt"),
            RouteOption(id="r1_3", name="Rail via China-Europe Express", mode="rail", origin="Shenzhen", destination="Frankfurt"),
            RouteOption(id="r1_4", name="Sea Freight via Cape of Good Hope", mode="sea", origin="Shenzhen", destination="Frankfurt"),
            RouteOption(id="r1_5", name="Feeder Sea to Mumbai + Air", mode="sea-air", origin="Shenzhen", destination="Frankfurt"),
            RouteOption(id="r1_6", name="Overland Trucking via Central Asia", mode="road", origin="Shenzhen", destination="Frankfurt")
        ]
    },
    {
        "id": "scenario_2",
        "name": "Typhoon in South China Sea",
        "description": "A category 5 typhoon has forced the closure of major shipping lanes and ports in the South China Sea. Expect severe maritime delays.",
        "routes": [
            RouteOption(id="r2_1", name="Reroute Sea via Philippines East", mode="sea", origin="Shanghai", destination="Los Angeles"),
            RouteOption(id="r2_2", name="Air Freight via Tokyo", mode="air", origin="Shanghai", destination="Los Angeles"),
            RouteOption(id="r2_3", name="Sea-Rail via Vancouver", mode="sea-rail", origin="Shanghai", destination="Los Angeles"),
            RouteOption(id="r2_4", name="Direct Air Express", mode="air", origin="Shanghai", destination="Los Angeles"),
            RouteOption(id="r2_5", name="Sea to Panama City + Rail", mode="sea-rail", origin="Shanghai", destination="New York"),
            RouteOption(id="r2_6", name="Polar Route Air Freight", mode="air", origin="Shanghai", destination="New York")
        ]
    },
    {
        "id": "scenario_3",
        "name": "Border Closure in Eastern Europe",
        "description": "Geopolitical tensions have led to an abrupt closure of key rail and road borders in Eastern Europe, severing major overland corridors.",
        "routes": [
            RouteOption(id="r3_1", name="Southern Corridor Rail", mode="rail", origin="Chengdu", destination="Berlin"),
            RouteOption(id="r3_2", name="Air Freight Hub-to-Hub", mode="air", origin="Chengdu", destination="Berlin"),
            RouteOption(id="r3_3", name="Sea Freight via Mediterranean", mode="sea", origin="Chengdu", destination="Berlin"),
            RouteOption(id="r3_4", name="Road Freight via Middle East", mode="road", origin="Chengdu", destination="Berlin"),
            RouteOption(id="r3_5", name="Sea Freight to Rotterdam + River Barge", mode="sea-rail", origin="Chengdu", destination="Berlin"),
            RouteOption(id="r3_6", name="Air to Istanbul + Road Freight", mode="air-road", origin="Chengdu", destination="Berlin")
        ]
    },
    {
        "id": "scenario_4",
        "name": "Suez Canal Blockage",
        "description": "A mega-vessel has run aground in the Suez Canal, completely blocking the waterway and halting all transit between the Red Sea and the Mediterranean.",
        "routes": [
            RouteOption(id="r4_1", name="Sea Freight via Cape of Good Hope", mode="sea", origin="Mumbai", destination="Rotterdam"),
            RouteOption(id="r4_2", name="Sea-Air via Dubai Hub", mode="sea-air", origin="Mumbai", destination="Rotterdam"),
            RouteOption(id="r4_3", name="Direct Air Freight", mode="air", origin="Mumbai", destination="Rotterdam"),
            RouteOption(id="r4_4", name="Rail via INSTC Corridor", mode="rail", origin="Mumbai", destination="Rotterdam"),
            RouteOption(id="r4_5", name="Sea to Cairo + Overland + Sea", mode="sea-rail", origin="Mumbai", destination="Rotterdam")
        ]
    },
    {
        "id": "scenario_5",
        "name": "Panama Canal Drought",
        "description": "Severe drought has drastically lowered water levels in the Panama Canal, reducing daily vessel transits by 60% and imposing strict draft limits.",
        "routes": [
            RouteOption(id="r5_1", name="Sea Freight via Magellan Strait", mode="sea", origin="Busan", destination="New York"),
            RouteOption(id="r5_2", name="Sea Freight via Suez Canal", mode="sea", origin="Busan", destination="New York"),
            RouteOption(id="r5_3", name="Sea-Rail Mini Landbridge via LA", mode="sea-rail", origin="Busan", destination="New York"),
            RouteOption(id="r5_4", name="Direct Air Freight", mode="air", origin="Busan", destination="New York"),
            RouteOption(id="r5_5", name="Sea to Mexico + Overland Rail", mode="sea-rail", origin="Busan", destination="New York")
        ]
    },
    {
        "id": "scenario_6",
        "name": "Global Pandemics / Lockdowns",
        "description": "A sudden outbreak in major manufacturing hubs has caused severe lockdowns and crew shortages, severely impacting terminal productivity.",
        "routes": [
            RouteOption(id="r6_1", name="Chartered Air Freight", mode="air", origin="Hong Kong", destination="London"),
            RouteOption(id="r6_2", name="Automated Sea Freight via Hamburg", mode="sea", origin="Hong Kong", destination="London"),
            RouteOption(id="r6_3", name="Sea-Rail via Middle Corridor", mode="sea-rail", origin="Hong Kong", destination="London"),
            RouteOption(id="r6_4", name="Sea Freight via Antwerp", mode="sea", origin="Hong Kong", destination="London"),
            RouteOption(id="r6_5", name="Air to Frankfurt + Automated Rail", mode="air-rail", origin="Hong Kong", destination="London")
        ]
    },
    {
        "id": "scenario_7",
        "name": "Labor Strike in Long Beach",
        "description": "Dockworkers at the Port of Long Beach have walked out, effectively freezing the primary gateway for Trans-Pacific imports into North America.",
        "routes": [
            RouteOption(id="r7_1", name="Sea Freight via Seattle", mode="sea", origin="Tokyo", destination="Los Angeles"),
            RouteOption(id="r7_2", name="Sea-Rail via Vancouver", mode="sea-rail", origin="Tokyo", destination="Los Angeles"),
            RouteOption(id="r7_3", name="Air Freight Direct", mode="air", origin="Tokyo", destination="Los Angeles"),
            RouteOption(id="r7_4", name="Sea Freight to Mexico + Trucking", mode="sea-rail", origin="Tokyo", destination="Los Angeles"),
            RouteOption(id="r7_5", name="Sea Freight via Panama to Houston + Rail", mode="sea-rail", origin="Tokyo", destination="Los Angeles")
        ]
    },
    {
        "id": "scenario_8",
        "name": "Typhoon in Bay of Bengal",
        "description": "A severe super-typhoon in the Bay of Bengal has halted all shipping operations along the eastern coast of India and disrupted airspace.",
        "routes": [
            RouteOption(id="r8_1", name="Overland Truck to Mumbai + Sea", mode="road", origin="Chennai", destination="Rotterdam"),
            RouteOption(id="r8_2", name="Air Freight via Dubai", mode="air", origin="Chennai", destination="Rotterdam"),
            RouteOption(id="r8_3", name="Rail to North India + Air", mode="rail", origin="Chennai", destination="Rotterdam"),
            RouteOption(id="r8_4", name="Sea Freight Reroute via Sri Lanka South", mode="sea", origin="Chennai", destination="Rotterdam"),
            RouteOption(id="r8_5", name="Direct Air Express (Delayed)", mode="air", origin="Chennai", destination="Rotterdam")
        ]
    },
    {
        "id": "scenario_9",
        "name": "Winter Storms in North America",
        "description": "Record-breaking blizzards have blanketed the Midwest, freezing major rail hubs in Chicago and halting nationwide trucking.",
        "routes": [
            RouteOption(id="r9_1", name="Sea Freight via LA + Southern Rail", mode="sea-rail", origin="Taipei", destination="Chicago"),
            RouteOption(id="r9_2", name="Air Freight Direct", mode="air", origin="Taipei", destination="Chicago"),
            RouteOption(id="r9_3", name="Sea Freight via Houston + Truck", mode="sea-rail", origin="Taipei", destination="Chicago"),
            RouteOption(id="r9_4", name="Air to Dallas + Truck", mode="air", origin="Taipei", destination="Chicago"),
            RouteOption(id="r9_5", name="Sea Freight via New York + Rail", mode="sea-rail", origin="Taipei", destination="Chicago")
        ]
    },
    {
        "id": "scenario_10",
        "name": "Customs System Outage in Europe",
        "description": "A massive cyberattack has taken down the centralized customs processing system at major EU airports, causing mile-long truck queues and cargo holding.",
        "routes": [
            RouteOption(id="r10_1", name="Sea Freight to Antwerp + Truck", mode="sea", origin="Kuala Lumpur", destination="Paris"),
            RouteOption(id="r10_2", name="Air Freight to London + Chunnel Rail", mode="air", origin="Kuala Lumpur", destination="Paris"),
            RouteOption(id="r10_3", name="Sea-Air via Dubai to Madrid + Truck", mode="sea-air", origin="Kuala Lumpur", destination="Paris"),
            RouteOption(id="r10_4", name="Direct Air Freight (Held in Customs)", mode="air", origin="Kuala Lumpur", destination="Paris"),
            RouteOption(id="r10_5", name="Rail via Southern Europe corridor", mode="rail", origin="Kuala Lumpur", destination="Paris")
        ]
    },
    {
        "id": "scenario_11",
        "name": "Piracy Threat in Gulf of Guinea",
        "description": "A sudden surge in militant piracy has made the Gulf of Guinea impassable for commercial container vessels, forcing immediate rerouting.",
        "routes": [
            RouteOption(id="r11_1", name="Air Freight Direct", mode="air", origin="Lagos", destination="Houston"),
            RouteOption(id="r11_2", name="Overland to North Africa + Sea", mode="road", origin="Lagos", destination="Houston"),
            RouteOption(id="r11_3", name="Armed Escort Sea Freight (Premium)", mode="sea", origin="Lagos", destination="Houston"),
            RouteOption(id="r11_4", name="Sea Freight via South Atlantic detour", mode="sea", origin="Lagos", destination="Houston"),
            RouteOption(id="r11_5", name="Chartered Cargo Plane", mode="air", origin="Lagos", destination="Houston")
        ]
    },
    {
        "id": "scenario_12",
        "name": "Volcanic Ash Cloud",
        "description": "An explosive volcanic eruption in Southeast Asia has grounded all flights across the region due to dense ash clouds in the stratosphere.",
        "routes": [
            RouteOption(id="r12_1", name="Express Sea Freight", mode="sea", origin="Jakarta", destination="Tokyo"),
            RouteOption(id="r12_2", name="Sea-Rail via China", mode="sea-rail", origin="Jakarta", destination="Tokyo"),
            RouteOption(id="r12_3", name="Feeder Vessel + Air from Manila", mode="sea-air", origin="Jakarta", destination="Tokyo"),
            RouteOption(id="r12_4", name="Standard Sea Freight", mode="sea", origin="Jakarta", destination="Tokyo"),
            RouteOption(id="r12_5", name="Truck to Singapore + Air", mode="road", origin="Jakarta", destination="Tokyo")
        ]
    },
    {
        "id": "scenario_13",
        "name": "Equipment Shortage (Chassis)",
        "description": "A massive shortage of trucking chassis at West Coast ports has left thousands of containers stranded at the terminal, unable to move inland.",
        "routes": [
            RouteOption(id="r13_1", name="Air Freight Direct", mode="air", origin="Yokohama", destination="Seattle"),
            RouteOption(id="r13_2", name="Sea Freight to Vancouver + Rail", mode="sea-rail", origin="Yokohama", destination="Seattle"),
            RouteOption(id="r13_3", name="Sea Freight (Transload at Port)", mode="sea", origin="Yokohama", destination="Seattle"),
            RouteOption(id="r13_4", name="LCL expedited via Air", mode="air", origin="Yokohama", destination="Seattle"),
            RouteOption(id="r13_5", name="Sea Freight via Prince Rupert + Rail", mode="sea-rail", origin="Yokohama", destination="Seattle")
        ]
    },
    {
        "id": "scenario_14",
        "name": "Heavy Floods in Southeast Asia",
        "description": "Unprecedented monsoon flooding has submerged major industrial zones and destroyed critical road infrastructure leading to the port.",
        "routes": [
            RouteOption(id="r14_1", name="River Barge + Deep Sea Freight", mode="sea", origin="Ho Chi Minh", destination="London"),
            RouteOption(id="r14_2", name="Helicopter Lift to Hub + Air Freight", mode="air", origin="Ho Chi Minh", destination="London"),
            RouteOption(id="r14_3", name="Overland Rail via China", mode="rail", origin="Ho Chi Minh", destination="London"),
            RouteOption(id="r14_4", name="Cross-border Truck to Bangkok + Air", mode="road", origin="Ho Chi Minh", destination="London"),
            RouteOption(id="r14_5", name="Sea-Air via Middle East", mode="sea-air", origin="Ho Chi Minh", destination="London")
        ]
    },
    {
        "id": "scenario_15",
        "name": "Latin America Customs Strike",
        "description": "A coordinated strike by customs agents across major South American ports has paralyzed all import and export processing indefinitely.",
        "routes": [
            RouteOption(id="r15_1", name="Air Freight via Private Charter", mode="air", origin="Sao Paulo", destination="Miami"),
            RouteOption(id="r15_2", name="Sea Freight to Mexico + Truck Detour", mode="sea-rail", origin="Sao Paulo", destination="Miami"),
            RouteOption(id="r15_3", name="Cross-border Truck to Buenos Aires + Air", mode="road", origin="Sao Paulo", destination="Miami"),
            RouteOption(id="r15_4", name="Sea Freight via Caribbean Hub + Air", mode="sea-air", origin="Sao Paulo", destination="Miami"),
            RouteOption(id="r15_5", name="Smugg... Expedited Diplomatic Pouch", mode="air", origin="Sao Paulo", destination="Miami")
        ]
    }
]
