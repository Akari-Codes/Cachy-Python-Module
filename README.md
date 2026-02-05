# Cachy

[![Cachy](https://github.com/Akari-Codes/Cachy-Python-Module/actions/workflows/python-publish.yml/badge.svg?branch=main&event=status)](https://github.com/Akari-Codes/Cachy-Python-Module/actions/workflows/python-publish.yml)

Cachy is a simple Module I have written for my own ease of use, and I decided to release it as a public module so other people can use it. Cachy allows use to add pass data into it and saves it to a single index but can also save the entire index or a single data from the index when using the save feature you can have multiple programs share variabls without having to setup a local data tunnel also allows you to have files saved in the cache meaning you can have the system load a cached file when it isnt in the index that was from a previous session into the current session.

## How to Use Cachy

To import this custom module, use the import command ```from cachy import Cachy```, then it must be put into a variable called cache ```cache = Cachy()```
Usage of this module:
- ```cache.deposit(data=<data to save>, id=<identifier>)```
This caches data under the identifier name
- 
- ```<variable> = cache.withdraw.(id=<identifier>)```
This fetches cached data under the identifier name
- 
- ```cache.save(data=<data to save>, id=<identifier>)```
This saves the data and caches it under the identifier name
- 
- ```cache.save_item(id=<identifier>)```
This saves existing cached data via the  identifier name
- 
- ```<variable> = cache.load(id=<identifier>)```
This loads saved data into cache, then fetches the same data from cache under the identifier name
- 
- ```cache.destroy(id=<identifier>)```
This destroys the ache item under the identifier name
- 
- ```cache.destroy_item(id=<identifier>)```
This destroys the cached item and the saved item under the identifier name
- 
- ```cache.unsave(id=<identifier>)```
This destroys the saved item under the identifier name
- 
- ```cache.session_save(name=<name of session>)```
This saves the session's loaded cached data into a cache file. The name for the session is optional; if you don't use the session parameter, then it will default to the internal global session name.
- 
- ```cache.session_load(name=<name of session>)```
This loads the session's saved cached data into the cache. The name for the session is optional; if you don't use the session parameter, then it will default to the internal global session name.
- 
- ```cache.session_clear(name=<name of session>)```
This clears the specified saved session. The name is not required; if no name is given, it will clear the saved session with the default session file identifier.
- 
- ```cache.sessions_clear_all()```
This clears all saved sessions, does not effect current loaded cache
- 
- ```cache.clear()```
This clears the cache
- 
- ```cache.clear_all()```
This clears the cache and the saved file cache

Feel free to create a fork for this module and edit as you like, but please credit me 😘, the least you can do for me 🥰.

Module by Akari_VT (Akari-Codes): Discord = ```akarigames_vt```
