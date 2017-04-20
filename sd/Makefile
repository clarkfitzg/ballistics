# Name of the report
REPORT = sd

# $< references the first prerequisite
$(REPORT).md : $(REPORT).Rmd
	Rscript -e "rmarkdown::render(commandArgs(TRUE)[1])" $<

view :
	open $(REPORT).pdf

clean :
	rm *.aux
	rm *.log
	rm *.out
	rm *.Rout
