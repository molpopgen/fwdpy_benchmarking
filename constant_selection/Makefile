SLIM=slim1.txt slim2.txt slim3.txt slim4.txt slim5.txt slim6.txt slim7.txt slim8.txt
FWDPY=fwdpy1.txt fwdpy2.txt fwdpy3.txt fwdpy4.txt fwdpy5.txt fwdpy6.txt fwdpy7.txt fwdpy8.txt

all: seeds.txt $(SLIM) $(FWDPY)

clean:
	rm -f $(SLIM) $(FWDPY) *.time.txt

seeds.txt: makeseeds.sh
	./makeseeds.sh

#For test cases, 1-4 are weak negative selection
#5-8 are strong positive selection (2Ns=1e3)
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

slim5.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim5.{}.time.txt ~/src/SLiM/bin/slim -d P=0.99 -d h=0.0 -d s=0.05 -d NEG=0 -seed {} slimscript.txt \> slim5.{}.stdout :::: seeds.txt
	touch slim5.txt

slim6.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim6.{}.time.txt ~/src/SLiM/bin/slim -d P=0.99 -d h=0.5 -d s=0.05 -d NEG=0 -seed {} slimscript.txt \> slim6.{}.stdout :::: seeds.txt
	touch slim6.txt

slim7.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim7.{}.time.txt ~/src/SLiM/bin/slim -d P=0.90 -d h=0.0 -d s=0.05 -d NEG=0 -seed {} slimscript.txt \> slim7.{}.stdout :::: seeds.txt
	touch slim7.txt

slim8.txt: slimscript.txt seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o slim8.{}.time.txt ~/src/SLiM/bin/slim -d P=0.90 -d h=0.5 -d s=0.05 -d NEG=0 -seed {} slimscript.txt \> slim8.{}.stdout :::: seeds.txt
	touch slim8.txt

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

fwdpy5.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy5.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.99 0.05 0.0 :::: seeds.txt
	touch fwdpy5.txt

fwdpy6.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy6.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.99 0.05 0.5 :::: seeds.txt
	touch fwdpy6.txt

fwdpy7.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy7.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.90 0.05 0.0 :::: seeds.txt
	touch fwdpy7.txt

fwdpy8.txt: run_fwdpy.py evolve.py seeds.txt
	parallel /usr/bin/time -f \"%e %M\" -o fwdpy8.{}.time.txt python run_fwdpy.py 1000 1000 {} 0.90 0.05 0.5 :::: seeds.txt
	touch fwdpy8.txt
