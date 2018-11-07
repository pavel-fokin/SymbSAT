CPPDIR=$(CURDIR)/symbsat-cpp
PYDIR=$(CURDIR)/symbsat-py
BUILDDIR=$(CURDIR)/build

.PHONY: all
all: help

.PHONY: help
help:
	@echo 'Makefile help:                         '
	@echo '                                       '
	@echo '   compile         Compile C++ code    '
	@echo '   tests-cpp       Run tests for C++   '
	@echo '   tests-py        Run tests for Python'

.PHONY: clean
clean-cpp:
	@[ ! -d $(BUILDDIR) ] || rm -rf $(BUILDDIR)

.PHONY: compile
compile: clean-cpp
	 mkdir $(BUILDDIR) && cd $(BUILDDIR) && cmake $(CPPDIR) && make -j$(nproc)

.PHONY: tests-py
tests-py:
	@cd $(PYDIR) && python3 -m unittest $(PYDIR)/tests/test_*.py

.PHONY: tests-cpp
tests-cpp: compile
	@$(BUILDDIR)/tests/unittests

.PHONY: coverage-py
coverage-py:
	@cd $(PYDIR) && coverage run --branch -m unittest $(PYDIR)/tests/test_*.py
