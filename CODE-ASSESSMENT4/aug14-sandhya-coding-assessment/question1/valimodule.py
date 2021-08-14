import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_donor(name,address,bloodgroup,pincode,mobile_number,place,emailid):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",address)
    val3=re.match("^(A|B|AB|O)[+-]$",bloodgroup)
    val4=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
    val5=re.search("^[7-9][0-9]{9}",mobile_number)
    val6=re.match("([a-z]+)([a-z]+)([a-z]+)$",place)
    val7=re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailid)
    try:
        if val1 and val2 and val3 and val4 and val5 and val6 and val7:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")