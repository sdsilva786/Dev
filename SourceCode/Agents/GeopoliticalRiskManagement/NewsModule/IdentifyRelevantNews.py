from SourceCode.GenAIModel import AzureOpenAI
from langchain.schema import SystemMessage, HumanMessage


def GetRelevantNews(news_data: str):
    prompt = f"""
        Analyze the following feed/news article. 
        {news_data}
        1) Determine whether it is related to tariffs or  duties. If it is, respond with "Yes", and then summarize the nature of the tariff-related news, including which countries are involved or affected. Categorise it as "Tariff/Duties".
        2) Determine whether it is related to trade restrictions. Categorise it as "trade restrictions"
        3) Determine whether it is related to war or armed conflict. Consider factors such as military activity, violence, international tension, territorial disputes, or mentions of weapons and casualties. Categorise it as "war". 
        If it is any of the above (DOnt show rows having no category)
        Generate  xml response for following fields:
        Feed/News:
        Category:
        Countries Affected:
        Summary: [Brief summary or leave blank]
        Risk Score: [High / Medium / Low or leave blank]
        The XML format should be as follows:
        <xml><records>
            <record>
                <field name="x">[Value of x]</field>
                <field name="y">[Value of y]</field>
                <field name="z">[Value of z]</field>
            </record>
            <record>
                <field name="x">[Value of x]</field>
                <field name="y">[Value of y]</field>
                <field name="z">[Value of z]</field>
            </record>
            <!-- Add more records as needed -->
        </records></xml>
        
        4) Always generate a complete and well-formatted XML output strictly adhering to the provided format. Ensure all required tags are present, properly nested, and structured according to the defined schema. \n
        5) Generate XML output without including the "```xml".\n
        """
    llm = AzureOpenAI.Get_Instance()
    response = llm.invoke([
        SystemMessage(content="You are an expert geopolitical analyst."),
        HumanMessage(content=prompt)
    ])

    relevant_data = response.content
    return relevant_data
