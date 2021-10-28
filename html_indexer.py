
base_file="html_base.txt"

###Using the "@" as a separator, when the for comes to it's line writes all the data 
def write_file(text, filename):
    c=open(base_file,"r")
    html=""
    for line in c.readlines():
        if(line.__contains__("@")):
            html+=text
        else:    
            html+=str(line)    

    with open(filename,'w') as f:
        f.write(html)
        f.close()
    c.close()

def convert2HTML(dic):
    s = '<UL>\n'
    tags = [x for x in dic]
    for tag in tags:
        s += f'\t<LI>{tag[1:]}: {dic[tag]}</LI>\n'
    s += '</UL>'
    return s




def write_to_file(dic,file):
    text= convert2HTML(dic)
    write_file(text,file)


def parse_search(matches,file):
    return convert2HTML(matches)

def parse_document(doc):
    authors=""
    i=0
    for auth in doc.authors: 
        i+=1
        authors += auth 
        if(i<len(doc.authors)>1):
            authors+=","

    s="<strong>"+str(doc.title)+"</strong>"
    s+="<p> Autores:"+str(authors)+" </p>"
    s+="<p> Categoría:"+str(doc.category)  +" </p>"
    s+="<p> Clave:"+str(doc.key)+" </p>"


def write_document(documents,file):
    text=""
    for document in documents:
        text += parse_document(document)
    write_file(text,file)




