class System:
	def __init__(self, name):
		self.name = name
		self.systems = []

Systems = {}

# LIBERTY
Systems["new york"] = 	System("new york")
Systems["colorado"] = 	System("colorado")
Systems["california"] =	System("california")
Systems["texas"] =		System("texas")

# KUSARI
Systems["shikoku"] =	System("shikoku")
Systems["new tokyo"] =	System("new tokyo")
Systems["kyushu"] =		System("kyushu")
Systems["honshu"] = 	System("honshu")
Systems["hokkaido"] =	System("hokkaido")
Systems["chugoku"] = 	System("chugoku")
Systems["tohoku"] =		System("tohoku")

# BRETONIA
Systems["leeds"] =		System("leeds")
Systems["new london"] =	System("new london")
Systems["dublin"] =		System("dublin")
Systems["cambridge"] =	System("cambridge")
Systems["edinburgh"] = 	System("edinburgh")

# RHEINLAND
Systems["hamburg"] =	System("hamburg")
Systems["new berlin"] =	System("new berlin")
Systems["frankfurt"] =	System("frankfurt")

# INDEPENDENT
Systems["kepler"] =		System("kepler")
Systems["galileo"] =	System("galileo")
Systems["alaska"] =		System("alaska")
Systems["bering"] =		System("bering")
Systems["hudson"] =		System("hudson")
Systems["magellan"] =	System("magellan")
Systems["manchester"] =	System("manchester")

# BORDERWORLD
Systems["tau-23"] = 	System("tau-23")
Systems["tau-29"] =		System("tau-29")
Systems["tau-31"] =		System("tau-31")
Systems["sigma-13"] =	System("sigma-13")
Systems["omega-3"] =	System("omega-3")

# CORSAIRS

# EDGE WORLD

# UNSORTED
Systems["cortez"] =		System("cortez")

###############################

# LIBERTY
Systems["new york"].systems = [Systems["colorado"], Systems["california"], Systems["texas"], Systems["alaska"], Systems["magellan"]]
Systems["colorado"].systems = [Systems["kepler"], Systems["new york"], Systems["galileo"]]
Systems["california"].systems = [Systems["new york"], Systems["magellan"], Systems["cortez"]]
Systems["texas"].systems = [Systems["new york"], Systems["hudson"], Systems["bering"]]

# KUSARI
Systems["shikoku"].systems = [Systems["kepler"], Systems["galileo"], Systems["new tokyo"]]
Systems["new tokyo"].systems = [Systems["kyushu"], Systems["shikoku"], Systems["honshu"], Systems["hokkaido"]]
Systems["kyushu"].systems = [Systems["tau-29"], Systems["new tokyo"], Systems["tau-23"]]
Systems["honshu"].systems = [Systems["new tokyo"], Systems["chugoku"]]
Systems["hokkaido"].systems = [Systems["chugoku"], Systems["new tokyo"]]
Systems["chugoku"].systems = [Systems["tohoku"], Systems["honshu"], Systems["hokkaido"]]
Systems["tohoku"].systems = [Systems["chugoku"]]

# BRETONIA
Systems["leeds"].systems = [Systems["tau-31"], Systems["magellan"], Systems["new london"], Systems["edinburgh"], Systems["dublin"]]
Systems["new london"].systems = [Systems["leeds"], Systems["dublin"], Systems["cambridge"], Systems["manchester"]]
Systems["dublin"].systems = [Systems["new london"], Systems["leeds"]]
Systems["cambridge"].systems = [Systems["new london"], Systems["omega-3"], Systems["leeds"]]
Systems["edinburgh"].systems = [Systems["leeds"]]

# RHEINLAND
Systems["hamburg"].systems = [Systems["hudson"], Systems["frankfurt"], Systems["bering"]]
Systems["new berlin"].systems = [Systems["sigma-13"]]
Systems["frankfurt"].systems = [Systems["hamburg"], Systems["new berlin"]]

# INDEPENDENT
Systems["kepler"].systems = [Systems["colorado"], Systems["shikoku"]]
Systems["galileo"].systems = [Systems["colorado"], Systems["shikoku"]]
Systems["alaska"].systems = [Systems["new york"]]
Systems["bering"].systems = [Systems["texas"], Systems["hamburg"]]
Systems["hudson"].systems = [Systems["texas"], Systems["hamburg"]]
Systems["magellan"].systems = [Systems["new york"], Systems["leeds"]]
Systems["manchester"].systems = [Systems["new london"], Systems["cortez"], Systems["magellan"]]

# BORDERWORLD
Systems["tau-23"].systems = [Systems["kyushu"], Systems["tau-29"]]
Systems["tau-29"].systems = [Systems["tau-23"], Systems["tau-31"], Systems["kyushu"]]
Systems["tau-31"].systems = [Systems["tau-29"], Systems["leeds"]]
Systems["sigma-13"].systems = [Systems["chugoku"], Systems["new berlin"]]
Systems["omega-3"].systems = [Systems["cambridge"]]

# CORSAIRS

# EDGE WORLD

# UNSORTED
Systems["cortez"].systems = [Systems["california"],Systems["manchester"]]
