from bs4 import BeautifulSoup
#import re
import requests
import pandas as pd

base_url = 'https://www.gsmarena.com/'

code_brand = None
brand = None

x = 0
brand = str(input('Enter Brand Name : ').lower())
a = int(input('''
    ------------------
    Start page Number  :
    ------------------
    '''))
b = int(input('''
    ------------------
    End page Number : 
    ------------------
    '''))+1

details = bool(input("type (True) for details : "))
print(details)
pics = int(input('type (1) for pics : '))

c = int(input("Number of Full Photo For Every Mob : ")) +1

for page_number in range(a,b):

    page_number = str(page_number)
    if brand=="samsung":
        code_brand = '09'
    elif brand=="nokia":
        code_brand = '1'
    elif brand=="huawei":
        code_brand = '58'
    elif brand=="sony":
        code_brand = '7'
    elif brand=="xiaomi":
        code_brand = '80'
    elif brand=="infinix":
        code_brand = '119'
    elif brand=="apple":
        code_brand = '48'
    elif brand=="htc":
        code_brand = '45'
    elif brand=="lenovo":
        code_brand = '73'
    elif brand=="honor":
        code_brand = '121'
    elif brand=="realme":
        code_brand = '118'
    elif brand=="vivo":
        code_brand = '98'
    elif brand=="asus":
        code_brand = '46'
    elif brand=="oppo":
        code_brand = '82'
    elif brand=="alcatel":
        code_brand = '5'
    elif brand=="zte":
        code_brand = '62'
    elif brand=="lg":
        code_brand = '20'
    elif brand=="motorola":
        code_brand = '4'
    elif brand=="acer":
        code_brand = '59'
    else:
        code_brand = 'None'
    
    url = base_url + brand + "-phones-f-" + code_brand + "-0-p"+ page_number +".php"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    s = requests.Session()
    s.headers.update(headers)
    product_links = []
    npo_ljnks = {}
    link_no = 0
    
    r = s.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    product_list = soup.findAll("div",  {'class': 'makers'})

    for item in product_list:
        for link in item.findAll('a', href=True):
            product_links.append(base_url + link['href'])
    print(len(product_links))
    if len(product_links) < 1:
        break
    n = 0
    for link in product_links:
        try:
            imgs = []
            li_devs = []
            r = s.get(link, headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')
            #page = page.find('div', {'id': 'specs-list'})
            if brand=="samsung":
                brd = '1'
            elif brand=="nokia":
                brd = '7'
            elif brand=="huawei":
                brd = '2'
            elif brand=="sony":
                brd = '8'
            elif brand=="xiaomi":
                brd = '5'
            elif brand=="infinix":
                brd = '6'
            elif brand=="apple":
                brd = '2'
            elif brand=="htc":
                brd = '10'
            elif brand=="lenovo":
                brd = '11'
            elif brand=="honor":
                brd = '13'
            elif brand=="realme":
                brd = '12'
            elif brand=="vivo":
                brd = '15'
            elif brand=="asus":
                brd = '17'
            elif brand=="oppo":
                brd = '4'
            elif brand=="alcatel":
                brd = '16'
            elif brand=="zte":
                brd = '14'
            elif brand=="lg":
                brd = '9'
            elif brand=="motorola":
                brd = '18'
            elif brand=="acer":
                brd = '19'
            else:
                brd = 'None'
            
            try:
                image_link = soup.find('div', {'class': 'specs-photo-main'}).find('img')['src']
            except :
                image_link = 'Not Found'
                pass
            
            try:
                name = soup.find('h1', {'class': 'specs-phone-name-title'}).text
            except :
                name = 'Not Found'
                break

            try:
                name_2 = soup.find('p', {'data-spec': 'comment'}).text
            except :
                name_2 = 'Not Found'
                pass

            slug = name.replace(' ','-')
            slug = slug.lower()

            if details == True:
                print("Start Collect Details For ",name)
                try:
                    network = soup.find('td', {'class': 'nfo'}).text
                except :
                    network = 'Not Found'
                    pass

                try:
                    technology = soup.find('a', {'data-spec': 'nettech'}).text
                except :
                    technology = 'Not Found'
                    pass

                try:
                    technology_2g = soup.find('td', {'data-spec': 'net2g'}).text
                except :
                    technology_2g = 'Not Found'
                    pass

                try:
                    technology_3g = soup.find('td', {'data-spec': 'net3g'}).text
                except :
                    technology_3g = 'Not Found'
                    pass

                try:
                    technology_4g = soup.find('td', {'data-spec': 'net4g'}).text
                except :
                    technology_4g = 'Not Found'
                    pass

                try:
                    technology_5g = soup.find('td', {'data-spec': 'net5g'}).text
                except :
                    technology_5g = 'Not Found'
                    pass

                try:
                    network_speed = soup.find('td', {'data-spec': 'speed'}).text
                except :
                    network_speed = 'Not Found'
                    pass
                
                try:
                    announced = soup.find('td', {'data-spec': 'year'}).text
                except :
                    announced = 'Not Found'
                    pass
                
                try:
                    status = soup.find('td', {'data-spec': 'status'}).text 
                except :
                    status = 'Not Found'
                    pass
                
                try:
                    dimensions = soup.find('td' , {'data-spec' : 'dimensions'}).text   
                except :
                    dimensions = 'Not Found'
                    pass
                
                try:
                    wight = soup.find('td' , {'data-spec' : 'weight'}).text
                except :
                    wight = 'Not Found wight'
                    pass

                try:
                    sim = soup.find('td' , {'data-spec' : 'sim'}).text   
                except :
                    sim = 'Not Found'
                    pass
                
                try:
                    build = soup.find('td' , {'data-spec' : 'build'}).text
                except :
                    build = 'Not Found'
                    pass
                
                # Display
                try:
                    displaytype = soup.find('td' , {'data-spec' : 'displaytype'}).text
                except :
                    displaytype = 'Not Found'
                    pass
                try:
                    displaysize = soup.find('td' , {'data-spec' : 'displaysize'}).text
                except :
                    displaysize = 'Not Found'
                    pass
                try:
                    displayresolution = soup.find('td' , {'data-spec' : 'displayresolution'}).text
                except :
                    displayresolution = 'Not Found'
                    pass
                # AndroiD & Cpu & Gpu & prcessor 
                try:
                    o_s = soup.find('td' , {'data-spec' : 'os'}).text
                except :
                    o_s = 'Not Found'
                    pass
                try:
                    chipset = soup.find('td' , {'data-spec' : 'chipset'}).text 
                except :
                    chipset = 'Not Found'
                    pass
                
                try:
                    cpu = soup.find('td' , {'data-spec' : 'cpu'}).text 
                except :
                    cpu = 'Not Found'
                    pass

                try:
                    cpu = soup.find('td' , {'data-spec' : 'gpu'}).text 
                except :
                    cpu = 'Not Found'
                    pass

                # Storage 
                try:
                    cardslot = soup.find('td' , {'data-spec' : 'memoryslot'}).text
                except :
                    cardslot = 'Not Found'
                    pass
                try:
                    internal = soup.find('td' , {'data-spec' : 'internalmemory'}).text
                except :
                    internal = 'Not Found'
                    pass


                try:
                    quantity_main_cam = soup.find('td' , {'data-spec' : 'cam1modules'}).text
                except :
                    quantity_main_cam = 'Not Found'
                    pass
                try:
                    features_main_cam = soup.find('td' , {'data-spec' : 'cam1features'}).text
                except :
                    features_main_cam = 'Not Found'
                    pass
                try:
                    video_main = soup.find('td' , {'data-spec' : 'cam1video'}).text 
                except :
                    video_main = 'Not Found'
                    pass
                try:
                    quantity_selfie_cam = soup.find('td' , {'data-spec' : 'cam2modules'}).text  
                except :
                    quantity_selfie_cam = 'Not Found'
                    pass
                try:
                    video_selfie = soup.find('td' , {'data-spec' : 'cam2video'}).text
                except :
                    video_selfie = 'Not Found'
                    pass
                try:
                    Loudspeaker = soup.find('td' , {'data-spec' : 'dimensions'}).text
                except :
                    Loudspeaker = 'Not Found'
                    pass
                try:
                    wlan = soup.find('td' , {'data-spec' : 'wlan'}).text
                except :
                    wlan = 'Not Found'
                    pass
                try:
                    bluetooth = soup.find('td' , {'data-spec' : 'dimensions'}).text
                except :
                    bluetooth = 'Not Found'
                    pass

                try:
                    nfc = soup.find('td' , {'data-spec' : 'nfc'}).text 
                except :
                    nfc = 'Not Found'
                    pass
                try:
                    radio = soup.find('td' , {'data-spec' : 'radio'}).text
                except :
                    radio = 'Not Found'
                    pass
                try:
                    usb = soup.find('td' , {'data-spec' : 'usb'}).text
                except :
                    usb = 'Not Found'
                    pass
                try:
                    sensors = soup.find('td' , {'data-spec' : 'sensors'}).text
                except :
                    sensors = 'Not Found'
                    pass
                try:
                    battery_type = soup.find('td' , {'data-spec' : 'batdescription1'}).text
                except :
                    battery_type = 'Not Found'
                    pass
                try:
                    price = soup.find('td' , {'data-spec' : 'price'}).text
                except :
                    price = 'Not Found'
                    pass
                try:
                    model = soup.find('td', {'data-spec': 'models'}).text
                except :
                    model = 'Not Found'
                    pass
                try:
                    color = soup.find('td' , {'data-spec' : 'colors'}).text
                except :
                    color = 'Not Found'
                    pass


                image_dev = 'Devices/Devices_Img/' + brand + '/' +  str(name) + '.jpg'            
                img_dev_1 = 'Devices/Devices_full_pic/' + brand + '/' +  str(name) + ' 1.jpg'
                img_dev_2 = 'Devices/Devices_full_pic/' + brand + '/' +  str(name) + ' 2.jpg'

                link_no+=1
                Mobile = {}
                Mobile[link_no] = {
                        'Name':name ,
                        'Network':network ,
                        'Announced':announced ,
                        'Status' : status ,
                        'dimensions' : dimensions ,
                        'wight' : wight ,
                        'build' : build ,
                        'sim' : sim ,
                        'displaytype' : displaytype ,
                        'displaysize' : displaysize ,
                        'displayresolution' : displayresolution ,
                        'O_S' : o_s , 
                        'chipset' : chipset,
                        'CPU' : cpu ,
                        'cardslot' : cardslot ,
                        'internal' : internal ,
                        'quan_main' : quantity_main_cam ,
                        'features' : features_main_cam ,
                        'video_main' : video_main ,
                        'quan_selfie' : quantity_selfie_cam ,
                        'video_selfie' : video_selfie ,
                        'Loudspeaker' :  Loudspeaker ,
                        'wlan' : wlan ,'bluetooth' : bluetooth ,'nfc' : nfc ,
                        'radio' : radio ,'usb' : usb ,'sensors' : sensors ,
                        'battery_type' : battery_type ,'price' : price ,
                        }
                npo_ljnks[link_no] = [ slug, brd,model, name,network,announced,status ,
                    dimensions , wight , build , sim , displaytype , displaysize , displayresolution ,
                    o_s , chipset, cpu , cardslot , internal , quantity_main_cam , 
                    features_main_cam , video_main ,quantity_selfie_cam , 
                    video_selfie , Loudspeaker  , wlan , bluetooth , nfc , 
                    radio , usb ,sensors , battery_type , price ,image_dev ,img_dev_1 , img_dev_2, color]
                ############
            
            if pics == 1 :
                li_devs = soup.findAll('li',{'class':'article-info-meta-link'})
                n += 1
                tag_pics = None
                for li in li_devs :
                    if li.text == 'Pictures':
                        tag_pics = base_url + str(li.find('a')['href'])
                        r = s.get(tag_pics)
                        soup2 = BeautifulSoup(r.content, 'lxml')
                        imgs_device = soup2.find('div',{'id':'pictures-list'})
                        x = 0
                        for tag in imgs_device.findAll('img'):
                            x += 1
                            if x < c:
                                extenss = ' ' + str(x) +'.jpg'
                                pic_name = str(name)
                                img = tag['src']
                                r = s.get(img)
                                dr = 'Pic Devices/'+ brand +'/full pics/p'+ page_number +'/'
                                with open( dr + pic_name + extenss, 'wb') as outfile:
                                    outfile.write(r.content)
                #time.sleep(10)
                print(n)
                print('-OK-------') 
                r = requests.get(image_link)
                dir_small_pic = 'Pic Devices/'+ brand + '/small pics/p'+ page_number +'/'
                with open(dir_small_pic + str(name) + '.jpg' , 'wb') as outfile:
                    outfile.write(r.content)
            
        except Exception:
            #print('error in ' + str(link))
            pass

    npo_ljnks_df = pd.DataFrame.from_dict(npo_ljnks,orient='index' ,
        columns= ['slug_dev', 'brand' , 'modeldev' , 'nameDev', 'networkDev','announcedDev', 'statusDev', 
            'dimensionsDev', 'wightDev', 'buildDev', 'simDev', 
            'displayTypeDev', 'displaySizeDev', 'displayResDev',  
            'oSDev','chipsetDev' ,'cPUDev','cardSlotDev','internalDev',
            'mainCameraDev', 'main_camera_featuresDev','main_camera_videoDev',
            'selfieCameraDev', 'selfie_camera_videoDev', 'loudspeakerDev',
            'wlanDev', 'bluetoothDev', 'nfcDev', 'radioDev' ,
            'usbDev','sensorsDev', 'batteryDev', 'priceDev' , 'imageDev', 
            'img_dev_full_1' , 'img_dev_full_2' ,'color'  ])
    
    print("Page Number ####  " + page_number + "  #### Scraped Ya Man 5alas :D :D")
    if npo_ljnks_df.to_excel('sheets/' + brand + '/GSM_'+ brand +'_p'+ page_number +'.xlsx') == True:
        print("Saved xlsx")
    else:
        print("failed sheets")