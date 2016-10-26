import requests
import random
import json

#change this to whatever your project is
# similar to this: https://github.com/reddit/reddit/wiki/API
userId = 'CoursePro.io demo API'


r = requests.post("https://coursepro.io/listColleges", json={'userId':userId})

if r.status_code!=200:
	print 'There was an error',r.status_code,r.reason,r
	exit()

#parse the json
colleges = json.loads(r.text)


# print all the data returned
# print colleges


print 'Colleges:'
for college in colleges:
	print college['title'],':',college['host']
print


# pick some random college
aCollegeIndex = int(len(colleges)*random.random())
aCollege = colleges[aCollegeIndex]

# print that college
print 'Using',aCollege['title']
print

#get more data about this college
r = requests.post("https://coursepro.io/listTerms", json={'userId':userId,'host':aCollege['host']})


if r.status_code!=200:
	print 'There was an error',r.status_code,r.reason,r
	exit()

#parse the json
terms = json.loads(r.text)


# print all the data returned
# print terms


print 'Terms:'
for term in terms:
	print term['text'],':',term['termId']
print


# pick some random term
aTermIndex = int(len(terms)*random.random())
aTerm = terms[aTermIndex]

# print that term
print 'Using',aTerm['text']
print


#get more data about this term
r = requests.post("https://coursepro.io/listSubjects", json={'userId':userId,'host':aCollege['host'],'termId':aTerm['termId']})


if r.status_code!=200:
	print 'There was an error',r.status_code,r.reason,r
	exit()

#parse the json
subjects = json.loads(r.text)

# print all the data returned
# print subjects



print 'Subjects:',
for subject in subjects:

	#in subject there is sometimes one or more that don't have text, ignore these
	if 'text' in subject:
		print subject['text'],':',subject['subject']
print

aSubject = {}

# if we picked the one subject that dosen't have a text, pick again
while 'text' not in aSubject:

	# pick some random subject
	aSubjectIndex = int(len(subject)*random.random())
	aSubject = subjects[aSubjectIndex]

# print that subject
print 'Using',aSubject['text']
print




#get more data about this term
r = requests.post("https://coursepro.io/listClasses", json={'userId':userId,'host':aCollege['host'],'termId':aTerm['termId'],'subject':aSubject['subject']})


if r.status_code!=200:
	print 'There was an error',r.status_code,r.reason,r
	exit()

#parse the json
classes = json.loads(r.text)


# print all the data returned
# print classes


print 'Classes:',
for aClass in classes:
	print aClass['name'],':',aClass['classId']
print


# pick some random subject
aClassIndex = int(len(classes)*random.random())
aClass = classes[aClassIndex]

# print that subject
print 'Using',aClass['name']
print



#get more data about this term
r = requests.post("https://coursepro.io/listSections", json={'userId':userId,'host':aCollege['host'],'termId':aTerm['termId'],'subject':aSubject['subject'],'classId':aClass['classId']})


if r.status_code!=200:
	print 'There was an error',r.status_code,r.reason,r
	exit()

#parse the json
sections = json.loads(r.text)

# print all the data returned
# print sections

if len(sections)==0:
	print 'No sections found!'
else:
	print 'Sections:',
	for section in sections:
		print section['seatsRemaining'],'out of',section['seatsCapacity'],'seats left!'
	print



