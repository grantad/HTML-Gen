import io
import os

start_tags = [ "<!DOCTYPE html>" , "<html>" , "<head>" , "<title>" , "</title>" , "</head>" , "<body>" 
 	   ]

close_tags = ["</body>" , "</html>"]

tags = [ "<h1>" , "</h1>" , "<h2>" , "</h2>" , "<h3>" , "</h3>" , "<h4>" , "</h4>" , "<h5>" , "</h5>" , "<h6>" , "</h6>" , "<a>" , "</a>" , "<p>" , "</p>" , "<br>"]

class page:
	f = ""
	def __init__(self , f):
		f = str(f)
		if f.find(".") == -1:
			f = f + ".html"
		self.f = f
		pgname = open(f , 'a')
		self.pgname = pgname	
	lines = 0
	def file_name(self):
		return self.f
	def ret(self):
		self.pgname.write("\n")
	def start_tags(self):
		t = 0
		while t < len(start_tags):
			self.pgname.write(start_tags[t])
			if start_tags[t] == "<title>":
				title = raw_input("Title ->")
				self.pgname.write(str(title))
			t += 1
			self.ret()
	def close_tags(self):
		self.pgname.write(close_tags[0])
		self.ret()
		self.pgname.write(close_tags[1])
	def paragraph(self):
		self.pgname.write(tags[9])
		para = raw_input("Type your paragraph ->")
		self.pgname.write(str(para))
		self.pgname.write(tags[10])
		self.ret()
	def headers(self , t):
		self.ret()
		tg = raw_input("Header # ->")
		tg = int(tg)
		tg = ((tg - 1) * 2)
		self.pgname.write(tags[tg])
		text = raw_input("Text ->")
		self.pgname.write(str(text))
		self.pgname.write(tags[tg + 1])
		self.ret()
	def link(self , l):
		print "Make links" 

class script:
	print "TODO"

class style_sheet:
	print "TODO"


print "1. New File"
print "2. Open File"
w = raw_input("->")
w = int(w)
if w == 1:
	name = raw_input("File name:")
	npage = page(name)
	print "Page Setup"
	npage.start_tags()

	print "1. Paragraph"
	print "2. Headers"
	print "3. Other Tags"
	print "4. Style"
	print "5. Scripts"