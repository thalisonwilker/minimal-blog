#-*-coding: UTF-8 -*-
import json
URL = "https://thalisonwilker.github.io/minimal-blog/posts/"

def git_push(commit=""):
	import os
	systemout = os.system("git add ./*")
	if systemout == 0:
		print "git add ./* [OK]"

	systemout = os.system("git commit -m '"+commit+"'")
	if systemout == 0:
		print "git commit -m 'Commit' [OK]"

	systemout = os.system("git push -u origin master")
	if systemout == 0:
		print "git push -u origin master [OK]"

def update_posts_list():
	posts = ""

	for line in open("urls","r").readlines():

		link = line.split("#")
		print link
		posts += "<a class='post-link' href="+link[0]+">\n\t"+link[1]+"</a>\n"


	template = open("template_index.html", "r")
	index_r_str = template.read()
	index_r_str = index_r_str.replace("$posts$", posts)
	template.read()

	index_w = open("index.html", "w")
	index_w.write(index_r_str)
	index_w.close()
	

header_html = open("header.html","r")
header = header_html.read()

footer_html = open("footer.html","r")
footer = footer_html.read()

urls = open("urls", "a")

title = raw_input("Titulo: ")

content = raw_input("Post: ")

header = header.replace("$title$", title)

post_body = "<div class='card-post'>\n\t\t<h1 class='post-header'>"+title+"</h1>\n\t\t<p class='post-content'>"+content+"</p>\n</div>"

post_body = header+"\n"+post_body+"\n"+footer

title_ = title

title = title.replace(" ","-").lower()

urls.write(URL+""+title+".html#"+title_+"\n" )
urls.close()

post = open("posts/"+title+".html","w")

post.write(post_body)

header_html.close()
post.close()
footer_html.close()



update_posts_list()
git_push(title_)
