import requests
import json

class AllDebrid:
	def __init__(self, token,agent):
		self._token=token
		self._agent=agent
		self._getProvider()
		self.headers = {
                        	'User-Agent': 'raspadmin_v1'
                	}

	def _getProvider(self):
		try:
			req = requests.get("https://api.alldebrid.com/v4/hosts?agent=%s" % (self._agent))
			data = json.loads(req.content)["data"]
			self._provider = []
			for x in data['hosts']:
				self._provider+=data['hosts'][x]["domains"]
		except Exception as e:
			self._provider= []
			print(str(e))

	def isProvider(self, url):
		for p in self._provider:
			if url.find(p)!=-1:
				return True

		return False


	def getLink(self,url):
		req = requests.get("https://api.alldebrid.com/v4/link/unlock?agent=%s&apikey=%s&link=%s" % (self._agent,self._token,url),headers=self.headers)
		data = json.loads(req.content.decode('utf-8'))
		if "error" in list(data.keys()):
			print(data)
			print((data["error"]["message"]))
			return (1,data["error"]["message"])
		else:
			return (0,data["data"]["link"])

