import json

from tools import record_unknown_question, record_user_details


def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f'Tool called: {tool_name}', flush=True)

        tool = globals()[tool_name]
        result = tool(**arguments) if tool else {}
        results.append({'role': 'tool', 'content':json.dumps(result),'tool_call_id': tool_call.id})
    return results