from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample

config_list = [
	{
        "model": "gpt-3.5-turbo-16k",
		"api_type": "open_ai",
		"api_key": "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"
	}
]

llm_config={
	"request_timeout": 300,
	"seed": 157,
	"config_list": config_list,
	"temperature": 0
}

# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
task="""write, execute and save python code to print the number 1 to 10"""
user_proxy.initiate_chat(assistant, message=task)

# This initiates an automated chat between the two agents to solve the task

