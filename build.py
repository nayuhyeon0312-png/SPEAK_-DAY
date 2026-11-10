import fitz, glob, re, json, os
pdf=glob.glob('/mnt/data/files/*.pdf')[0]
doc=fitz.open(pdf)
entries=[]
for page_no,page in enumerate(doc,1):
    for colx in (48,299):
        blocks=[]
        for b in page.get_text('blocks'):
            x,y,x1,y1,t,*_=b
            if abs(x-colx)<8 and y<800:
                value=' '.join(t.split())
                if value: blocks.append((y,value))
        blocks.sort()
        for i,(y,word) in enumerate(blocks[:-1]):
            if re.fullmatch(r"[A-Za-z][A-Za-z'-]*",word) and not (len(word)==1 and word.isupper() and word!='I'):
                y2,definition=blocks[i+1]
                # In this PDF, vocabulary labels and their definitions are separated by ~13.7 pt.
                if 12 < y2-y < 15:
                    entries.append({'word':word,'definition':definition})
# Alphabetical source order; the PDF is laid out in paired columns.
entries.sort(key=lambda x:x['word'].lower())
assert len(entries)==721, f'Expected 721 entries, got {len(entries)}'
assert len({x['word'].lower() for x in entries})==721, 'Duplicate vocabulary labels detected'
with open('/mnt/data/speak-day/words.json','w',encoding='utf-8') as f: json.dump(entries,f,ensure_ascii=False,indent=2)
print('Extracted',len(entries),'words. First 20:',[x['word'] for x in entries[:20]])
