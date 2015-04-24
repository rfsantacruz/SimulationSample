clean-lib:
	rm -f -r build/*

clean-cpp:
	rm -f src/*.cpp
    
clean-py:
	rm -f src/*.pyc
	rm -f test/*.pyc

clean-all: clean-lib clean-cpp clean-py


.PHONY: build
build: clean-all
	python src/setup.py build_ext
