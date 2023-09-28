from autogen import AssistantAgent, UserProxyAgent
import autogen
import openai


openai.api_key = "<your OpenAI API key here>"

config_list = [
    {
        'model': 'gpt-4',
        'api_key': '<your OpenAI API key here>',
    },  # OpenAI API endpoint for gpt-4
    {
        'model': 'gpt-3.5-turbo',
        'api_key': '<your OpenAI API key here>',
    },  # OpenAI API endpoint for gpt-3.5-turbo
    {
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '<your OpenAI API key here>',
    },  # OpenAI API endpoint for gpt-3.5-turbo-16k
]


user_proxy = autogen.UserProxyAgent(
    name = "Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin",
    code_execution_config = False,
)

fun_engineer = autogen.AssistantAgent(
    name = "Fun_manager",
    llm_config = config_list,
    system_message='Fun manager. You maximize the fun when Admin is at a location - optimize for unique memorable experiences & fun stories',    
)


groupchat = autogen.GroupChat(agents=[
    user_proxy, fun_engineer], messages=[], max_round=50)

manager = autogen.GroupChatManager(groupchat=groupchat)
llm_config = config_list

user_proxy.initiate_chat(
    manager,
    message = 'Plan a month long trip to bangkok. Include a table of dates and activity.'
)

