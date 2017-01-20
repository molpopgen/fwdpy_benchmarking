SLIM=slim1.txt slim2.txt slim3.txt slim4.txt
all: seeds.txt $(SLIM)
clean:
	rm -f $(SLIM)
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
