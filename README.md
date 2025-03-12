## OpenAI Agents SDK demo

Really simple demo of the [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents)

```
pip install openai-agents
```

```
python agent_multi_weather.py
```

Query;

```
Which city is currently the coldest? 
Melbourne, Chicago, Oslo, Dublin, or Shanghai? 
Will I need an umbrella in this city in the next few days? 
Finally given the coldest city, can you suggest a famous landmark for me to visit in that city?
```

Response;

```
The coldest city currently is **Oslo** with a temperature of 0.2°C.

### Weather in Oslo:
- **Current Temp:** 0.2°C
- **Umbrella Needed?** It doesn't seem like there will be significant precipitation in the next few days, so an umbrella might not be necessary.

### Landmark Suggestion:
In Oslo, a famous landmark to visit is the **Vigeland Sculpture Park**. It's renowned for its large collection of sculptures by Gustav Vigeland and is a unique cultural experience.
```

