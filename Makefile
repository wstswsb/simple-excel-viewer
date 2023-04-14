lint:
	ruff --fix ./

prettify:
	black ./

mypy_lint:
	mypy ./simple_excel_viewer/
