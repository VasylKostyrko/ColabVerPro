def findErrMsg(lang, errCode):
    """Відображає повідомлення про помилку!"""
    errDictMsg = messLang[errCode]
    errMsg = errDictMsg[lang]
    return errMsg

def viewErrMsg(errMsg):
    """Відображає повідомлення про помилку
    в підвалі клітинки"""
	print(errMsg)
