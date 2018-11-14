# Scrape car listings from Autotrader.com using scrapy

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
 
|title                                             |engine           |miles_used              |color                 |price                 |drive_type           |mpg           |list_type                                                                                                                                                                                                                                                                                                                                                                                                                       |searched_zipcode                                                                                                                                                                                                                                                                                                                                                                                                                                  |link | 
|-----------------------------------------------------|--------------------|---------------------------|-------------------------|-------------------------|------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------| 
|Used 2015 Audi A8 L 4.0T                          |8-Cylinder Turbo |25,839 miles            |White,$41,500       |All wheel drive       |18 City / 29 Highway |Newly Listed  |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497468736&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=AUDI&modelCode1=A8&digitalRetail=true&clickType=listing     |        | 
|Used 2003 Toyota Highlander Limited V6            |6-Cylinder       |99,440 miles            |Gold,$6,499         |4 wheel drive - front |18 City / 22 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498367789&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=TOYOTA&modelCode1=HIGHLANDER&clickType=listing              |        | 
|Used 2011 Ford Fusion SE                          |Hybrid           |50,550 miles            |White,$9,998        |2 wheel drive - front |41 City / 36 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497808272&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing                    |        | 
|Used 2015 Ford Fusion SE                          |4-Cylinder       |23,258 miles|$12,999 |2 wheel drive - front |22 City / 34 Highway  |Reduced Price        |20005         |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497613664&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing  |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |        | 
|Used 2016 Ford Fiesta Titanium Hatchback          |4-Cylinder       |10,598 miles            |Silver,$13,222      |2 wheel drive - front |27 City / 36 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496798119&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FIESTA&clickType=listing                    |        | 
|Used 2015 Honda Civic LX Sedan                    |4-Cylinder       |22,502 miles            |Silver,$13,699      |2 wheel drive - front |30 City / 39 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499121102&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing                    |        | 
|Used 2015 Honda Civic LX Sedan                    |4-Cylinder       |16,728 miles            |Silver,$13,799      |2 wheel drive - front |30 City / 39 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499235826&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing                    |        | 
|Used 2017 Ford Fiesta Titanium Hatchback          |4-Cylinder       |9,810 miles             |Black,$13,991       |2 wheel drive - front |27 City / 37 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496747290&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FIESTA&clickType=listing                    |        | 
|Used 2016 Chevrolet Cruze LT Sedan                |4-Cylinder Turbo |14,810 miles            |Red,$14,650         |2 wheel drive - front |30 City / 42 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494466951&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CHEV&modelCode1=CRUZE&clickType=listing                     |        | 
|Used 2015 Ford Fusion SE Hybrid                   |Hybrid           |28,764 miles|$15,225 |2 wheel drive - front |44 City / 41 Highway  |Reduced Price        |20005         |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=495692488&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing  |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |        | 
|Used 2016 Ford Fusion Energi SE Luxury            |Hybrid           |14,333 miles            |Black,$16,687       |2 wheel drive - front |40 City / 36 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497783145&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FUSION&clickType=listing                    |        | 
|Used 2016 Ford C-MAX SEL                          |Hybrid           |16,009 miles            |Black,$16,777       |2 wheel drive - front |40 City / 36 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496628196&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=FOCMAX&clickType=listing                    |        | 
|Used 2016 Honda Civic LX-P Coupe                  |4-Cylinder       |17,618 miles            |Black,$16,999       |2 wheel drive - front |30 City / 41 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=499002844&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=CIVIC&clickType=listing                    |        | 
|Used 2016 Ford Escape FWD SE                      |4-Cylinder Turbo |18,622 miles            |Black,$17,225       |2 wheel drive - front |23 City / 32 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496231623&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=FORD&modelCode1=ESCAPE&digitalRetail=true&clickType=listing |        | 
|Certified 2015 GMC Terrain FWD SLE                |4-Cylinder       |25,014 miles            |Gray,$17,656        |2 wheel drive - front |22 City / 32 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498001320&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=GMC&modelCode1=TERRAIN&clickType=listing                    |        | 
|Used 2016 Acura ILX w/ Premium Package            |4-Cylinder       |17,434 miles            |Gray,$18,925        |2 wheel drive - front |25 City / 36 Highway |Newly Listed  |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494512320&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=ACURA&modelCode1=ILX&clickType=listing                      |        | 
|Used 2015 Lincoln MKZ Hybrid                      |Hybrid           |22,700 miles            |Black,$20,390       |2 wheel drive - front |41 City / 39 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494302769&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=LINC&modelCode1=MKZ&digitalRetail=true&clickType=listing    |        | 
|Used 2016 Chevrolet Traverse FWD LS               |6-Cylinder       |19,793 miles            |Gray,$20,775        |2 wheel drive - front |15 City / 22 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=495797704&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CHEV&modelCode1=TRAVERSE&clickType=listing                  |        | 
|Used 2015 Audi A4 2.0T Premium quattro Sedan      |4-Cylinder Turbo |26,676 miles            |White,$21,599       |All wheel drive       |22 City / 31 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=496531639&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=AUDI&modelCode1=A4&clickType=listing                        |        | 
|Certified 2015 Lincoln MKC FWD                    |4-Cylinder Turbo |24,356 miles            |Red,$23,444         |2 wheel drive - front |20 City / 29 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=498381676&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=LINC&modelCode1=LINCMKC&clickType=listing                   |        | 
|Used 2015 Cadillac ATS 2.0T Performance AWD Sedan |4-Cylinder Turbo |27,430 miles            |Gray,$24,390        |All wheel drive       |20 City / 28 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=494512293&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CAD&modelCode1=ATS&digitalRetail=true&clickType=listing     |        | 
|Used 2014 Cadillac XTS Premium                    |6-Cylinder       |24,377 miles            |Blue,$24,990        |2 wheel drive - front |18 City / 28 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497415243&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=CAD&modelCode1=XTS&clickType=listing                        |        | 
|Used 2018 Honda HR-V AWD EX-L w/ Navigation       |4-Cylinder       |2,832 miles,,$24,999  |All wheel drive       |27 City / 31 Highway  |Reduced Price        |20005         |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497627593&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=HONHRV&clickType=listing |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |        | 
|Used 2018 Honda Odyssey LX                        |6-Cylinder       |5,219 miles             |White,$26,999       |2 wheel drive - front |19 City / 28 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497627595&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=HONDA&modelCode1=ODYSSEY&clickType=listing                  |        | 
|Certified 2015 Buick Enclave AWD Leather          |6-Cylinder       |23,773 miles            |Blue,$27,353        |All wheel drive       |16 City / 22 Highway |Reduced Price |20005                                                                                                                                                                                                                                                                                                                                                                                                                           |https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=497902938&zip=20005&referrer=%2Fcars-for-sale%2Fsearchresults.xhtml%3Fzip%3D20005%26startYear%3D1981%26sortBy%3Drelevance%26incremental%3Dall%26firstRecord%3D0%26marketExtension%3Don%26endYear%3D2019%26searchRadius%3D50&startYear=1981&numRecords=25&firstRecord=0&endYear=2019&searchRadius=50&makeCode1=BUICK&modelCode1=ENCLAVE&clickType=listing                  |        | 
