"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "I couldn't find any venues in Edinburgh with a capacity of 300 and vegan options. The largest available venue found was The Guilford Arms with a capacity of 200, but it does not offer vegan options. The largest available venue with vegan options is The Albanach with a capacity of 180."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When I changed The Albanach's status to 'full' in mcp_venue_server.py and reran the client, the agent automatically pivoted to the next best match, The Haymarket Vaults, which has a capacity of 160 and vegan options. Crucially, I did not have to update the client script or the tool definitions; the agent discovered the updated state through the MCP tool call, demonstrating the decoupling of tool logic and agent orchestration.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 45   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0    # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a standardized protocol for tool discovery and execution, allowing agents to dynamically connect to and use tools without needing hardcoded function definitions or schemas in the agent's codebase. This promotes better modularity and reusability across different agent frameworks and languages, as the same MCP server can serve multiple clients while keeping the tool implementation details encapsulated on the server side.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner: A strong-reasoning model in the autonomous-loop half that breaks down complex user requests into discrete subgoals, ensuring the Executor has a clear, non-ambiguous plan.
- Executor: A tool-using agent in the autonomous-loop half that carries out the subgoals provided by the Planner, using MCP tools to interact with the environment.
- Memory Store: A shared layer that persists conversation history and discovered information (like venue details), allowing both the autonomous and structured components to maintain context.
- Rasa MCP Gateway: A bridge component that connects the structured Rasa CALM flow to the shared MCP servers, enabling auditable business logic to use the same tools as the autonomous loop.
- Handoff Bridge: A shared-layer logic that determines when the autonomous loop has gathered enough information to pass control to a structured business process (like final booking) or vice versa.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph agent is far better suited for the research phase because it can handle open-ended, non-deterministic sub-tasks like filtering venues by varying constraints and dynamically fetching extra details via tool calls. Swapping them feels wrong because the research phase requires the probabilistic flexibility of a ReAct loop to handle messy or incomplete search results. In contrast, the booking/confirmation call is better handled by Rasa CALM's structured flows, which provide an auditable and deterministic state machine for business-critical actions where high reliability is paramount.
"""