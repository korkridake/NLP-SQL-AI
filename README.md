<h1 align="center"> NL2SQL Guidebook</h1>

- [Enterprise-Grade Natural Language to SQL Generation using LLMs (NL2SQL)](#enterprise-grade-natural-language-to-sql-generation-using-llms-nl2sql)
- [Technology Plan for AI Agents](#technology-plan-for-ai-agents)
  - [AI Agent Decision Tree](#ai-agent-decision-tree)
- [Acknowledgements](#acknowledgements)
- [Additional Resources](#additional-resources)

# Enterprise-Grade Natural Language to SQL Generation using LLMs (NL2SQL)

![relationship](media/guerrillabuzz-7hA2wqBcSF8-unsplash.jpg)

Photo by <a href="https://unsplash.com/@guerrillabuzz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">GuerrillaBuzz</a> on <a href="https://unsplash.com/photos/diagram-7hA2wqBcSF8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

The Natural Language to SQL project leverages Azure Generative AI to automatically create SQL queries from natural language inputs. This approach streamlines the conversion process, helping to ensure both accuracy and efficiency. When building NL to SQL solutions, here are the key issues to address:

* **Schema Complexity**: Databases have intricate schemas that can make NL to SQL translation difficult.
* **Schema Storage & Planning**: Efficiently storing schema details for quick access by the AI model.
* **Contextual Retrieval**: The AI model requires an understanding of schema relationships to generate accurate queries.
* **Ranking and Optimization**: Retrieving the most relevant schema details and prioritizing them for accuracy.
* **Natural Language Ambiguity**: Human language is inherently ambiguous and context-dependent. Disambiguating user queries and understanding the intended meaning is necessary to generate accurate SQL statements.
* **Dynamic Schemas**: Adapting to evolving database schemas without much challenge is crucial.

You learn how to:

* Design and configure Fabric data agents that enable secure conversational access to enterprise data.
* Curate and optimize data sources, instructions, and example queries for accurate and relevant responses.
* Publish, operationalize, and integrate Fabric data agents with downstream experiences like Microsoft Foundry, Power BI, and custom apps.
* Apply governance, permission, and prompting best practices that improve reliability and safeguard data.

From this repository, you can explore the [latest advancements](#-text-to-sql-survey--tutorial) in Text-to-SQL research (a.k.a NL2SQL). We provide a comprehensive survey, in-depth research papers, and benchmark evaluations. 

**<img src="https://img.shields.io/badge/TKDE'2025-green"> A Survey of Text-to-SQL in the Era of LLMs: Where are we, and where are we going?**
[<img src="https://img.shields.io/badge/Paper-grey">](https://arxiv.org/abs/2408.05109)
[<img src="https://img.shields.io/badge/Slides-orange">](./slides/NL2SQL_handbook.pdf)

**<img src="https://img.shields.io/badge/VLDB'2025-blue"> Natural Language to SQL: State of the Art and Open Problems**
[<img src="https://img.shields.io/badge/Paper-grey">](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/VLDB25-NL2SQL.pdf)
[<img src="https://img.shields.io/badge/Slides-orange">](./slides/NL2SQL-VLDB2025.pdf)

**<img src="https://img.shields.io/badge/VLDB'2024-blue"> The Dawn of Natural Language to SQL: Are We Fully Ready?**
[<img src="https://img.shields.io/badge/Paper-grey">](https://www.vldb.org/pvldb/vol17/p3318-luo.pdf) 
[<img src="https://img.shields.io/badge/Slides-orange">](./slides/NL2SQL360-VLDB2024.pdf)
[<img src="https://img.shields.io/badge/Code-purple">](https://github.com/HKUSTDial/NL2SQL360)

<p align="center">
<img width="800" src="media/river.svg"/>
</p>

# Technology Plan for AI Agents

It's critical to understand how to select the right technology platform for each of your potential agent use cases. It covers adopting a ready-to-use SaaS agent or building a custom agent with Microsoft Foundry (PaaS) or Microsoft Copilot Studio (SaaS). Effective technology adoption aligns goals with cost, level of effort, and customization needs. This alignment matches the technology to the use case and balances the effort required to achieve a return on investment. Understanding the available landscape ensures the right choice between adopting a ready-to-use SaaS agent or building a custom solution to provide business advantage.

## AI Agent Decision Tree

The AI agent decision tree guides the technology selection process by focusing on one primary question: Does a SaaS agent meet your functional requirements? If a SaaS agent satisfies your needs, adopt the prebuilt solution. If no SaaS agent fits the use case, you must build a custom agent. Determining which platform to use for a custom build, Microsoft Foundry, Microsoft Copilot Studio, or custom infrastructure, requires further investigation. The following sections provide guidance on selecting the right platform based on your specific requirements.

![ai-agent-decision-tree](media/ai-agent-decision-tree.svg)

# Acknowledgements

```bibtex
@article{liu2025survey,
  title={A Survey of Text-to-SQL in the Era of LLMs: Where are we, and where are we going?},
  author={Liu, Xinyu and Shen, Shuyu and Li, Boyan and Ma, Peixian and Jiang, Runzhi and Zhang, Yuxin and Fan, Ju and Li, Guoliang and Tang, Nan and Luo, Yuyu},
  journal={IEEE Transactions on Knowledge and Data Engineering},
  year={2025},
  publisher={IEEE}
}
```

# Additional Resources

1. [Technology Plan for AI Agents across your organization using the Microsoft Ecosystem - Cloud Adoption Framework | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/technology-solutions-plan-strategy)
2. [HKUSTDial/NL2SQL_Handbook: This is a continuously updated handbook for readers to easily track the latest Text-to-SQL techniques in the literature and provide practical guidance for researchers and practitioners.](https://github.com/HKUSTDial/NL2SQL_Handbook)
3. [NL2SQL with BigQuery and Gemini | Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/nl2sql-with-bigquery-and-gemini)
4. [A Survey of NL2SQL with Large Language Models: Where are we, and where are we going?](https://arxiv.org/html/2408.05109v4)
5. [Enterprise-grade natural language to SQL generation using LLMs: Balancing accuracy, latency, and scale | Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/enterprise-grade-natural-language-to-sql-generation-using-llms-balancing-accuracy-latency-and-scale/)