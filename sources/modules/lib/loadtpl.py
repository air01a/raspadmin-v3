def load_tpl(tplfile,vars):
	tpl=open(tplfile, "r")
        content=tpl.read()
        tpl.close()

        for var in list(vars.keys()):
        	content=content.replace(var,vars[var])
	return content
