# VivaLaWeekend
## Overview
This is a tool intended to simplify both course selection and semester planning at Minerva. Eventually, I see this answering the following question: "Given a course schedule for a semester, when should I take assignment extensions to balance out my workload?"
## Structure
This tool has 5 parts, each of which build on each other in order:
1. Syllabus Update(r): pulls all new syllabi from Minerva's website to ensure data is up-to-date
2. Syllabus Parser: parses Minerva syllabus and returns assignment information
3. Database: stores assignment information
4. Recommender(er): recommends when to start and turn in assignments given parameters
5. Website: place for students to go, select which courses they are taking, and spits back workload recommendation

## To-Do's
1. Build Syllabus Update(r): pulls and saves all undergraduate syllabi from hub.minerva.kgi.edu
2. Beautify Syllabus Parser: clean and understandable code, returns assignment data in concise format
3. Stress Test Syllabus Parser: parser correctly reads every Minerva syllabus
4. Build Database: runs syllabus update(r), parses, stores data in database
5. Build Recommender(er): takes in courseload and recommends when to take assignments based on assignment weight, assignment due date, normalized course weight (user specified), and available assignment extensions (user specified)
6. Build UI: barebones webpage that communicates with backend, should update user specified courses every GET request
7. Data Protection: google oauth for minerva emails
8. Website: Integrate and push to heroku

## Ideas
1. Flag courses / assignments that are due on a 5-day break
2. How long to spend on each class based on projected read time
3. When to take absences?
4. LO applications given course grades, assignment LO's, and target grade