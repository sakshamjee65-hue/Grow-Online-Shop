# -*- coding: utf-8 -*-
import json
import os

transcript_path = r"C:\Users\Saksham\.gemini\antigravity-ide\brain\7c2457ed-c985-4c58-9115-9b23833c18f3\.system_generated\logs\transcript_full.jsonl"

last_valid_html = None

with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if 'index.html' in line and 'CodeContent' in line:
            try:
                d = json.loads(line)
                for tc in d.get('tool_calls', []):
                    args = tc.get('args', {})
                    if 'index.html' in args.get('TargetFile', '') and len(args.get('CodeContent', '')) > 30000:
                        last_valid_html = args['CodeContent']
            except Exception:
                pass

if last_valid_html:
    with open('index_restored.html', 'w', encoding='utf-8') as out:
        out.write(last_valid_html)
    print("Restored index_restored.html successfully, length:", len(last_valid_html))
else:
    print("No valid index.html found in transcript!")
