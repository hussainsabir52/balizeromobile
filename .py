g = geocoder.ip('me')

	referrer = request.headers.get("Referer") 
	if referrer == None:
		ref = "Direct"
	else:	
		u = urlparse(referrer)
		ref = u.netloc
	
	today = datetime.today()
	anal = Analytic(date=today,browser=request.user_agent.platform,
		country=g.country,referrer=ref,linkanalytic_id=link.id)
	db.session.add(anal)
	db.session.commit()	





	UA-134629090-2

	'AW-628471311'