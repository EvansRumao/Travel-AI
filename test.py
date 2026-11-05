from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
# res = tavily_search("Best hotels in India")
# print(res)

# res = search_flights("Plan a 7 days Nepal trip from Mumbai")
# print(res)

user_input=input("Enter your travel query: ")
result=run_travel_agent(
  user_input=user_input,
  thread_id="test_thread"
)

print("Final response")
print(result["answer"])