"""Read-only, network-free validation of preserved diagnostic transcriptions."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = {'.gitattributes', 'README.md', 'CITATION.cff', 'PROVENANCE.md', 'MANIFEST.json',
           'validate.py', 'diagnostic_records.json', 'LICENSE-MIT.txt', 'LICENSE-CC-BY-4.0.txt',
           'manuscript/research_note.tex', 'manuscript/research_note.pdf'}
FREEZE = 'c8c177b01f127043d8ba99ed06e70dfeb5b43ad7'

def require(ok, message):
    if not ok:
        raise SystemExit('FAIL: ' + message)

def validate():
    # Root .git is repository administration, never part of the public payload.
    paths = [p for child in ROOT.iterdir() if child.name != '.git'
             for p in ([child] + list(child.rglob('*')) if child.is_dir() else [child])]
    require(not any(p.is_symlink() for p in paths), 'symlinks forbidden')
    require(not any(p.name == '.git' for p in paths), 'history forbidden')
    actual = {p.relative_to(ROOT).as_posix() for p in paths if p.is_file()}
    require(actual == ALLOWED, 'inventory differs from allowlist')
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf-8'))
    require(manifest['frozen_commit'] == FREEZE, 'source commitment mismatch')
    entries = manifest['files']
    require(len(entries) == 10, 'manifest cardinality')
    require({r['path'] for r in entries} == ALLOWED - {'MANIFEST.json'}, 'manifest file set')
    for item in entries:
        require(item['path'] in ALLOWED, 'unapproved manifest path')
        data = (ROOT / item['path']).read_bytes()
        require(len(data) == item['bytes'], 'length mismatch: ' + item['path'])
        require(hashlib.sha256(data).hexdigest() == item['sha256'], 'checksum mismatch: ' + item['path'])
    tex = (ROOT / 'manuscript/research_note.tex').read_text(encoding='utf-8')
    records = json.loads((ROOT / 'diagnostic_records.json').read_text(encoding='utf-8'))
    require(records['frozen_commit'] == FREEZE, 'record source commitment')
    require(set(records) == {'record_type', 'frozen_commit', 'table_rows', 'principal_claim_map', 'preserved_gate'}, 'record schema')
    parsed = []
    blocks = re.findall(r'\\begin\{table\}.*?\\end\{table\}', tex, re.S)
    require(len(blocks) == 4, 'table count')
    for ident, block in zip(('T1', 'T2', 'T3', 'AT1'), blocks):
        body = block.split(r'\midrule', 1)[1].split(r'\bottomrule', 1)[0]
        rows = [x.strip() + r' \\' for x in body.split(r'\\') if x.strip()]
        parsed.extend((f'{ident}.{i}', row) for i, row in enumerate(rows, 1))
    rows = records['table_rows']
    require(len(rows) == 31, 'row count')
    require([(r['id'], r['frozen_latex_row']) for r in rows] == parsed, 'table transcription mismatch')
    for row in rows:
        require(set(row) == {'id', 'frozen_latex_row', 'approved_audit_description', 'approved_source_locator'}, 'table schema')
        require(bool(row['approved_source_locator']), 'missing provenance locator')
    require(len(records['principal_claim_map']) == 17, 'principal-claim count')
    for claim in records['principal_claim_map']:
        require(set(claim) == {'destination_and_claim', 'approved_claim_ids', 'evidence_ids'}, 'claim schema')
    require(records['preserved_gate'] == {'fixed_design_completed': True, 'integrity_passed': True,
                                        'comparability_passed': True, 'substantive_response_reporting_permitted': False}, 'withholding gate mismatch')
    require(not re.search(r'\\(?:input|include|includegraphics|bibliography|write18)\b', tex), 'external TeX dependency')
    require(not re.search(r'[A-Z]:[\\/]|/Users/|/home/', tex), 'machine path in manuscript')
    print('PASS: exact eleven-file payload allowlist; checksums; 31 approved table rows; 17 principal claims; withholding gate. Preserved-record verification only.')

if __name__ == '__main__':
    validate()
