# In a notebook, you can use: %pip install -U fabric-data-agent-sdk
%pip install -U fabric-data-agent-sdk

# Step 1: Import required libraries.
# - pandas: used to build the evaluation dataset (question + expected answer rows).
# - FabricDataAgentManagement: lightweight helper to reference and inspect an existing Data Agent.
# - evaluate_data_agent: runs the evaluation against your agent.
# - get_evaluation_summary / get_evaluation_details: fetches aggregated and row-level results.
import pandas as pd
from fabric.dataagent.client import FabricDataAgentManagement
from fabric.dataagent.evaluation import (
    evaluate_data_agent,
    get_evaluation_details,
    get_evaluation_summary,
)

# Step 2: Identify the target Data Agent to evaluate.
# Update this value if your Data Agent has a different name.
data_agent_name = "nl2sqltaxi"
print(f"[INFO] Target Data Agent name: {data_agent_name}")

# Create a management object for the Data Agent.
# This does not run an evaluation; it simply initializes a client-side handle.
data_agent = FabricDataAgentManagement(data_agent_name)
print(f"[INFO] Data Agent handle initialized: {data_agent}")

# Step 3: Build the evaluation dataset.
# Required column names:
# - question: the natural-language query you want the agent to answer.
# - expected_answer: the expected output used by the evaluator for comparison.
# Add more rows to test additional scenarios.
df = pd.DataFrame(
    columns=["question", "expected_answer"],
    data=[
        ["How many green taxi trips that took place in 2019?", "6,300,814"],
    ],
)
print(f"[INFO] Evaluation dataset created with {len(df)} row(s).")

# Step 4: Configure evaluation options.
# workspace_name (Optional):
# - Use None when the Data Agent is in your current workspace.
# - Provide a workspace name string when evaluating an agent in another workspace.
workspace_name = None

# table_name (Optional):
# - Name of the output table that stores evaluation results.
# - The SDK also creates a '<table_name>_steps' table for detailed execution traces.
table_name = "demo_evaluation_output"

# data_agent_stage (Optional):
# - "sandbox" for draft/testing stage.
# - "production" for published/production stage.
# Default SDK behavior is typically production if not provided.
data_agent_stage = "sandbox"

print("[INFO] Evaluation configuration:")
print(f"       workspace_name = {workspace_name}")
print(f"       table_name     = {table_name}")
print(f"       data_agent_stage = {data_agent_stage}")

# Step 5: Run evaluation.
# evaluate_data_agent returns a unique evaluation_id for this run.
evaluation_id = evaluate_data_agent(
    df,
    data_agent_name,
    workspace_name=workspace_name,
    table_name=table_name,
    data_agent_stage=data_agent_stage,
)
print(f"[SUCCESS] Evaluation started/completed. evaluation_id = {evaluation_id}")

# Step 6: Retrieve aggregated summary metrics.
# This usually includes counts of pass/fail/unclear (exact columns may vary by SDK version).
eval_summary_df = get_evaluation_summary(table_name)
print("[INFO] Evaluation summary DataFrame:")
print(eval_summary_df)

# Step 7: Retrieve detailed row-level results.
# get_all_rows:
# - True: return all evaluated rows.
# - False: return only failed rows (default behavior in many examples).
get_all_rows = True

# verbose:
# - True: print additional diagnostics/summary to console.
# - False: return the DataFrame silently.
verbose = True

eval_details_df = get_evaluation_details(
    evaluation_id,
    table_name,
    get_all_rows=get_all_rows,
    verbose=verbose,
)

print("[INFO] Detailed evaluation DataFrame:")
print(eval_details_df)