
.PHONY: all local clean 

all:

env:
	( \
	  virtualenv -p python3 env; \
	  env/bin/pip install jinja2; \
	)

local: env
	$(foreach user,$(USERS), env/bin/python package.py obj/$(user)/angr;)

clean: 
	rm -rf obj
	rm -rf env
