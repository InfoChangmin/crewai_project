from crewai import Task
from crewai_tools import tool
from crewai import Crew
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
import yfinance as yf
import os

# 개인 환경 설정 부분입니다.
os.environ["OPENAI_API_KEY"] = 'Your-api_key'
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


scrape_tool  = ScrapeWebsiteTool()

@tool("Stock Price")
def stock_price(ticker):
    '''
    Useful to get stock price data.
    The input should be a ticker, for example AAPL, NET.
    '''
    ticker = yf. Ticker(ticker)
    return ticker.history(period='1mo')

@tool("Balance Sheet")
def balance_sheet (ticker):
    '''
    Useful to get the balance sheet of a company.
    The input to this tool should be a ticker, for exa
    '''
    ticker = yf.Ticker(ticker)
    return ticker.balance_sheet

@tool ("Income Statement" )
def income_stmt (ticker):
    '''
    Useful to get the income statement of a company.
    The input to this tool should be a ticker, for ex
    '''
    ticker = yf. Ticker(ticker)
    return ticker.income_stmt

@tool("Insider Transactions")
def insider_transactions (ticker):
    '''
    Useful to get insider transactions of a stock.
    The input to this tool should be a ticker, for exi
    '''
    ticker = yf.Ticker(ticker)
    return ticker.insider_transactions

@tool("Stock News")
def stock_news(ticker):
    '''
    Useful to get news about a stock.
    The input should be a ticker, for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.news


researcher = Agent (
    role='Researcher',
    goal='Gather and interpret vast amounts of data to privide a comprehensive overview of the sentiment and news surrounding a stock',
    backstory="You're skilled in gathering and interpreting data from various sources. Yor read each data source carefully and extract the most important information. your insights are crucial for making informed investment desisions.",
    verbose = True,
    tools = [
        scrape_tool,
        stock_news
    ]
)
technical_analyst = Agent (
    role='Technical_Analyst',
    goal='Analyze the movements of a stock and provide insights on trends, entry points, resistance and support levels.',
    backstory="An expert in technical analysis, you're known for your ability to predict stock prices. You provide valuable insights to your customers.",
    verbose = True,
    tools = [
            stock_price
        ]
    )
financial_analyst = Agent (
    role='Financial_Analyst',
    goal="Use financial statements, insider trading data and other metrics to evaluate a stock's financial health and performance.",
    backstory="You're a very experienced investment advisor that looks at a company's financial health, market sentiment, and qualitative data to make informed recommendations.",
    verbose = True,
    tools = [
            income_stmt,
            balance_sheet,
            insider_transactions
        ]
)
hedge_fund_manager = Agent (
    role='Hedge_Fund_Manager',
    goal='Manage a portfolio of stocks and make investment decisions to maximize returns using insights from financial analysts and researchers.',
    backstory="You're a seasoned hedge fund manager with a proven track record of making profitable investments. You always impress your clients.",
    verbose = True
)

research = Task(
    description="Gather and analyze the latest news and market sentiment surrounding {company}'s stock. Provide a summary of the news and any notable shifts in sentiment.",
    agent=researcher,
    expected_output="Your final answer MUST be a detailed summary of the news and market sentiment surrounding the stock.",
)

technical_analysis = Task(
    description="Analyze the {company}'s financial statements, balance sheet, insider trading data and other metrics to evaluate {company}'s financial health and performance.",
    agent=technical_analyst,
    expected_output="Your final answer MUST be a report with potential entry points, price targets and any other relevant information.",
)

financial_analysis = Task(
    description="Conduct a technical analysis of the {company} stock price movements and identify key support and resistance levels chart patterns.",
    agent=technical_analyst,
    expected_output="Your final answer MUST be a report with an overview an overview of {company}'s revenue, earnings, cash flow, and other key financial metrics.",
)
investment_recommendation = Task(
    description="Based on the research, technical analysis, and financial analysis reports, provide a detailed investment recommendation for {company} stock.",
    agent=hedge_fund_manager,
    expected_output="Your final answer MUST be a detailed recommendation to BUY, SELL or HOLD the stock. Provide a clear rationale for your recommendation.",
    context = [
        research,
        technical_analysis,
        financial_analysis
    ],
    output_file = 'investment_recommedation.md'
)

crew = Crew(
    tasks=[
        research,
        technical_analysis,
        financial_analysis,
        investment_recommendation
    ],
    agents=[
        researcher,
        technical_analyst,
        financial_analyst,
        hedge_fund_manager
    ],
    verbose=2,
)
result = crew.kickoff(
    inputs={
        "company":"Tesla"
    }
)