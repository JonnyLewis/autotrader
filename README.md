# Scrape sale details from Autotrader.com using scrapy

A Scrapy spider to extract car sale information from autotrader.com.

## Fields

 - Price (in US dollars)
 - Title
 - Used (in Miles)
 - Color
 - mpg
 - Drive Type
 - Engine
 - Link
 - List Type
 - Searched Zipcode

## Requirements 
- Python 3 
- Scrapy

## Running the Scraper
 - Change the URL in `start_urls` from `main.py`
 -  Run command `scrapy crawl autotrader_spider -o out.csv -t csv` to get data as CSV into a file called out.csv or `scrapy crawl autotrader_spider -o out.json -t json` to get data as JSON File.
 
 ## Sample Output 
 
 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| miles_used,mpg,link,drive_type,list_type,title,color,searched_zipcode,price,engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| ,,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499883116&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&clickType=alpha,,Newly Listed,Used 2017 BMW X5 M,,20005,"$78,400",                                                                                                                                                        | 
| "25,839 miles",18 City / 29 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497468736&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=AUDI&modelCode1=A8&digitalRetail=true&clickType=listing,All wheel drive,Newly Listed,Used 2015 Audi A8 L 4.0T,White,20005,"$41,500",8-Cylinder Turbo                          | 
| "99,440 miles",18 City / 22 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498367789&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=TOYOTA&modelCode1=HIGHLANDER&clickType=listing,4 wheel drive - front,Reduced Price,Used 2003 Toyota Highlander Limited V6,Gold,20005,"$6,499",6-Cylinder                      | 
| "50,550 miles",41 City / 36 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497808272&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing,2 wheel drive - front,Reduced Price,Used 2011 Ford Fusion SE,White,20005,"$9,998",Hybrid                                             | 
| "23,258 miles",22 City / 34 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497613664&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing,2 wheel drive - front,Reduced Price,Used 2015 Ford Fusion SE,,20005,"$12,999",4-Cylinder                                             | 
| "10,598 miles",27 City / 36 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496798119&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FIESTA&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Ford Fiesta Titanium Hatchback,Silver,20005,"$13,222",4-Cylinder                       | 
| "22,502 miles",30 City / 39 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499121102&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing,2 wheel drive - front,Reduced Price,Used 2015 Honda Civic LX Sedan,Silver,20005,"$13,699",4-Cylinder                                 | 
| "16,728 miles",30 City / 39 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499235826&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing,2 wheel drive - front,Reduced Price,Used 2015 Honda Civic LX Sedan,Silver,20005,"$13,799",4-Cylinder                                 | 
| "9,810 miles",27 City / 37 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496747290&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FIESTA&clickType=listing,2 wheel drive - front,Reduced Price,Used 2017 Ford Fiesta Titanium Hatchback,Black,20005,"$13,991",4-Cylinder                         | 
| "14,810 miles",30 City / 42 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494466951&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CHEV&modelCode1=CRUZE&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Chevrolet Cruze LT Sedan,Red,20005,"$14,650",4-Cylinder Turbo                           | 
| "28,764 miles",44 City / 41 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=495692488&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing,2 wheel drive - front,Reduced Price,Used 2015 Ford Fusion SE Hybrid,,20005,"$15,225",Hybrid                                          | 
| "14,333 miles",40 City / 36 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497783145&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Ford Fusion Energi SE Luxury,Black,20005,"$16,687",Hybrid                              | 
| "16,009 miles",40 City / 36 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496628196&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FOCMAX&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Ford C-MAX SEL,Black,20005,"$16,777",Hybrid                                            | 
| "17,618 miles",30 City / 41 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499002844&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Honda Civic LX-P Coupe,Black,20005,"$16,999",4-Cylinder                                | 
| "18,622 miles",23 City / 32 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496231623&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=ESCAPE&digitalRetail=true&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Ford Escape FWD SE,Black,20005,"$17,225",4-Cylinder Turbo           | 
| "25,014 miles",22 City / 32 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498001320&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=GMC&modelCode1=TERRAIN&clickType=listing,2 wheel drive - front,Reduced Price,Certified 2015 GMC Terrain FWD SLE,Gray,20005,"$17,656",4-Cylinder                               | 
| "17,434 miles",25 City / 36 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494512320&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=ACURA&modelCode1=ILX&clickType=listing,2 wheel drive - front,Newly Listed,Used 2016 Acura ILX w/ Premium Package,Gray,20005,"$18,925",4-Cylinder                              | 
| "22,700 miles",41 City / 39 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494302769&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=LINC&modelCode1=MKZ&digitalRetail=true&clickType=listing,2 wheel drive - front,Reduced Price,Used 2015 Lincoln MKZ Hybrid,Black,20005,"$20,390",Hybrid                        | 
| "19,793 miles",15 City / 22 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=495797704&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CHEV&modelCode1=TRAVERSE&clickType=listing,2 wheel drive - front,Reduced Price,Used 2016 Chevrolet Traverse FWD LS,Gray,20005,"$20,775",6-Cylinder                            | 
| "26,676 miles",22 City / 31 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496531639&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=AUDI&modelCode1=A4&clickType=listing,All wheel drive,Reduced Price,Used 2015 Audi A4 2.0T Premium quattro Sedan,White,20005,"$21,599",4-Cylinder Turbo                        | 
| "24,356 miles",20 City / 29 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498381676&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=LINC&modelCode1=LINCMKC&clickType=listing,2 wheel drive - front,Reduced Price,Certified 2015 Lincoln MKC FWD,Red,20005,"$23,444",4-Cylinder Turbo                             | 
| "27,430 miles",20 City / 28 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494512293&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CAD&modelCode1=ATS&digitalRetail=true&clickType=listing,All wheel drive,Reduced Price,Used 2015 Cadillac ATS 2.0T Performance AWD Sedan,Gray,20005,"$24,390",4-Cylinder Turbo | 
| "24,377 miles",18 City / 28 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497415243&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CAD&modelCode1=XTS&clickType=listing,2 wheel drive - front,Reduced Price,Used 2014 Cadillac XTS Premium,Blue,20005,"$24,990",6-Cylinder                                       | 
| "2,832 miles",27 City / 31 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497627593&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=HONHRV&clickType=listing,All wheel drive,Reduced Price,Used 2018 Honda HR-V AWD EX-L w/ Navigation,,20005,"$24,999",4-Cylinder                                | 
| "5,219 miles",19 City / 28 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497627595&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=ODYSSEY&clickType=listing,2 wheel drive - front,Reduced Price,Used 2018 Honda Odyssey LX,White,20005,"$26,999",6-Cylinder                                     | 
| "23,773 miles",16 City / 22 Highway,https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497902938&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=BUICK&modelCode1=ENCLAVE&clickType=listing,All wheel drive,Reduced Price,Certified 2015 Buick Enclave AWD Leather,Blue,20005,"$27,353",6-Cylinder                             | 
