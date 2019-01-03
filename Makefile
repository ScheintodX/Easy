xfwm.png: xfwm.svg
	inkscape -e $@ $<

xpm.Makefile: makemake.py conf.json
	./makemake.py > $@

BASE=xfwm.png
CROP=gm convert -crop
include xpm.Makefile

all: $(ALL_XPM)

BASE=xfwm.png

.phony: clean
clean:
	rm -Rf xfwm4/*.xpm *.png xpm.Makefile

