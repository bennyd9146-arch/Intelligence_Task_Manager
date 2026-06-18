## תיאור המערכת

הפרוייקט הוא ניהול משימות לסוכנים הפרוייקט נותן מידע מה המצב  של כל סוכן וכך לדעת איזה משימות  לתת \להוריד מהסוכן  



## מבנה התיקיות


intelligence-task-manager/
├── database/
│ ├── db\_connection.py
│ ├── agent\_db.py
│ └── mission\_db.py
├── README.md
├── requirements.txt
└── .gitignore


## מבנה הטבלאות



### טבלת הסוכנים


| field | type | notes |
| :---- | :---- | :---- |
| id | int ,auto_increment ,primary_key | מזהה ייחודי |
| name | varchar | שם הסוכן |
| specialty | varchar | תחום התמחות |
| is\_active | boolean | default : True |
| completed\_missions | int | default : 0 |
| failed\_missions | int | default : 0 |
| agent\_rank | enum / varchar | only : junior / senior / commander |



### טבלת משימות


| field | type | notes |
| :---- | :---- | :---- |
| id | int ,auto\_increment, primary key | מזהה ייחודי |
| title | varchar | כותרת המשימה |
| description | text | תיאור מפורט |
| difficulty | int | מיקום |
| importance | int | 1-10 בלבד |
| status | varchar | default : new |
| risk\_level | varchar | מחושב אוטומטי |
| assigned\_agent\_id | int | NULL עד שיוך |
|      |     |      |



## הסבר על המחלקות


#### missionDB 


המחלקה אחראית על כל פעולות mql מול טבלת ה mission

| מתודה | תפקיד |
| :---- | :---- |
| creat\_mission(data) | יוצרת משמה חדשה ומחזירה את האובייקט |
| get\_all\_mission() | מחזירה את כל המשימות |
| assign_mission(m_id, a_id)  |  משייכת משימה לסוכן | 
| update_mission_status(id, status) | מחזירה משימות assigned / in\_progress של סוכן |
|count\_all\_missions() | סה"כ משימות |
| status_by_count(status) | סופר לפי סטטוס מסויים |
|count\_open\_missions() | סופר משימות פתוחות |
| count_critical_missions() | סופר משימות critial |
|get\_top\_agent | הסוכן עם ה copleted\_missions הגבוה ביותר  |
| | |


#### AgentDB


המחלקה אחראית על פעולות ה sql מול טבלת ה agents


| מתודה | תפקיד |
| :---- | :---- |
| agent_create(data) | יוצרת סוכן חדש ומחזירה את האובייקט של הסוכן |
| agents_all_get() | מחזירת את כל הסוכנים ברשימה |
| get_agent_by_id(id) | מחזירה סוכן לפי id |
| update_agent(id, data) | update לכל השורה (א"א לשנות id) |
| agent_deactivate(id) | מגדירה מצב סוכן ללא פעיל |
| completed_increment(id) | מעדכן את כמות המשימות שהושלמו |
| failed_increment(id) | מעדכן את הכמות המשימות שנכשלו |
| get_agent_performance(id) | מחזירה מילון עם המפתחות : succes\_rate, completed, failed, total |
|count\_active\_agents() | מחזיר את מספר הסוכנים הפעילים |



#### DB_connection


אחראית על החיבור ל sql

| מתודה | תפקיד | 
| :---- | :---- | 
| get\_connection() | מחזירה חיבור פעיל ל sql | 
| create\_database() | יוצרת את ה db_Intelligence אם הוא לא קיים |
| create\_table() | יוצרת את שתי הטבלאות אם הן לא קיימות |


#### חוקי המערכת 


| number | Rules |
| :---- | :---- |
| #1 | rank must be junior / senior / commander any other value raise error |
| #2 | difficulty and importance must be between 1 to 10 else error
| #3 | risk\_level  מחושב אוטומטית בעת יצירת משימה א"א ליצור אותו |
| #4 | agent is\_active = False c'ant accept mission |
| #5 | סוכן לא יכול להחזיק יותר מ 3 משימות פתוחות בו זמנית |
| #6 | if risk\_level = critial only commander agent cen accept the mission |
| #7 | ניתן לשייך רק משימה בסטטוס new לאחר שיוך status = ASSIGNED |
| #8 | ניתן להתחיל רק משימה בסטטוס ASSIGNED אחרי ש status = in\_progress |
| #9 | ניתן לסייים רק משימה  in\_progress ולשנות לסטטוס failed or completed |
| #10 | ניתן לסיים רק משימה בסטטוס new or assigned else error



## הרצת docker

`docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 \
 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0
`



## חלק 2

זה המבנה של היום ואתמול יחד

├── main.py 
├── database
├── routes/
│   ├── agent\_routes.py
│   ├── mission\_routes.py
│   └── report\_routes.py
├── logs/
│   └── app.log
├── README.md 
└── requirements.txt



## main.py


הוא מריץ את הקבצים הוא מפעיל את השרת מחבר את הראוטים 


## agent_routes.py

הוא אחראי על כל העיסוק בפועל עם הסוכן(ליצורתלהפעיל וכו')


| Method | Endpoint | Description |
|:---- | :---- | :---- |
| `post` | /agents | יצירת סוכן חדש |
| `get` | /agents | כל הסוכנים |
| `get` | /agents/{id} | סוכן לפי id |
| `put` | /agents/{id} | עדכון סוכן |
| `put` | /agents{id}/deactivate | השבתת סוכן |
| `get` | /agents{id}/performance | ביצועי סוכן |




## mission_routes.py

| Method | Endpoint | Description |
|:---- | :---- | :---- |
| `post` | /missions | יצירת משימה | 
| `get` | /missions | כל המשימות |
| `get` | /missions{id} |משימה לפי id |
| `put` | /missions{id}/assign/{agent_id} | שיוך לסוכן |
| `put` | /missions/{id}/start | התחלת משימה |
| `put` | /missions/{id}/complete | סיום בהצלחה |
| `put` | /missions/{id}/fail | סיום בכישלון | 
| `put` | /missions/{id}/cancel | ביטול משימה |





## report_routes.py

| Method | Endpoint | Description |
|:---- | :---- | :---- |
| `get` | /summary/reports | דוח כללי של המערכת | 
| `get` | /reports/missions-by-status | משימות לפי סטטוס |
| `get` | /reports/top-agent  | הסוכן המצטיין |


## בדיקות 

| בדיקה | שגיאה עם נכשל |
| :---- | :---- |
| המשימה קיימת | mission not found 404 |
| הסוכן קיים | Agent not found 404 |
| המשימה בסטטוס new | Mission not available 400 |
| הסוכן פעיל | Agent is not active 400 |
| פחות מ3 משמות פתוחות | Agent has reached maximum missions 400 |
| Commander הסוכן — CRITICAL אם | Only Commander can handle critical missons 400

## logging 


| מתי | רמה  |
| :---- | :---- |
| בתחילת הפעולה | INFO אומר איזה קובץ נקרא
| לפני פעולת sql | INFO אומר מה הולך לקרות בקובץ |
| אם קרתה שגיאה | ERROR ומה בדיוק קרה |
| אם הצליח | INFO שהצליח |


### פעולות הרצה

להתקין fastapi and uvicorn ומריצים uvicorn ex:app --reload (מה שכתוב זה בעצם שמריצים את הקובץ ואת הapp שלו וה reload זה לנוחות שלא נצטרך להריץ שוב ושוב)