&#x09;      **Scenario	                        Corridor**

1	Port Strike in Singapore	   Shenzhen → Frankfurt

2	Typhoon in South China Sea	   Shanghai → Los Angeles/New York

3	Border Closure in Eastern Europe   Chengdu → Berlin

4	Suez Canal Blockage	           Mumbai → Rotterdam

5	Panama Canal Drought	           Busan → New York

6	Global Pandemic/Lockdowns	   Hong Kong → London

7	Labor Strike in Long Beach	   Tokyo → Los Angeles

8	Typhoon in Bay of Bengal	   Chennai → Rotterdam

9	Winter Storms in North America	   Taipei → Chicago

10	Customs System Outage in Europe	   Kuala Lumpur → Paris

11	Piracy Threat in Gulf of Guinea	   Lagos → Houston

12	Volcanic Ash Cloud	           Jakarta → Tokyo

13	Equipment Shortage (Chassis)	   Yokohama → Seattle

14	Heavy Floods in SE Asia	           Ho Chi Minh → London

15	Latin America Customs Strike	   Sao Paulo → Miami



These are some hardcoded events just for testing and showing purpose, but at the same time, 

If your selected Origin+Destination doesn't match any pre-built scenario, the app queries the 

**GDELT Project API (a real-time global news database)** 

**searching for keywords like "port strike", "shipping delay", "typhoon", "canal blockage", etc. combined with your city names.** 

If it finds a matching article, it creates a live disruption scenario from the news headline.



If neither matches, it falls back to "Business as Usual (Baseline Assessment)." 

