Kap: 1


1.1 	För att man kopplar upp sig direkt mot switchen via consolkabel och behöver därför inte gå via nätet

1.2 	Switch> Användarläge kan få info men inte ändra något
	Switch# Priviliged läge, här går det att göra ändringar. Nås via enable
	Switcg#(config) Här görs alla ändringar på enheten. Nås via configure terminal

1.3 	Enable

1.4 	Running-config är configen som är på switchen just nu men inte nödvändigtvis den som kommer användas om man startar om.
    	Startup-config är configen som är sparad på switchen och kommer användas vid en omstart.

1.5 	Den försvinner

1.6 	Physical
	Data link
	Network
	Transportation 
	Session
	Presentation
	Application	

1.7	Switchen arbetar på lager:2 och routern på lager:3

1.8	En brandvägg bestämmer vem som får passera

1.9	Show version ger dig bland annat information om: vilken version av IOS, uptime, vilken modell, serie nummer

1.10 	Den ska ha 9600 8N1 har den fel hastighet ser man ingenting eller konstiga tecken

1.11	Port:3 och jag skulle köra: enable, conf t, interface gi0/3, no shutdown och write memory

1.12	Jag säger att han är i fel läge och måste gå in i privilige läge via "enable" # och sen till konfigurationsläge
	för att kunna sätta nytt hostname

1.13	Skillnaden mellan en running-config och en startup-config är att den ena är kvar efter en omstart.
	Running-config är den konfigurationen som är inställd på switchen just nu. 
	Bara för att konfigurationen används just nu behöver inte betyda att den är sparad om man skulle starta om den.
	Startup-configt är konfigurationen som kommer användas vid en omstart.
	Så det är viktigt att alltid spara running-config till startup-config för att va säker på att den är sparad.


