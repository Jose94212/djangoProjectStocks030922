s=[
    # {
    #     "3IINFOLTD": {}
    # },
    {
        "3MINDIA": {
            "2022-09-12": {
                "Open": 22839.95,
                "Close": 22806.15,
                "%Deliverble": 0.7961
            },
            "2022-09-13": {
                "Open": 22949.95,
                "Close": 22802.15,
                "%Deliverble": 0.6803
            }
        }
    },
    {
        "4THDIM": {}
    },
    {
        "5PAISA": {
            "2022-09-12": {
                "Open": 351.25,
                "Close": 352.4,
                "%Deliverble": 0.6633
            },
            "2022-09-13": {
                "Open": 360.0,
                "Close": 356.85,
                "%Deliverble": 0.6333
            }
        }
    },
    {
        "AARTIDRUGS": {
            "2022-09-12": {
                "Open": 469.75,
                "Close": 464.85,
                "%Deliverble": 0.42869999999999997
            },
            "2022-09-13": {
                "Open": 464.85,
                "Close": 462.9,
                "%Deliverble": 0.48119999999999996
            }
        }
    }
    ]



for i in s:
    for k,v in i.items():
        # print(list(v.keys())[1])
        list_deliverable=[]
        for datee,vv in v.items():
            print(datee)
            print(vv.get("%Deliverble"))
            list_deliverable.append(vv.get("%Deliverble"))
        print("\t",list_deliverable)
        print("\t","bigger is:",list_deliverable[1]>list_deliverable[0])
        #     print(kk,"\t",vv,"\t")
        #     print("\t\t\t",type(vv))
