"""Controls for counting answers without confusing them with verification."""
import ast,sys
from pathlib import Path
p=Path(sys.argv[1]); tree=ast.parse(p.read_text())
f=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='has_answer')
ns={};exec('import re',ns);exec(compile(ast.Module(body=[f],type_ignores=[]),str(p),'exec'),ns)
cases=[
 ('### Answer\nCorrected: https://example.org/commit\n### Verification\n',True),
 ('### Answer\nThe finding holds. See: versioned evidence\n',True),
 ('### Answer\nPartly corrected: commit abc\n',True),
 ('### Answer\nAwaiting `Corrected:` or `See:`.\n### Verification\nCorrected: cited by auditor only\n',False),
 ('### Answer\n`Corrected:` follows with a commit.\n',False),
 ('### Verification\nSee: no answer\n',False)]
for text,want in cases:assert ns['has_answer'](text)==want,(text,want)
print('Six answer classification controls passed')
