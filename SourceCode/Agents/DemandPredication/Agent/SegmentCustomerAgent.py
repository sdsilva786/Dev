from SourceCode.Agents.DemandPredication.DTO.DemandPredictionState import InternalDemandPredictionState
from SourceCode.Agents.DemandPredication.SegmentProfilingModule import CustomerSegmentAnalysis
from langgraph.graph import StateGraph
from SourceCode.DataPersistence.Folder import SaveData


def SegmentCustomerAgent(state: InternalDemandPredictionState) -> InternalDemandPredictionState:
    df_customer_segment, df_segment_by_purchase_behavior, df_segment_by_part_preference = CustomerSegmentAnalysis.get_segment()
    output_file_path = SaveData.Customer_Segmentation(df_customer_segment)
    state["customer_segmentation_path"] = output_file_path

    output_file_path_p = SaveData.segment_by_part_preference(df_segment_by_part_preference)
    state["segment_by_part_preference_path"] = output_file_path_p

    output_file_path_b = SaveData.Purchase_Behavior_Segmentation(df_segment_by_purchase_behavior)
    state["segment_by_purchase_behavior_path"] = output_file_path_b

    return state
