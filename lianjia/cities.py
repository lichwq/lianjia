CITY_LIST = [
    'shanghai',
    # 'sh',
    # 'guangzhou',
    # 'shenzhen',
    # 'chengdu',
    # 'hangzhou',
    # 'nanjing',
    # 'tianjin',
    # 'wuhan',
    # 'chongqing',
    # 'hebei',
    # 'handan',
    # 'shijiazhuang',
    # 'baoding',
    # 'zhangjiakou',
    # 'chengde',
    # 'tangshan',
    # 'langfang',
    # 'cangzhou',
    # 'hengshui',
    # 'xingtai',
    # 'qinhuangdao',
    # 'shanxi',
    # 'shuozhou',
    # 'xinzhou',
    # 'taiyuan',
    # 'datong',
    # 'yangquan',
    # 'jinzhong',
    # 'changzhi',
    # 'jincheng',
    # 'linfen',
    # 'lvliang',
    # 'yuncheng',
    # 'neimenggu',
    # 'hulunbeier',
    # 'huhehaote',
    # 'baotou',
    # 'wuhai',
    # 'wulanchabu',
    # 'tongliao',
    # 'chifeng',
    # 'eerduosi',
    # 'bayannaoer',
    # 'xilinguole',
    # 'xingan',
    # 'alashan',
    # 'liaoning',
    # 'shenyang',
    # 'tieling',
    # 'dalian',
    # 'anshan',
    # 'fushun',
    # 'benxi',
    # 'dandong',
    # 'jinzhou',
    # 'yingkou',
    # 'fuxin',
    # 'liaoyang',
    # 'chaoyang',
    # 'panjin',
    # 'huludao',
    # 'jilinn',
    # 'changchun',
    # 'jilin',
    # 'yanbian',
    # 'siping',
    # 'tonghua',
    # 'baicheng',
    # 'liaoyuan',
    # 'songyuan',
    # 'baishan',
    # 'heilongjiang',
    # 'jixi',
    # 'qitaihe',
    # 'hegang',
    # 'shuangyashan',
    # 'yichun',
    # 'haerbin',
    # 'qiqihaer',
    # 'mudanjiang',
    # 'jiamusi',
    # 'heihe',
    # 'suihua',
    # 'daqing',
    # 'daxinganling',
    # 'jiangsu',
    # 'wuxi',
    # 'zhenjiang',
    # 'suzhou',
    # 'nantong',
    # 'yangzhou',
    # 'yancheng',
    # 'xuzhou',
    # 'huaian',
    # 'lianyungang',
    # 'changzhou',
    # 'tz',
    # 'suqian',
    # 'kunshan',
    # 'changshu',
    # 'zhangjiagang',
    # 'taicang',
    # 'zhejiang',
    # 'quzhou',
    # 'huzhou',
    # 'jiaxing',
    # 'ningbo',
    # 'shaoxing',
    # 'taizhou',
    # 'wenzhou',
    # 'lishui',
    # 'jinhua',
    # 'zhoushan',
    # 'anhui',
    # 'chuzhou',
    # 'fuyang',
    # 'hefei',
    # 'bengbu',
    # 'wuhu',
    # 'huainan',
    # 'maanshan',
    # 'anqing',
    # 'sz',
    # 'bozhou',
    # 'huangshan',
    # 'huaibei',
    # 'tongling',
    # 'xuancheng',
    # 'luan',
    # 'chaohu',
    # 'chizhou',
    # 'shandong',
    # 'taian',
    # 'heze',
    # 'jinan',
    # 'qingdao',
    # 'zibo',
    # 'dezhou',
    # 'yantai',
    # 'weifang',
    # 'jining',
    # 'weihai',
    # 'linyi',
    # 'binzhou',
    # 'dongying',
    # 'zaozhuang',
    # 'rizhao',
    # 'laiwu',
    # 'liaocheng',
    # 'henan',
    # 'shangqiu',
    # 'zhengzhou',
    # 'anyang',
    # 'xinxiang',
    # 'xuchang',
    # 'pingdingshan',
    # 'xinyang',
    # 'nanyang',
    # 'kaifeng',
    # 'luoyang',
    # 'jiaozuo',
    # 'hebi',
    # 'puyang',
    # 'zhoukou',
    # 'luohe',
    # 'zhumadian',
    # 'sanmenxia',
    # 'jiyuan',
    # 'hunan',
    # 'yueyang',
    # 'changsha',
    # 'xiangtan',
    # 'zhuzhou',
    # 'hengyang',
    # 'chenzhou',
    # 'changde',
    # 'yiyang',
    # 'loudi',
    # 'shaoyang',
    # 'xiangxi',
    # 'zhangjiajie',
    # 'huaihua',
    # 'yongzhou',
    # 'hubei',
    # 'xiantao',
    # 'tianmen',
    # 'qianjiang',
    # 'xiangfan',
    # 'ezhou',
    # 'xiaogan',
    # 'huanggang',
    # 'huangshi',
    # 'xianning',
    # 'jingzhou',
    # 'yichang',
    # 'shiyan',
    # 'suizhou',
    # 'jingmen',
    # 'enshi',
    # 'shennongjia',
    # 'jiangxi',
    # 'yingtan',
    # 'xinyu',
    # 'nanchang',
    # 'jiujiang',
    # 'shangrao',
    # 'fz',
    # 'yc',
    # 'jian',
    # 'ganzhou',
    # 'jingdezhen',
    # 'pingxiang',
    # 'fujian',
    # 'fuzhou',
    # 'xiamen',
    # 'ningde',
    # 'putian',
    # 'quanzhou',
    # 'zhangzhou',
    # 'longyan',
    # 'sanming',
    # 'nanping',
    # 'guangdong',
    # 'shanwei',
    # 'yangjiang',
    # 'jieyang',
    # 'maoming',
    # 'jiangmen',
    # 'shaoguan',
    # 'huizhou',
    # 'meizhou',
    # 'shantou',
    # 'zhuhai',
    # 'foshan',
    # 'zhaoqing',
    # 'zhanjiang',
    # 'zhongshan',
    # 'heyuan',
    # 'qingyuan',
    # 'yunfu',
    # 'chaozhou',
    # 'dongguan',
    # 'guangxi',
    # 'laibin',
    # 'hezhou',
    # 'chongzuo',
    # 'yl',
    # 'fangchenggang',
    # 'nanning',
    # 'liuzhou',
    # 'guilin',
    # 'wuzhou',
    # 'guigang',
    # 'bose',
    # 'qinzhou',
    # 'hechi',
    # 'beihai',
    # 'hannan',
    # 'sanya',
    # 'danzhou',
    # 'dongfang',
    # 'wenchang',
    # 'qionghai',
    # 'wuzhishan',
    # 'wanning',
    # 'haikou',
    # 'baisha',
    # 'sansha',
    # 'baoting',
    # 'changjiang',
    # 'chengmai',
    # 'dingan',
    # 'ledong',
    # 'lingao',
    # 'lingshui',
    # 'qiongzhong',
    # 'tunchang',
    # 'sichuan',
    # 'meishan',
    # 'ziyang',
    # 'panzhihua',
    # 'zigong',
    # 'mianyang',
    # 'nanchong',
    # 'dazhou',
    # 'suining',
    # 'guangan',
    # 'bazhong',
    # 'luzhou',
    # 'yibin',
    # 'neijiang',
    # 'leshan',
    # 'liangshan',
    # 'yaan',
    # 'ganzi',
    # 'aba',
    # 'deyang',
    # 'guangyuan',
    # 'guizhou',
    # 'guiyang',
    # 'zunyi',
    # 'anshun',
    # 'qiannan',
    # 'qiandongnan',
    # 'tongren',
    # 'bijie',
    # 'liupanshui',
    # 'qianxinan',
    # 'yunnan',
    # 'xishuangbanna',
    # 'dehong',
    # 'zhaotong',
    # 'kunming',
    # 'dali',
    # 'honghe',
    # 'qujing',
    # 'baoshan',
    # 'wenshan',
    # 'yuxi',
    # 'chuxiong',
    # 'puer',
    # 'lincang',
    # 'nujiang',
    # 'diqing',
    # 'lijiang',
    # 'xizang',
    # 'lasa',
    # 'rikaze',
    # 'shannan',
    # 'linzhi',
    # 'changdu',
    # 'naqu',
    # 'ali',
    # 'shaanxi',
    # 'xian',
    # 'xianyang',
    # 'yanan',
    # 'yulin',
    # 'weinan',
    # 'shangluo',
    # 'ankang',
    # 'hanzhong',
    # 'baoji',
    # 'tongchuan',
    # 'gansu',
    # 'longnan',
    # 'wuwei',
    # 'jiayuguan',
    # 'linxia',
    # 'lanzhou',
    # 'dingxi',
    # 'pingliang',
    # 'qingyang',
    # 'jinchang',
    # 'zhangye',
    # 'jiuquan',
    # 'tianshui',
    # 'gannan',
    # 'baiyin',
]