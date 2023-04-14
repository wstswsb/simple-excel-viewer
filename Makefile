lint:
	ruff --fix ./

prettify:
	black ./

mypy_lint:
	mypy ./simple_excel_viewer/

test:
	pytest ./tests --cov ./simple_excel_viewer --cov-report term-missing
