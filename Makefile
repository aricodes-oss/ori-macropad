OUTDIR = /run/media/${USER}/ORIPAD
OBJECTS = boot.py code.py lib mappings.json README.md

all:
	cp -r $(OBJECTS) $(OUTDIR)/
