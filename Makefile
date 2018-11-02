all: help

help:
	@echo 'Makefile help:                                           '
	@echo '                                                         '
	@echo '   tests-py        Run tests for Python                  '

tests-py:
	@cd symbsat-py && python3 -m unittest tests/test_*.py

.PHONY: all help tests-py
