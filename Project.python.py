//second time
// Third Time


import os,shutil
dicti={
'Audio_file':('.mp3','.m4a','.wav','.flac'),
'Video_file':('.mp4','.mkv','.MKV','.flv','.mpeg','.3gp'),
'Document_file':('.doc','.pdf','.txt','.pptx')
}


a=input('enter your folderpth')



def fun(folder_path,file_extension):
    num=[]
    for i in os.listdir(folder_path):
        for j in file_extension:
            if i.endswith(j):
                num.append(i)
    return num




for i,j in dicti.items():
    folder_name=i.split('_')[0]+ 'file'
    folder_path=os.path.join(a,folder_name)
    os.mkdir(folder_path)
    for item in fun(a,j):
        item_path=os.path.join(a,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)




#print(fun(a,Audio_file))
                
        
