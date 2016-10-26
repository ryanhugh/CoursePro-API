CoursePro.io API
=================================================
API to access all of the class data available at CoursePro.io.   

Python code in demo.py

userId
-----------------------
change the userId on each request to your project name  
similar to this: https://github.com/reddit/reddit/wiki/API  


POST https://coursepro.io/listColleges
-----------------------
Request:
```
{
   "userId":"Demo API"
} 
```


Response:
```
[
    {
        "url": "neu.edu",
        "host": "neu.edu",
        "_id": "HqtXHB89V8S6BpRo",
        "title": "Northeastern University"
    }
   ...
]
```


POST https://coursepro.io/listTerms
-----------------------
Request:
```
{
  "userId":"Demo API",
  "host":"neu.edu"
}
```

Response:
```
[
    {
        "text": "Spring 2015",
        "host": "neu.edu",
        "termId": "201530",
        "_id": "BoIfVpV8OFnD9qpX"
    },
    {
        "text": "Spring 2016",
        "host": "neu.edu",
        "termId": "201630",
        "_id": "O1KNWBWioW3MmL6p"
    },
    ...
]
```

POST https://coursepro.io/listSubjects
-----------------------
Request:
```
{
  "userId":"Demo API",
  "host":"neu.edu",
  "termId":"201630"
}
```

Response:
```
[
    {
        "text": "Electrical and Comp Engineerng",
        "host": "neu.edu",
        "termId": "201630",
        "_id": "05e5Or9bB6Kg7vNV",
        "subject": "EECE"
    },
    {
        "text": "Global Studies - CPS Sem",
        "host": "neu.edu",
        "termId": "201630",
        "_id": "0AtOEvPRy1bulBsA",
        "subject": "GBST"
    }
    ...
]
```



POST https://coursepro.io/listClasses
-----------------------
Request:
```
{
  "userId":"Demo API",
  "host":"neu.edu",
  "termId":"201630",
  "subject":"CS"
}
```

prettyUrl is guaranteed to be a valid url, but sometimes may not exist


Response:
```
[
    {
        "classId": "6540",
        "_id": "0Q8zfrwXk7Tk1rW6",
        "name": "Foundations of Formal Methods and Software Analysis",
        "url": "https://wl11gp.neu.edu/udcprod8/bwckctlg.p_disp_listcrse?term_in=201630&subj_in=CS&crse_in=6540&schd_in=%25",
        "crns": [],
        "host": "neu.edu",
        "prettyUrl": "https://wl11gp.neu.edu/udcprod8/bwckctlg.p_disp_course_detail?cat_term_in=201630&subj_code_in=CS&crse_numb_in=6540",
        "prereqs": {
            "values": [
                {
                    "classId": "6520",
                    "subject": "CS"
                }
            ],
            "type": "and"
        },
        "subject": "CS",
        "termId": "201630",
        "desc": "Covers necessary mathematical background such as first-order logic, and some measure theory. Studies the formal methods in more depth and breadth. Discusses the current state of the art in verification and semantics of probabilistic, real-time, and hybrid systems. Prereq. CS 6520; restricted to students in the College of Computer and Information Science. 4.000 Lecture hours"
    }
    ...
]
```



POST https://coursepro.io/listSections
-----------------------
Request:
```
{
  "userId":"Demo API",
  "host":"neu.edu",
  "termId":"201630",
  "subject":"CS",
  "classId":"4800"
}
```

`startDate` and `endDate` are days since Jan 1, 1970.  
`start` and `end` are minutes since the beginning of the day.  



Response:
```
[
    {
        "classId": "4800",
        "seatsCapacity": 80,
        "url": "https://wl11gp.neu.edu/udcprod8/bwckschd.p_disp_detail_sched?term_in=201630&crn_in=35776",
        "seatsRemaining": 61,
        "meetings": [
            {
                "startDate": 16811,
                "times": {
                    "2": [
                        {
                            "start": 55500,
                            "end": 61500
                        }
                    ],
                    "5": [
                        {
                            "start": 55500,
                            "end": 61500
                        }
                    ]
                },
                "endDate": 16911,
                "where": "International Village 019",
                "profs": [
                    "Jacek Ossowski"
                ]
            },
            {
                "startDate": 16913,
                "endDate": 16920,
                "where": "Tba",
                "profs": [
                    "Jacek Ossowski"
                ]
            }
        ],
        "waitCapacity": 0,
        "host": "neu.edu",
        "termId": "201630",
        "waitRemaining": 0,
        "_id": "9L8BouW3cMCPKJMA",
        "crn": "35776",
        "subject": "CS"
    }
    ...
]
```
