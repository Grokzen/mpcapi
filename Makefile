help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  sdist           create sdist package"
	@echo "  clean           remove temporary files created by build tools"
	@echo "  cleanmeta       removes all META-* and egg-info/ files created by build tools"	
	@echo "  cleanall        all the above + tmp files from development tools"

sdist: cleanmeta
	python setup.py sdist

clean:
	-rm -f MANIFEST
	-rm -rf dist/
	-rm -rf build/

cleanmeta:
	-rm -rf mpcapi.egg-info/

cleanall: clean cleanmeta
	-find . -type f -name "*~" -exec rm -f "{}" \;
	-find . -type f -name "*.orig" -exec rm -f "{}" \;
	-find . -type f -name "*.rej" -exec rm -f "{}" \;
	-find . -type f -name "*.pyc" -exec rm -f "{}" \;
	-find . -type f -name "*.parse-index" -exec rm -f "{}" \;
