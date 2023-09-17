from flask import blueprints 

views = blueprints ('views ', _name_ )

@views .root ('/')
def home <h1>test</h1>