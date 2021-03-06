#encoding: utf-8

import sys
from nltk.tokenize.nist import NISTTokenizer as Tokenizer

def segline(strin, tok, to_lower = False):
	def clearstr(lin, to_lower):
		rs = []
		for tmpu in lin:
			if tmpu:
				rs.append(tmpu)
		if to_lower:
			return " ".join(rs).lower()
		else:
			return " ".join(rs).lower()
	return clearstr(tok.tokenize(strin, return_str=True).split(), to_lower)

def handle(srcfile,rsfile):
	err=0
	ens="\n".encode("utf-8")
	with open(rsfile,"wb") as fwrt:
		with open(srcfile,"rb") as frd:
			tok = Tokenizer()
			for line in frd:
				tmp=line.strip()
				if tmp:
					try:
						tmp = tmp.decode("utf-8")
					except Exception as e:
						tmp = ""
					if tmp:
						tmp=segline(tmp, tok)
						if tmp:
							fwrt.write(tmp.encode("utf-8", "ignore"))
						else:
							err+=1
					else:
						err+=1
				fwrt.write(ens)
	if err>0:
		print("".join(("Seg:",srcfile,",Error:",str(err),)))

if __name__=="__main__":
	handle(sys.argv[1], sys.argv[2])
