from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='β'
			else: make_text+='β'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = 'π©πππ¬πππ«π ππ§ππ¨... \n\n'
    msg+= 'πππ¨π¦ππ«π: ' + str(filename)+'\n'
    msg+= 'ππππ¦ππ§Μπ¨ ππ¨π­ππ₯: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'π₯πππ¬πππ«π ππ§ππ¨: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'πΆπππ₯π¨ππ’πππ: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'β°ππ’ππ¦π©π¨: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = 'π©πππ¬πππ«π ππ§ππ¨ ππ«ππ‘π’π―π¨π©\n\n'
    msg += 'π¦ππ«ππ‘π’π―π¨: '+filename+'\n\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'πππ¨π«π¬ππ§π­ππ£π: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'ππππ¦ππ§Μπ¨ ππ¨π­ππ₯: '+sizeof_fmt(totalBits)+'\n'
    msg += 'π₯πππ¬πππ«π ππ§ππ¨: '+sizeof_fmt(currentBits)+'\n'
    msg += 'πΆπππ₯π¨ππ’πππ: '+sizeof_fmt(speed)+'/s\n'
    msg += 'β°ππ’ππ¦π©π¨ πππ¬π­ππ§π­π: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= 'β/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = 'βππ?ππ’ππ§ππ¨... \n\n'
    msg+= 'πππ¨π¦ππ«π: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'β«ππ?ππ’ππ§ππ¨: ' + str(filename)+'\n'
    msg+= 'ππππ¦ππ§Μπ¨ ππ¨π­ππ₯: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= 'π€ππ?ππ’ππ¨: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= 'πΆπππ₯π¨ππ’πππ: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= 'πππ’ππ¦π©π¨: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = 'βππ?ππ’ππ§ππ¨ π π₯π ππ?ππβ\n\n'
    msg += 'πππ¨π¦ππ«π: '+filename+'\n\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= 'π¦ππ«ππ‘π’π―π¨: ' + str(filename)+'\n\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += 'πππ¨π«πππ§π­ππ£π: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += 'ππππ¦ππ§Μπ¨ ππ¨π­ππ₯: '+sizeof_fmt(totalBits)+'\n'
    msg += 'π€ππ?ππ’ππ¨: '+sizeof_fmt(currentBits)+'\n'
    msg += 'πΆπππ₯π¨ππ’πππ: '+sizeof_fmt(speed)+'/s\n'
    msg += 'β°ππ’ππ¦π©π¨ πππ¬π­ππ§π­π: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'πππ¨π¦π©π«π’π¦π’ππ§ππ¨... \n\n'
    msg+= 'πππ¨π¦ππ«π: ' + str(filename)+'\n\n'
    msg+= 'ππππ¦ππ§Μπ¨ ππ¨π­ππ₯: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ππππ¦ππ§Μπ¨ πππ«π­ππ¬: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'πΎπππ§π­π’πππ πππ«π­ππ¬: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = 'βππ«π¨πππ¬π¨ ππ’π§ππ₯π’π³πππ¨β\n\n'
    msg+= 'πππ¨π¦ππ«π: ' + str(filename)+'\n\n'
    msg+= 'ππππ¦ππ§Μπ¨ π­π¨π­ππ₯: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ππππ¦ππ§Μπ¨ πππ«π­ππ¬: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= 'π€πππ«π­ππ¬ ππ?ππ’πππ¬: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= 'πππ¨π«π«ππ« ππ«ππ‘π’π―π¨: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>πππ§π₯ππππ¬π</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">π' + f['name'] + 'π</a>'
            msg+= "<a href='"+url+"'>π"+f['name']+'π</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = 'πππ«ππ‘π’π―π¨π¬ ('+str(len(evfiles))+')π\n\nπππ¨π«π«ππ« π­π¨ππ¨ /delallπ\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= 'π/txt_'+ str(i) + 'π/del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'βοΈππ? ππ§ππ¨π«π¦πππ’π¨π§βοΈ\n\n'
    msg+= 'πππ¨π¦ππ«π: @' + str(username)+'\n'
    msg+= 'π€ππ¬ππ«: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'ππππ¬π¬π°π¨π«π: ' + str(userdata['moodle_password'])+'\n'
    msg+= 'π‘ππ¨π¬π­: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'ποΈπππ©π¨ππ: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= 'π·οΈππ₯π¨π?πππ²π©π: ' + str(userdata['cloudtype'])+'\n'
    msg+= 'πππ©π­π²π©π: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= 'ποΈππ’π«: /' + str(userdata['dir'])+'\n'
    msg+= 'ππππ¦ππ§Μπ¨ ππ ππ’π©π¬: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'β'
    if isadmin:
        msgAdmin = 'β'
    msg+= 'ππππ¦π’π§ : ' + msgAdmin + '\n'
    proxy = 'β'
    if userdata['proxy'] !='':
       proxy = 'β'
    token = 'β'
    if userdata['token']!=0:
       token = 'β'
    xdlink = 'β'
    if userdata['xdmode']!=0:
    	xdlink = 'β'
    msg+= 'β‘ππ«π¨π±π² : ' + proxy + '\n\n'
    msg+= 'π?ππ¨π€ππ§ : ' + token + '\n'
    msg+= 'π―πππ₯π’π§π€ : ' + xdlink + '\n\n'
    return msg
