Kap: 2


2.1	Motagarens adress står först

2.2	En mac-adress består av 12 tecken. Första halvan säger vem tillverkaren är	

2.3	Switchen får sina anteckningar från att skicka ut ett "broadcast" till all portarna på switchen för att sen
	få ett svar tillbaka om vem som sitter på respektive port. Switchen gör det själv

2.4	Den skickar ut ett broadcast på all portar förutom på den som skickade meddelandet

2.5	Den sitter kvar ca 300 sec. Om den inte fösvann skulle listan tillslut bli oändlig och så skulle switchen skicka
	till en port ingen sitter på

2.6	ff:ff:ff:ff:ff:ff är adressen som används vid ett broadcast meddelande. Betyder till alla på detta nätet

2.7	För att switchen inte vet vem som sitter på vilken port så den frågar alla och alla svarar med sin adress så att
	så att switchen kan bygga sin lista. Sen går svaret bara tillbaka till den som frågade från början
	eftersom switchen redan har den adressen

2.8	Den frågar efter sin default gateways MAC-adress

2.9	Dynamisk betyder att den lärst sig adressen själv och static att den är manuelt inskriven eller switchens egna

2.10	Kabeln kan va dålig, sitta i fel port, enheten är avstängd eller att porten är "shutdown"

2.11	Hon sitter på fel Vlan, kolumn 1 avslöjar det

2.12	Port 2 fungerar sämmre efter som den bara har a-half- a-100 och inte a-full a-1000 som övriga portar
	Jag skulle kontrolera om båda sidor använde samma hastighet (show interface gi0/2) (duplex missmatch)

2.13	Ramen skickas till alla portar för att switchen ska få information om vem som sitter på vilken port.
	När switchen har skickat ut meddelandet till alla portar så svarar alla tillbaka att "jag är  "IP" 
	och jag har "MAC". På så sätt kan switchen göra sig en egen lista om vem som sitter på vilken port och behöver
	då inte skicka till alla portar nästa gång.
