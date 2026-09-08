import ipaddress


text = "192.168.1.128/26"


net = ipaddress.ip_network(text, strict=False)


usable = list (net.hosts())

print(f"Nat:           {net.network_address}")
print(f"Natmask:       {net.netmask}")
print(f"Broadcast:     {net.broadcast_address}")
print(f"Forsta address:{usable[0]}")
print(f"Sista address: {usable[-1]}")
print(f"Antal enheter: {len(usable)}")