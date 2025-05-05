from SourceCode.Agents.Orchestrator import MainGraph
from SourceCode.Agents.StateTypes.GlobalState import GlobalState

initial_state = {
    "next_agent": "DemandPredicationAgent"
}

app = MainGraph.run(GlobalState)
app.invoke(initial_state)
