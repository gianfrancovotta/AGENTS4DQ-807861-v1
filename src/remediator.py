from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from outputs import Outputs

load_dotenv()

class RemediatorAgent:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemma-4-31b-it", temperature=0)

    def generate_remediation_report(self, completeness_report, consistency_report, anomaly_report, file_to_check):
        prompt = (
            f"You are a Lead Data Quality Engineer. I am providing you with three diagnostic reports "
            f"for a dataset named '{file_to_check.name}'.\n\n"
            "Note: The pipeline has ALREADY standardized column names, casted data types, replaced placeholders with NaNs, "
            "and removed exact duplicate rows.\n\n"
            f"### 1. Completeness Report:\n{completeness_report}\n\n"
            f"### 2. Consistency Report:\n{consistency_report}\n\n"
            f"### 3. Anomaly Report:\n{anomaly_report}\n\n"
            "### TASK:\n"
            "Generate a final 'Human-in-the-Loop Action Plan' and a 'Data Reliability Score'.\n\n"
            "### OUTPUT FORMAT (Strict Markdown):\n"
            "## Final Data Reliability Score: [Insert Score 0-100]/100\n"
            "**Justification:** [1-2 sentences explaining why this score was given based on the severity of remaining issues.]\n\n"
            "## Human-in-the-Loop Action Plan\n"
            "Based on the reports, here are the exact steps the data engineering team should take to finish cleaning this dataset:\n"
            "- **Missing Values:** [Provide specific imputation strategies (e.g., median, mean, mode) for remaining missing values].\n"
            "- **Outliers & Anomalies:** [Advise on what to do with the specific outliers flagged—should they be capped, deleted, or investigated?]\n"
            "- **Inconsistencies:** [Advise on how to manually resolve any format or cross-column logic issues found].\n"
        )
        message = self.model.invoke(prompt)
        return message.content
