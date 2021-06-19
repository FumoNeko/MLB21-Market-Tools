import time
import json
import requests

#intentions
#def request():
#    uuid = "6ce0a227d926a8d0f23afd8d51a80695"
#    r = requests.get('https://mlb21.theshow.com/apis/listing.json?uuid=' + uuid)
#    data = json.loads(r.text)
#    print(data["listing_name"])
#    print(data["best_buy_price"])
#    print(data["best_sell_price"])
#
#
#request()

r = """{
  "listing_name": "Mike Trout",
  "best_sell_price": 406500,
  "best_buy_price": 393500,
  "item": {
    "uuid": "6ce0a227d926a8d0f23afd8d51a80695",
    "img": "https://mlb21.theshow.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbjVqIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--364426441567d96536e02762276a00e8b4bc497d/ac222fd2c12adecfc7a891d9d18ddc45.jpg",
    "name": "Mike Trout",
    "rarity": "Diamond",
    "team": "Angels",
    "ovr": 96,
    "series": "Live"
  },
  "price_history": [{
    "date": "5/10",
    "best_buy_price": 397000,
    "best_sell_price": 400000
  }, {
    "date": "5/09",
    "best_buy_price": 387000,
    "best_sell_price": 405000
  }, {
    "date": "5/08",
    "best_buy_price": 383102,
    "best_sell_price": 392000
  }, {
    "date": "5/07",
    "best_buy_price": 373000,
    "best_sell_price": 380000
  }, {
    "date": "5/06",
    "best_buy_price": 360750,
    "best_sell_price": 372999
  }, {
    "date": "5/05",
    "best_buy_price": 364005,
    "best_sell_price": 383966
  }, {
    "date": "5/04",
    "best_buy_price": 366559,
    "best_sell_price": 381444
  }, {
    "date": "5/03",
    "best_buy_price": 371101,
    "best_sell_price": 384999
  }, {
    "date": "5/02",
    "best_buy_price": 366020,
    "best_sell_price": 386500
  }, {
    "date": "5/01",
    "best_buy_price": 380001,
    "best_sell_price": 405000
  }, {
    "date": "4/30",
    "best_buy_price": 355555,
    "best_sell_price": 376899
  }, {
    "date": "4/29",
    "best_buy_price": 341015,
    "best_sell_price": 363500
  }, {
    "date": "4/28",
    "best_buy_price": 339000,
    "best_sell_price": 354450
  }, {
    "date": "4/27",
    "best_buy_price": 345200,
    "best_sell_price": 358000
  }, {
    "date": "4/26",
    "best_buy_price": 341000,
    "best_sell_price": 360000
  }, {
    "date": "4/25",
    "best_buy_price": 335000,
    "best_sell_price": 345000
  }, {
    "date": "4/24",
    "best_buy_price": 348000,
    "best_sell_price": 369797
  }, {
    "date": "4/23",
    "best_buy_price": 333333,
    "best_sell_price": 349999
  }, {
    "date": "4/22",
    "best_buy_price": 335200,
    "best_sell_price": 355999
  }, {
    "date": "4/21",
    "best_buy_price": 334050,
    "best_sell_price": 369666
  }, {
    "date": "4/20",
    "best_buy_price": 361000,
    "best_sell_price": 380000
  }, {
    "date": "4/19",
    "best_buy_price": 345701,
    "best_sell_price": 379777
  }, {
    "date": "4/18",
    "best_buy_price": 339000,
    "best_sell_price": 355998
  }, {
    "date": "4/17",
    "best_buy_price": 347200,
    "best_sell_price": 399850
  }, {
    "date": "4/16",
    "best_buy_price": 0,
    "best_sell_price": 0
  }, {
    "date": "4/15",
    "best_buy_price": 0,
    "best_sell_price": 0
  }],
  "completed_orders": [{
    "date": "5/10/2021 2:15:17 PM",
    "price": "393,502"
  }, {
    "date": "5/10/2021 2:08:57 PM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 2:08:20 PM",
    "price": "405,000"
  }, {
    "date": "5/10/2021 1:57:09 PM",
    "price": "395,010"
  }, {
    "date": "5/10/2021 1:50:20 PM",
    "price": "395,006"
  }, {
    "date": "5/10/2021 1:49:34 PM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 1:46:39 PM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 1:39:58 PM",
    "price": "396,004"
  }, {
    "date": "5/10/2021 1:36:07 PM",
    "price": "397,000"
  }, {
    "date": "5/10/2021 1:26:16 PM",
    "price": "406,999"
  }, {
    "date": "5/10/2021 1:15:30 PM",
    "price": "395,005"
  }, {
    "date": "5/10/2021 1:14:28 PM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 1:10:31 PM",
    "price": "401,002"
  }, {
    "date": "5/10/2021 12:57:43 PM",
    "price": "401,100"
  }, {
    "date": "5/10/2021 12:51:24 PM",
    "price": "401,200"
  }, {
    "date": "5/10/2021 12:44:29 PM",
    "price": "401,500"
  }, {
    "date": "5/10/2021 12:21:22 PM",
    "price": "401,110"
  }, {
    "date": "5/10/2021 12:09:08 PM",
    "price": "412,000"
  }, {
    "date": "5/10/2021 11:52:22 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 11:36:33 AM",
    "price": "400,001"
  }, {
    "date": "5/10/2021 11:10:24 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 11:03:00 AM",
    "price": "393,150"
  }, {
    "date": "5/10/2021 10:42:41 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 10:32:50 AM",
    "price": "394,000"
  }, {
    "date": "5/10/2021 10:29:27 AM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 10:27:06 AM",
    "price": "398,000"
  }, {
    "date": "5/10/2021 10:17:18 AM",
    "price": "399,000"
  }, {
    "date": "5/10/2021 9:57:37 AM",
    "price": "417,999"
  }, {
    "date": "5/10/2021 9:43:56 AM",
    "price": "403,337"
  }, {
    "date": "5/10/2021 9:43:56 AM",
    "price": "417,999"
  }, {
    "date": "5/10/2021 9:38:42 AM",
    "price": "417,998"
  }, {
    "date": "5/10/2021 9:28:25 AM",
    "price": "399,010"
  }, {
    "date": "5/10/2021 9:11:28 AM",
    "price": "415,000"
  }, {
    "date": "5/10/2021 8:52:58 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 8:47:02 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 8:46:16 AM",
    "price": "393,100"
  }, {
    "date": "5/10/2021 8:44:47 AM",
    "price": "409,999"
  }, {
    "date": "5/10/2021 8:37:20 AM",
    "price": "394,000"
  }, {
    "date": "5/10/2021 8:32:53 AM",
    "price": "409,999"
  }, {
    "date": "5/10/2021 8:30:35 AM",
    "price": "409,950"
  }, {
    "date": "5/10/2021 8:30:17 AM",
    "price": "409,900"
  }, {
    "date": "5/10/2021 8:27:28 AM",
    "price": "407,500"
  }, {
    "date": "5/10/2021 8:26:04 AM",
    "price": "394,000"
  }, {
    "date": "5/10/2021 8:20:58 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 8:19:02 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 7:59:04 AM",
    "price": "398,267"
  }, {
    "date": "5/10/2021 7:58:28 AM",
    "price": "405,000"
  }, {
    "date": "5/10/2021 7:49:40 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 7:48:58 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 7:46:40 AM",
    "price": "397,500"
  }, {
    "date": "5/10/2021 7:43:44 AM",
    "price": "397,501"
  }, {
    "date": "5/10/2021 7:37:33 AM",
    "price": "404,444"
  }, {
    "date": "5/10/2021 7:32:47 AM",
    "price": "399,000"
  }, {
    "date": "5/10/2021 7:32:14 AM",
    "price": "404,443"
  }, {
    "date": "5/10/2021 7:28:59 AM",
    "price": "403,000"
  }, {
    "date": "5/10/2021 7:28:35 AM",
    "price": "397,001"
  }, {
    "date": "5/10/2021 7:16:36 AM",
    "price": "395,599"
  }, {
    "date": "5/10/2021 7:14:26 AM",
    "price": "402,500"
  }, {
    "date": "5/10/2021 7:09:41 AM",
    "price": "402,250"
  }, {
    "date": "5/10/2021 7:03:29 AM",
    "price": "394,300"
  }, {
    "date": "5/10/2021 7:01:36 AM",
    "price": "394,500"
  }, {
    "date": "5/10/2021 6:59:36 AM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 6:56:18 AM",
    "price": "404,400"
  }, {
    "date": "5/10/2021 6:55:37 AM",
    "price": "404,399"
  }, {
    "date": "5/10/2021 6:54:18 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 6:48:20 AM",
    "price": "395,250"
  }, {
    "date": "5/10/2021 6:39:16 AM",
    "price": "395,001"
  }, {
    "date": "5/10/2021 6:37:27 AM",
    "price": "395,250"
  }, {
    "date": "5/10/2021 6:37:20 AM",
    "price": "396,025"
  }, {
    "date": "5/10/2021 6:36:41 AM",
    "price": "396,026"
  }, {
    "date": "5/10/2021 6:36:31 AM",
    "price": "396,028"
  }, {
    "date": "5/10/2021 6:35:41 AM",
    "price": "396,027"
  }, {
    "date": "5/10/2021 6:32:57 AM",
    "price": "396,100"
  }, {
    "date": "5/10/2021 6:31:03 AM",
    "price": "396,100"
  }, {
    "date": "5/10/2021 6:28:49 AM",
    "price": "397,999"
  }, {
    "date": "5/10/2021 6:28:11 AM",
    "price": "398,002"
  }, {
    "date": "5/10/2021 6:24:22 AM",
    "price": "396,222"
  }, {
    "date": "5/10/2021 6:18:41 AM",
    "price": "396,055"
  }, {
    "date": "5/10/2021 6:17:24 AM",
    "price": "416,999"
  }, {
    "date": "5/10/2021 6:16:53 AM",
    "price": "415,555"
  }, {
    "date": "5/10/2021 6:14:12 AM",
    "price": "396,056"
  }, {
    "date": "5/10/2021 6:13:43 AM",
    "price": "419,891"
  }, {
    "date": "5/10/2021 6:13:40 AM",
    "price": "419,700"
  }, {
    "date": "5/10/2021 6:12:46 AM",
    "price": "414,999"
  }, {
    "date": "5/10/2021 6:09:28 AM",
    "price": "414,900"
  }, {
    "date": "5/10/2021 6:06:01 AM",
    "price": "414,994"
  }, {
    "date": "5/10/2021 6:03:44 AM",
    "price": "399,001"
  }, {
    "date": "5/10/2021 6:02:21 AM",
    "price": "399,100"
  }, {
    "date": "5/10/2021 5:59:11 AM",
    "price": "402,000"
  }, {
    "date": "5/10/2021 5:57:31 AM",
    "price": "419,500"
  }, {
    "date": "5/10/2021 5:55:47 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 5:54:23 AM",
    "price": "418,999"
  }, {
    "date": "5/10/2021 5:53:47 AM",
    "price": "410,001"
  }, {
    "date": "5/10/2021 5:48:48 AM",
    "price": "418,420"
  }, {
    "date": "5/10/2021 5:44:08 AM",
    "price": "397,001"
  }, {
    "date": "5/10/2021 5:43:37 AM",
    "price": "417,500"
  }, {
    "date": "5/10/2021 5:43:34 AM",
    "price": "397,000"
  }, {
    "date": "5/10/2021 5:41:42 AM",
    "price": "397,400"
  }, {
    "date": "5/10/2021 5:41:29 AM",
    "price": "397,500"
  }, {
    "date": "5/10/2021 5:39:02 AM",
    "price": "419,400"
  }, {
    "date": "5/10/2021 5:37:31 AM",
    "price": "396,005"
  }, {
    "date": "5/10/2021 5:37:27 AM",
    "price": "396,006"
  }, {
    "date": "5/10/2021 5:30:41 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 5:29:27 AM",
    "price": "419,890"
  }, {
    "date": "5/10/2021 5:27:00 AM",
    "price": "415,000"
  }, {
    "date": "5/10/2021 5:26:30 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 5:25:36 AM",
    "price": "399,000"
  }, {
    "date": "5/10/2021 5:25:28 AM",
    "price": "396,501"
  }, {
    "date": "5/10/2021 5:20:06 AM",
    "price": "404,420"
  }, {
    "date": "5/10/2021 5:19:57 AM",
    "price": "404,400"
  }, {
    "date": "5/10/2021 5:17:35 AM",
    "price": "395,027"
  }, {
    "date": "5/10/2021 5:17:14 AM",
    "price": "396,050"
  }, {
    "date": "5/10/2021 5:17:01 AM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 5:16:48 AM",
    "price": "396,005"
  }, {
    "date": "5/10/2021 5:15:16 AM",
    "price": "399,000"
  }, {
    "date": "5/10/2021 5:13:03 AM",
    "price": "407,999"
  }, {
    "date": "5/10/2021 5:12:01 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 5:09:40 AM",
    "price": "397,001"
  }, {
    "date": "5/10/2021 5:07:54 AM",
    "price": "408,000"
  }, {
    "date": "5/10/2021 5:07:03 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 5:05:01 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 5:01:57 AM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 5:00:44 AM",
    "price": "410,000"
  }, {
    "date": "5/10/2021 5:00:07 AM",
    "price": "403,000"
  }, {
    "date": "5/10/2021 4:59:42 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 4:59:05 AM",
    "price": "402,990"
  }, {
    "date": "5/10/2021 4:57:22 AM",
    "price": "397,500"
  }, {
    "date": "5/10/2021 4:55:39 AM",
    "price": "397,250"
  }, {
    "date": "5/10/2021 4:54:56 AM",
    "price": "397,250"
  }, {
    "date": "5/10/2021 4:51:53 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 4:48:18 AM",
    "price": "403,999"
  }, {
    "date": "5/10/2021 4:48:10 AM",
    "price": "403,000"
  }, {
    "date": "5/10/2021 4:47:43 AM",
    "price": "402,999"
  }, {
    "date": "5/10/2021 4:47:33 AM",
    "price": "396,039"
  }, {
    "date": "5/10/2021 4:47:02 AM",
    "price": "396,553"
  }, {
    "date": "5/10/2021 4:45:24 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 4:44:10 AM",
    "price": "396,300"
  }, {
    "date": "5/10/2021 4:41:38 AM",
    "price": "395,508"
  }, {
    "date": "5/10/2021 4:39:58 AM",
    "price": "402,998"
  }, {
    "date": "5/10/2021 4:39:40 AM",
    "price": "402,992"
  }, {
    "date": "5/10/2021 4:38:47 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 4:38:01 AM",
    "price": "394,650"
  }, {
    "date": "5/10/2021 4:37:53 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 4:36:06 AM",
    "price": "402,991"
  }, {
    "date": "5/10/2021 4:35:39 AM",
    "price": "402,990"
  }, {
    "date": "5/10/2021 4:34:36 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 4:33:25 AM",
    "price": "398,000"
  }, {
    "date": "5/10/2021 4:30:43 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 4:30:16 AM",
    "price": "402,996"
  }, {
    "date": "5/10/2021 4:30:01 AM",
    "price": "402,000"
  }, {
    "date": "5/10/2021 4:28:07 AM",
    "price": "396,456"
  }, {
    "date": "5/10/2021 4:27:11 AM",
    "price": "402,000"
  }, {
    "date": "5/10/2021 4:26:59 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 4:26:57 AM",
    "price": "400,000"
  }, {
    "date": "5/10/2021 4:24:16 AM",
    "price": "399,990"
  }, {
    "date": "5/10/2021 4:22:50 AM",
    "price": "394,676"
  }, {
    "date": "5/10/2021 4:22:26 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 4:21:28 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 4:17:34 AM",
    "price": "396,000"
  }, {
    "date": "5/10/2021 4:16:55 AM",
    "price": "402,000"
  }, {
    "date": "5/10/2021 4:16:02 AM",
    "price": "398,001"
  }, {
    "date": "5/10/2021 4:12:23 AM",
    "price": "396,001"
  }, {
    "date": "5/10/2021 4:12:15 AM",
    "price": "404,994"
  }, {
    "date": "5/10/2021 4:11:28 AM",
    "price": "398,022"
  }, {
    "date": "5/10/2021 4:09:22 AM",
    "price": "397,000"
  }, {
    "date": "5/10/2021 4:08:58 AM",
    "price": "396,001"
  }, {
    "date": "5/10/2021 4:07:07 AM",
    "price": "396,500"
  }, {
    "date": "5/10/2021 4:04:42 AM",
    "price": "396,001"
  }, {
    "date": "5/10/2021 4:04:19 AM",
    "price": "397,006"
  }, {
    "date": "5/10/2021 4:04:10 AM",
    "price": "397,005"
  }, {
    "date": "5/10/2021 4:00:06 AM",
    "price": "395,000"
  }, {
    "date": "5/10/2021 3:59:12 AM",
    "price": "400,500"
  }, {
    "date": "5/10/2021 3:58:43 AM",
    "price": "400,501"
  }, {
    "date": "5/10/2021 3:58:17 AM",
    "price": "414,998"
  }, {
    "date": "5/10/2021 3:57:25 AM",
    "price": "400,508"
  }, {
    "date": "5/10/2021 3:56:50 AM",
    "price": "415,500"
  }, {
    "date": "5/10/2021 3:56:21 AM",
    "price": "405,002"
  }, {
    "date": "5/10/2021 3:54:33 AM",
    "price": "405,000"
  }, {
    "date": "5/10/2021 3:51:02 AM",
    "price": "403,502"
  }, {
    "date": "5/10/2021 3:50:42 AM",
    "price": "403,600"
  }, {
    "date": "5/10/2021 3:50:31 AM",
    "price": "403,601"
  }, {
    "date": "5/10/2021 3:49:12 AM",
    "price": "404,200"
  }, {
    "date": "5/10/2021 3:48:48 AM",
    "price": "405,000"
  }, {
    "date": "5/10/2021 3:47:20 AM",
    "price": "419,950"
  }, {
    "date": "5/10/2021 3:47:18 AM",
    "price": "419,945"
  }, {
    "date": "5/10/2021 3:46:06 AM",
    "price": "404,000"
  }, {
    "date": "5/10/2021 3:46:00 AM",
    "price": "419,191"
  }, {
    "date": "5/10/2021 3:45:59 AM",
    "price": "403,501"
  }, {
    "date": "5/10/2021 3:45:43 AM",
    "price": "405,000"
  }, {
    "date": "5/10/2021 3:43:50 AM",
    "price": "419,999"
  }, {
    "date": "5/10/2021 3:43:19 AM",
    "price": "404,156"
  }, {
    "date": "5/10/2021 3:40:53 AM",
    "price": "414,994"
  }, {
    "date": "5/10/2021 3:40:27 AM",
    "price": "414,980"
  }, {
    "date": "5/10/2021 3:38:30 AM",
    "price": "414,900"
  }, {
    "date": "5/10/2021 3:37:08 AM",
    "price": "414,800"
  }, {
    "date": "5/10/2021 3:36:53 AM",
    "price": "414,785"
  }, {
    "date": "5/10/2021 3:35:53 AM",
    "price": "400,003"
  }, {
    "date": "5/10/2021 3:35:16 AM",
    "price": "414,000"
  }, {
    "date": "5/10/2021 3:34:42 AM",
    "price": "412,500"
  }, {
    "date": "5/10/2021 3:33:37 AM",
    "price": "413,999"
  }]
}
"""
data = json.loads(r)
print(data["item"]["uuid"])