from SourceCode.Agents.DemandPredication import MainGraph as DemandPredicationAgent
from SourceCode.Agents.InventoryOptimization import MainGraph as InventoryAgent
from SourceCode.Agents.GeopoliticalRiskManagement import MainGraph as RiskAgent
from SourceCode.Agents.SupplierAndLogisticsManagement import MainGraph as SupplierAndLogisticsAgent
from SourceCode.Agents.Orchestrator.Agent import SupervisorAgent
from SourceCode.Agents.StateTypes.GlobalState import GlobalState
from langgraph.graph import StateGraph


def run(global_state: GlobalState):
    builder = StateGraph(GlobalState)

    builder.add_node("SupervisorAgent", SupervisorAgent.Supervisor)
    builder.add_node("DemandPredicationAgent", DemandPredicationAgent.run)
    builder.add_node("InventoryOptimizationAgent", InventoryAgent.run)
    builder.add_node("SupplierAndLogisticsManagementAgent", SupplierAndLogisticsAgent.run)
    builder.add_node("GeopoliticalRiskManagement", RiskAgent.run)

    builder.set_entry_point("SupervisorAgent")
    builder.add_edge("DemandPredicationAgent", "supervisor")
    builder.add_edge("InventoryOptimizationAgent", "supervisor")
    builder.add_edge("SupplierAndLogisticsManagementAgent", "supervisor")
    builder.add_edge("GeopoliticalRiskManagement", "supervisor")

    app = builder.compile()
