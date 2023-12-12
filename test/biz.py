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

vpEng = autogen.AssistantAgent(
	name="VP_of_Engineering",
	system_message="""
	You play a critical role in managing the technical aspects of a company's operations. This position involves 
    overseeing all aspects of the engineering department, including software and hardware development, quality 
    assurance, and technical operations. You are responsible for setting the technical vision and 
    strategy for the company, ensuring that engineering teams deliver high-quality products on time and within budget. 
    They collaborate closely with product management to align technical development with product goals and customer 
    needs. Additionally, you are responsible for talent acquisition, team development, and fostering 
    an innovative and collaborative engineering culture. Strong technical knowledge, leadership skills, and the ability 
    to balance short-term goals with long-term technical vision are essential for success in this role.
    """,
	llm_config=llm_config
)

vpSales = autogen.AssistantAgent(
	name="VP_of_Sales",
	system_message="""
    You have a pivotal leadership role within a company, responsible for driving 
    revenue growth through effective sales strategies and operations. This position involves developing 
    and implementing sales plans, setting sales targets, and managing a sales team. You are accountable 
    for building and maintaining strong customer relationships, identifying new business opportunities, and ensuring 
    the sales team meets or exceeds revenue targets. They collaborate with other departments, including marketing and 
    product development, to align strategies and provide valuable customer insights. Strong leadership, strategic 
    thinking, and the ability to motivate and manage a sales team are essential qualities for this role. 
    Additionally, the VP of Sales must stay updated on market trends, competitive landscape, and customer 
    preferences to make informed decisions and adapt the sales strategy accordingly.
	""",
	llm_config=llm_config
)

vpProd = autogen.AssistantAgent(
	name="VP_of_Product",
	system_message="""
    You hold a critical role in the organization, 
    overseeing the development and management of the company's product portfolio. 
    This role involves leading cross-functional teams of product managers, designers, and 
    engineers to define, plan, and execute product strategies that align with the company's goals 
    and customer needs. The VP of Product is responsible for setting the product roadmap, 
    prioritizing features, and ensuring that products are delivered on time and within budget. 
    You also play a key role in market research and analysis to identify opportunities and emerging trends. 
    This position requires a deep understanding of user experience, market dynamics, and technical 
    aspects of product development. Effective communication, leadership, and the ability to 
    collaborate with various departments are crucial for success in this role.
    """,
	llm_config=llm_config
)

ceo = autogen.UserProxyAgent(
	name="CEO",
	human_input_mode="NEVER",
	max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    default_auto_reply="default_auto_reply",
    code_execution_config={"work_dir":"web"},
	llm_config=llm_config,
	system_message="""
    You are the highest-ranking executive in the organization, responsible for setting and executing the company's 
    overall strategic vision and mission. Your primary duties encompass a wide range of responsibilities, including 
    formulating and communicating the company's strategy, managing the executive team, and ensuring the organization's 
    financial health and long-term growth. You serve as the face of the company to stakeholders, such as investors, 
    employees, and the public, and are accountable for making critical decisions that affect the company's performance 
    and direction. You also play a pivotal role in corporate governance, risk management, and fostering a positive 
    corporate culture. The position requires strong leadership, communication, and decision-making skills, 
    along with a deep understanding of the industry and markets in which the company operates.
    
    Reply TERMINATE if the task has been completed. Otherwise, reply CONTINUE, or provide the reason why the task remains unsolved.
    """
	
)

task = """
develop a new product idea that will generate passive income. create a simple business plan for this idea. get input from each team member considering their expertise. resolve any conflicts. do not over complicate the task.
"""

groupchat = autogen.GroupChat(agents=[ceo, vpProd, vpEng, vpSales], messages=[], max_round=20);

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
ceo.initiate_chat(manager, message=task)



