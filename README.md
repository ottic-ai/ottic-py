# OTTIC SDK

Learn how to use the Ottic SDK to manage and use published prompts in your applications.

## Setup

Follow these steps to install and configure the Ottic SDK:

### Step 1: Install Ottic

Install the Ottic Node.js SDK.

```bash
pip install ottic
```

### Step 2: Obtain Your Ottic API Key

Visit the [Integrations](https://app.ottic.ai/integrations) page to copy your Ottic API key.

> **Note**: This key is required to authenticate and use Ottic in your application.

### Step 3: Integrate a Published Prompt

Use the snippet below to set up the Ottic SDK and begin working with a published prompt in your application:

```python
from ottic import OtticAI

ottic = OtticAI(api_key=OTTIC_API_KEY)
```

## Using a Published Prompt in Production

Ottic allows you to generate responses from LLM with your prompt in your application. Below are three use cases demonstrating how to generate responses with published prompts or render prompt text.

### 1. Generate a Response Using a Prompt

This snippet demonstrates how to use a published prompt with variable placeholders to generate a response from the model:

```python
from ottic import OtticAI

ottic = OtticAI(api_key=OTTIC_API_KEY)

response = await ottic.chat.complete.create({
  promptId: 'YOUR_PROMPT_ID', # Replace with your published prompt ID
  variables: {
    variable: "dataset variable",
    variable1: "dataset variable1",
    variable2: "dataset variable2",
  },
  messages: [
    {
      role: 'user',
      content: "I want to buy a new insurance. I need help!",
    },
  ],
  metadata: {
    "userId": "METADATA_USER_ID",
    "userEmail": "USER@EMAIL.COM",
  },
  chainId: "CHAIN_ID",
  tags: ["TAG1", "TAG2"],
})
```

- **promptId** (string, required): The ID of the published prompt you want to use.
- **variables** (object): Variables you want to use in your prompt. Without variables, the prompt will be used as is.
- **messages** (array): A list of messages comprising the conversation so far. If messages are not provided, the prompt will be used as is.
- **metadata** (object): Contains additional information about the request.
- **chainId** (string): Identifier for the chain of requests and responses.
- **tags** (array): Array of strings that contain tags for the request.

> **Note**: `metadata`, `chainId`, and `tags` are optional parameters to monitor your requests and responses.

> **Note**: `response` will contain the output generated by the LLM based on the configuration of your Ottic prompt.

This snippet demonstrates how to request a response using the selected prompt settings. You can update the LLM configuration directly in Ottic and generate responses without modifying your code.

### 2. Retrieve a Rendered Prompt with Variable Replacements

To fetch a prompt with placeholders replaced by specified variable values, use the following code:

```python
from ottic import OtticAI

ottic = OtticAI(api_key=OTTIC_API_KEY)
livePrompt = await ottic.prompts.render({
  promptId: 'YOUR_PROMPT_ID',
  variables: {
    variable: "dataset variable",
    variable1: "dataset variable1",
    variable2: "dataset variable2",
  },
})
```

- **promptId** (string, required): The ID of the published prompt you want to use.
- **variables** (object): Variables you want to use in your prompt. Without variables, the prompt will be used as is.

If any variables are missing, they will remain as placeholders in the returned prompt.

### 3. Retrieve a Prompt with Placeholders Intact

To retrieve a prompt without any variable replacements, use this snippet:

```python
from ottic import OtticAI

ottic = OtticAI(api_key=OTTIC_API_KEY)
livePrompt = await ottic.prompts.render({ promptId: 'YOUR_PROMPT_ID' })
```

This will return the original prompt without modifications.



More information about Ottic API can be found [https://docs.ottic.ai](https://docs.ottic.ai).