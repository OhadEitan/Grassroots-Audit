"""Bounded source checks of response claims, not execution of GLP semantics."""
import json,re,sys,hashlib
from pathlib import Path
root=Path(sys.argv[1])
out={"source_commit":"d56822c2e6c474d883f8535bd63d0ef1b6381486","method":"source inspection and exact set comparison"}
rows=[]
for app,count in [('gai',23),('gsnp',36)]:
    phone=(root/f'programs/social/graph/core/{app}_phone.glp').read_text()
    cert=re.search(r'sign\(creator_cert\(Src\?, \[([^]]+)\], (.+)\), K\?, CSig\)',phone).groups()
    names=re.findall(r'[a-z][a-z_0-9]*',cert[0])
    schemas=re.findall(r'\bsas\(([a-z][a-z_0-9]*),',(root/f'programs/gai/{app.upper()}.glp').read_text())
    compiled=re.findall(r'^schema_entry\(([a-z][a-z_0-9]*),',(root/f'programs/apps/{app}/platform.vglp').read_text(),re.M)
    verdict=(root/f'cascade/{app.upper()}/verdict.txt').read_text().strip()
    assert len(names)==len(set(names))==len(schemas)==len(compiled)==count
    assert set(names)==set(schemas)==set(compiled)
    assert cert[1]==verdict
    rows.append(dict(app=app,act_count=count,contract_certificate_platform_sets_equal=True,verdict_equal=True,names=sorted(names)))
out['certificates']=rows
cssn=(root/'programs/cssn/CSSN.glp').read_text()
english=re.split(r'^Logic pragmas\s*$', (root/'programs/cssn/CSSN.txt').read_text(), maxsplit=1, flags=re.M)[0]
assert 'Bob knows Carol' in english
ca=next(l for l in cssn.splitlines() if 'sas(children_acquaint,' in l)
assert "atom(knows, ['Bob', 'Carol'])" in ca
oa=next(l for l in cssn.splitlines() if 'sas(of_age,' in l)
assert "atom(creator, ['Alice', 'Carol'])" in oa
assert "atom(has_parent, ['Carol', 'Bob'])" in oa
assert "atom(has_parent, ['Carol', 'Alice'])" not in oa
assert "atom(parent, ['Alice', 'Carol'])" not in oa
assert "not(atom(has_parent, ['Carol', '_']))" in oa
out['cssn']={'finding_1':'English clause now explicitly requires Bob knows Carol, matching the schema.','finding_2':'Creator Alice remains authorized when another parent Bob remains; the schema no longer requires Alice to remain a parent. Runtime play is checked separately.'}
gb=(root/'programs/currencies/bonds/GB.glp').read_text()
escrow={}
for act in ['deposit','deposit_bond','release','release_bond','return','return_bond']:
    line=next(l for l in gb.splitlines() if f'sas({act},' in l)
    asset='escrow_bond' if 'bond' in act else 'escrow_coin'
    args="['Carol', 'Dave', num('Day'), 'Alice', 'Bob', 'Cond']" if 'bond' in act else "['Carol', 'Dave', 'Alice', 'Bob', 'Cond']"
    assert f'atom({asset}, {args})' in line
    assert '], true, [' in line
    escrow[act]=line.strip()
out['gb']={'finding_1':'Partially repaired: escrow records include depositor, beneficiary and condition, consumed by release/return. The condition remains uninterpreted and the enforced mark is unresolved.','schemas':escrow}
print(json.dumps(out,indent=2))
