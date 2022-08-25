#
# How to use Janome with multi-processing.
# Hironobu Suzuki 
#
import sys
from multiprocessing import Pool, Manager
from janome.tokenizer import Tokenizer

def doJanome(lineData):
	text=lineData.text
	output=""
	for token in Tokenizer().tokenize(text):
		l=str(token).split('\t')
		k=str(l[1]).split(',')
		if k[0] == '動詞' and k[1] == '自立':
			output+=k[6]+","
		if k[0] == '名詞' and k[1] == 'サ変接続':
			output+=k[6]+","

	output=output.rstrip(',')	# 最後に余計な','がついているのを削除
	lineData.set(output)	# カンマで区切られた文字列 (CSV)
	return

class dataContainer:
	def __init__(self):
		self.text=""
		self.manager=Manager().list(range(0)) 

	def add(self,text_):
		self.text += text_	# 子プロセスに送るための入れ物

	def set(self,container_):	# 親プロセスに戻すための入れ物
		self.manager.append(container_)

	def get(self):
		return self.manager[0]


CPUs=16
textData=[]
for i in range(CPUs):
	textData.append(dataContainer())

content=sys.stdin.read()        # 標準入力からすべてを読み込む。

idx=0
for line in content.splitlines():
	textData[idx%CPUs].add(line) # 行単位で分配
	idx+=1

with Pool(CPUs) as pool:
	pool.map(doJanome,textData) # 並列処理

# 一覧作成
	for content in textData:
		for w in content.get().split(','):
			print(w)
##print("All Finished")
