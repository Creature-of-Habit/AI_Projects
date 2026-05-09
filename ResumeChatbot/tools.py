import json
from notify import push

def record_user_details(email, name='Name not provided', notes='No notes provided'):
    push(f'Recording interest from {name} with email {email} and notes {notes}')
    return {'recorded': 'ok'}


def record_unknown_question(question):
    push(f'Recording unknown question: {question}')
    return {'recorded': 'ok'}

record_user_details_json = {
    'name': 'record_user_details',
    'description': 'Use this tool to record that a user is interested in being in touch and provided an email address.',
    'parameters': {
        'type': 'object',
        'properties': {
            'email': {
                'type': 'string',
                'description': 'The email address of the user'
            },
            'name': {
                'type': 'string',
                'description': 'The name of the user'
            },
            'notes': {
                'type': 'string',
                'description': 'Any additional notes the conversation worth recording'
            }
        },
        'required': ['email'],
        'additionalProperties': False
    }
}

record_unknown_question_json = {
    'name': 'record_unknown_question',
    'description': 'Always use this tool to record any question that could not be answered as you did notknow the answer.',
    'parameters': {
        'type': 'object',
        'properties': {
            'question': {
                'type': 'string',
                'description': 'The question that could not be answered.'
            }
        },
        'required': ['question'],
        'additionalProperties': False
    }
}

tools = [{'type': 'function', 'function': record_user_details_json},
            {'type': 'function', 'function': record_unknown_question_json}]
