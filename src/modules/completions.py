from typing import Dict, Optional, List, Any

class Completions:
    def __init__(self, client):
        """
        Initialize the Completions client.
        
        :param client: API client instance
        """
        self._client = client

    def create(self, 
               prompt_id: str, 
               variables: Optional[Dict[str, Any]] = None, 
               messages: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Create a chat completion.
        
        :param prompt_id: Identifier for the prompt
        :param variables: Optional dictionary of variables
        :param messages: Optional list of message dictionaries
        :return: Chat completion response
        """
        input_data = {'prompt_id': prompt_id}
        
        if variables:
            input_data['variables'] = variables
        
        if messages:
            input_data['messages'] = messages
        
        response = self._client.post('/v1/chat/completions', input_data)
        return response