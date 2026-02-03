from cachy import cache
cache.initialize()
cache.deposit(data="Cock", id="1")
print(cache.withdraw(id="1"))
cache.save(data="tata", id="2")
print(cache.load(id="2"))
