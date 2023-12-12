import autogen

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

assistant = autogen.AssistantAgent(
	name="assistant",
	system_message="You are a Python coder",
	llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
	name="user_proxy",
	human_input_mode="NEVER",
	max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    default_auto_reply="default_auto_reply",
    code_execution_config={"work_dir":"web"},
	llm_config=llm_config,
	system_message="""Reply TERMINATE if the task has been completed. Otherwise, reply CONTINUE, or provide the reason why the task remains unsolved."""
	
)

task = """
write a python method to output the numbers 1 to 100 and save that method to a file 
"""

user_proxy.initiate_chat(assistant, message=task)



