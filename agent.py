from google.adk.agents import LlmAgent, Agent
from google.adk.tools import agent_tool, ToolContext
from google.adk.tools.google_search_tool import GoogleSearchTool

def search_web(query: str) -> str:
  """Search the web for information on a query.

  Args:
    query: The search query string.

  Returns:
    Simulated search results.
  """
  return (
      f'Search results for "{query}":\n'
      f'1. Google Pixel: Teléfonos inteligentes (smartphones) de alta gama, como el Google Pixel 9 Pro, que destacan por su cámara y software con IA\n'
      f'2. Google Nest: Dispositivos para el hogar inteligente (smart home), incluyendo altavoces inteligentes (Nest Mini), pantallas (Nest Hub), cámaras de seguridad, timbres con video y termostatos\n'
      f'3. Chromecast con Google TV: Dispositivos de streaming para conectar al televisor y reproducir contenido en alta definición, facilitando el acceso a plataformas como YouTube, Netflix o Disney'
  )

def analyze_billing(user_id: str) -> str:
  """Analyze and synthesize information from invoice.

  Args:
    user_id: The user id.

  Returns:
    A summary.
  """

  return (
      f'The total amount for this invoice is €35.00. Payment will be automatically processed in two business days.'
  )

def reset_password(userid: str) -> str:
  """Reset the password and send the new link to change it.

  Args:
    userid: The user id.

  Returns:
    A summary.
  """
  return (
      f'A password reset link has been sent to your registered email address. Please follow the instructions in the email to complete the process.'
  )

def setup_mfa(userid: str, phone: str) -> str:
  """Set up the MFA security configuration for the user using their phone number.

  Args:
    userid: The user id.
    phone: The phone number.

  Returns:
    A summary.
  """
  return (
      f'The MFA has been set up for your account. Please follow the instructions in the email to use it.'
  )

iam_agent = Agent(
  name='iam_agent',
  model='gemini-2.5-flash',
  description=(
      'ALWAYS answer the question in spanish. Agent specialized in performing access and identity management questions. Resetting password, using MFAs, etc.'
  ),
  instruction='Use the right tool to solve the user inquiries.',
  tools=[
    reset_password, setup_mfa
  ],
)

billing_agent = Agent(
  name='billing_agent',
  model='gemini-2.5-flash',
  description=(
      'ALWAYS answer the question in spanish. Agent specialized in performing billing and invoices questions.'
  ),
  instruction='Answer the questions about billing and invoices the billing answer.',
  tools=[
    analyze_billing
  ],
)

root_agent = Agent(
  name='root_agent',
  model='gemini-2.5-flash',
  description=(
      'ALWAYS answer the question in spanish. Require the User ID if you do not have it. Help the customer and delegate to subagents always, always delegate to billing agent or iam agent'
  ),
  sub_agents=[iam_agent, billing_agent],
  instruction='help the customer finding answers to questions'
)
