SLIM=slim1.txt slim2.txt slim3.txt slim4.txt
FWDPY=fwdpy1.txt fwdpy2.txt fwdpy3.txt fwdpy4.txt

all: seeds.txt $(SLIM) $(FWDPY)

clean:
	rm -f $(SLIM) $(FWDPY) *.time.txt

seeds.txt: makeseeds.sh
	./makeseeds.sh

slim1.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim1.{}.time.txt ~/src/SLiM/bin/slim -d P=0.99 -d h=0.0 -d s=0.001 -d NEG=1 -seed {} slimscript.txt \> slim1.{}.stdout :::: seeds.txt
	touch slim1.txt

slim2.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim2.{}.time.txt ~/src/SLiM/bin/slim -d P=0.99 -d h=0.5 -d s=0.001 -d NEG=1 -seed {} slimscript.txt \> slim2.{}.stdout :::: seeds.txt
	touch slim2.txt

slim3.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim3.{}.time.txt ~/src/SLiM/bin/slim -d P=0.90 -d h=0.0 -d s=0.001 -d NEG=1 -seed {} slimscript.txt \> slim3.{}.stdout :::: seeds.txt
	touch slim3.txt

slim4.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim4.{}.time.txt ~/src/SLiM/bin/slim -d P=0.90 -d h=0.5 -d s=0.001 -d NEG=1 -seed {} slimscript.txt \> slim4.{}.stdout :::: seeds.txt
	touch slim4.txt

fwdpy1.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy1.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.99 -0.001 0.0 :::: seeds.txt
	touch fwdpy1.txt

fwdpy2.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy2.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.99 -0.001 0.5 :::: seeds.txt
	touch fwdpy2.txt

fwdpy3.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy3.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.90 -0.001 0.0 :::: seeds.txt
	touch fwdpy3.txt

fwdpy4.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy4.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.90 -0.001 0.5 :::: seeds.txt
	touch fwdpy4.txt
