from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_system = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

def f():
   user_agent_rot = UserAgent(software_names=software_names, operating_system=operating_system, limit=100)
   n = 100
   while n>0:
      user_agent = user_agent_rot.get_user_agents()

      user_agent = user_agent_rot.get_random_user_agent()
      print(user_agent)
      n-=1
      