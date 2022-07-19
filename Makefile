OUTDIR = /run/media/${USER}/ORIPAD
OBJECTS = boot.py code.py lib mappings.json

all:
	cp -r $(OBJECTS) $(OUTDIR)/
