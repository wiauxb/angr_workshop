
.PHONY: all local clean 

all:

env:
	( \
	  virtualenv -p python3 env; \
	  env/bin/pip install -r requirements.txt; \
	)

local: env
	$(foreach user,$(USERS), (cd exercices && ../env/bin/python package.py ../obj/$(user)/angr/exercices;))
	$(foreach user,$(USERS), (cd exercices-sup && ../env/bin/python package.py ../obj/$(user)/angr/exercices-sup;))
	$(foreach user,$(USERS), (cd exercices-sup && ../env/bin/python extern.py ../obj/$(user)/angr/exercices-sup;))

clean: 
	rm -rf obj
	rm -rf env
