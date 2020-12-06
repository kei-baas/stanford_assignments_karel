def main() : 
    # todo end of the code
    bank_acount_balance =  getBankAcount("enter you bank Balance")
    validValues = mounth_year_filter_all(get_mounth_year((30,2020)),bank_acount_balance)
    if validValues : 
        print("this is cs50")
        print(validValues)
        interest = enterIntersts()
        # INITIAL ACTIVE YEAR AND MOUNTH
        activeMounth = validValues['starter']['mounth']
        activeYear = validValues['starter']['year']
        # END INTIAL ACTIVE YEAR AND MOUNTH
        overaltime = calculatedTime(validValues) 
           
        for i in range(1,overaltime+1) : 
            bank_acount_balance = (someMathOperation(interest) * bank_acount_balance) + bank_acount_balance
            if(activeMounth >=12) : 
                activeMounth = 1
                activeYear = activeYear+1
                
            print(f"year :{activeYear} , month : {activeMounth} is ${bank_acount_balance}")
            activeMounth = activeMounth + 1

        return 
    

def calculatedTime(validValues) : 
    overaltime = (validValues['ending']['year'] - validValues['starter']['year']) * 12 + (validValues['ending']['mounth']-validValues['starter']['mounth'])
    return overaltime

def someMathOperation(interest) : 
    mountlyProfit = (interest / 12) / 100
    return mountlyProfit
    
def validator(filters,value) : 
    for i in filters :
        if i == value :
            return False
            


def enterIntersts() : 
    val = float(input("enter your intrest ? "))
    while not positiveNumber(val) : 
        val =  float(input("enter your intrest? "))
    return val
    
        
# get the bank balnce of the user
def getBankAcount(promptMessage) : # must return a positive float number
    bank_acount_balance = float(input("enter your balance ? | please positive numbers : 4000,20,4 | do not use $ sign | -> "))
    while not positiveNumber(bank_acount_balance) : 
        bank_acount_balance = float(input(promptMessage))
    return bank_acount_balance
    #at this point val is the bank acount 
    
# check for positivity    
def positiveNumber(number) : 
    # the positive number must also greator than zero
    if number > 0  : 
        return True 
    else : 
        return False 
    return False

def get_mounth_year(config) : 
    # config must be an tuple (mounth,yearBase)
    m_limit,y_base = config 

    def get_values(yearMes,mounthMes,flag) : 
        
        y = int(input(yearMes))
        m = int(input(mounthMes))
        while True: 
            if (y < y_base) : 
                y = int(input(yearMes))
                # year must be set again 
            if (m > m_limit) : 
                m = int(input(mounthMes))
                # mounth muset be set again
       
                
            if ((m <= m_limit) and (y >= y_base)) :
                if(positiveNumber(m)):
                    return {"type":flag,"year":y,"mounth":m}
                else:
                    m = int(input(mounthMes))
                
        
    
    
    starter_values = get_values("enter the starter Year ? | must be equal or greater than base year | ->  ","enter the starter Mouth ? | ->  ",'base')
    # the starter values for mounth and years
    ending_values = get_values("enter the ending Year ? | must be equal or greator than starter | -> ", "enter the ending Mounth ? | -> ",'head')
    # the ending values for the mountha and year
    return { 
        "starter":starter_values,
        "ending":ending_values
    }
        

        
def mounth_year_filter_all(year_mounth_obj,balance) :
    starter = year_mounth_obj['starter']
    ending = year_mounth_obj['ending']
    if ending['year'] < starter['year'] : 
        print("second year must be bigger or equal to the first year")
        alternativeYearObj = get_mounth_year((30,2020))
        return mounth_year_filter_all(alternativeYearObj,balance)
        # return False we can return false here but we dont want to terminate the process
        # here we got error in the year fo the ending phaze
    elif ending['year'] == starter['year'] : 
        if ending['mounth'] < starter['mounth'] : 
            print("second mouth must not be smaller than first mounth when both years are equal")
            alternativeYearObj = get_mounth_year((30,2020))
            return mounth_year_filter_all(alternativeYearObj,balance)
            # return False we can return false here but we dont want terminate the process
            # you have to enter the years or mounth again something error with the user input 
        elif ending['mounth'] == starter['mounth'] : 
            # here we have to return the balance
            return balance
    return year_mounth_obj
    # this means this is a valid object to be process
    pass


def validValueConversion(value,toType,toTypeLimits) : 
    vals = checkType(value,toType)

    for i in toTypeLimits : 
        if value == i : 
            return False # means you type a wrong character
        else : 
            return eval(toType)(value)
            # this is simply like this float(value)
            
            
def checkType(value,type_to_check_for) :
    valid_types = ['float','int','str'] # you can extend it also 
    for i in valid_types : 
        if type_to_check_for == i  : 
            if type(value) == eval(i) : 
                return {"type":i,"state":True,'value':value}
    return {"state":False}




def is_bool(value) : 
    if type(value) == bool : 
        return True 
    return False


def is_string(value) : 
    if type(value) == str : 
        return True 
    return False


# if __name__ == "__main__" : 
#     main()

result = checkType("hellow",'str')
print(result)