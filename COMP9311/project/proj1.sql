-- comp9311 20T1 Project 1
--
-- MyMyUNSW Solutions


-- Q1:
create or replace view Q1(courseid, code)
as
select distinct courses.id as courseid, code
from courses, subjects, staff_roles, course_staff
where staff_roles.name = 'Course Tutor'
and course_staff.role = staff_roles.id
and courses.id = course_staff.course
and subjects.id = courses.subject
and code like 'LAWS%'
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q2:
create or replace view Q2(unswid,name,class_num)
as
select distinct buildings.unswid, buildings.name,
count (rooms) as num
from buildings, class_types,classes,rooms
where class_types.name = 'Lecture'
and classes.ctype = class_types.id
and rooms.id = classes.room
and buildings.id = rooms.building
group by buildings.unswid, buildings.name
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q3:
create or replace view Q3(classid, course, room)
as 
select distinct classes.id as classid, classes.course, classes.room
from classes, facilities, people, room_facilities, students, course_enrolments,rooms,courses
where facilities.description = 'Television monitor'
and room_facilities.facility = facilities.id
and rooms.id = room_facilities.room
and classes.room = rooms.id
and people.name = 'Craig Conlon'
and students.id = people.id
and course_enrolments.student = students.id
and courses.id = course_enrolments.course
and classes.course = courses.id
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q4:
create or replace view loc_stu_CR_COMP9311(unswid, name)
as
select people.unswid, people.name
from people, course_enrolments,students,courses, subjects
where course_enrolments.grade = 'CR'
and students.id = course_enrolments.student
and people.id = students.id
and students.stype = 'local'
and courses.id = course_enrolments.course
and subjects.id = courses.subject
and subjects.code = 'COMP9311' 
;

create or replace view loc_stu_CR_COMP9021(unswid, name)
as
select people.unswid, people.name
from people, course_enrolments,students,courses, subjects
where course_enrolments.grade = 'CR'
and students.id = course_enrolments.student
and people.id = students.id
and students.stype = 'local'
and courses.id = course_enrolments.course
and subjects.id = courses.subject
and subjects.code = 'COMP9021'
;

create or replace view Q4(unswid, name)
as 
select distinct loc_stu_CR_COMP9311.unswid, loc_stu_CR_COMP9311.name
from loc_stu_CR_COMP9311, loc_stu_CR_COMP9021
where loc_stu_CR_COMP9311.unswid =  loc_stu_CR_COMP9021.unswid
and loc_stu_CR_COMP9311.name =  loc_stu_CR_COMP9021.name
;
--... SQL statements, possibly using other views/functions defined by you ...
;

--Q5:
create or replace view not_null(id)
as
select course_enrolments.student
from course_enrolments
where course_enrolments is not null
;

create or replace view every_average(id,avg)
as
select not_null.id, 
avg(mark)
from not_null, course_enrolments, students
where course_enrolments.student = not_null.id
and students.id = course_enrolments.student
group by not_null.id
; 

create or replace view average(avg)
as
select avg(every_average.avg)
from every_average
;

create or replace view Q5(num_student)
as
select count(*)
from average, every_average
where every_average.avg > average.avg
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q6:
create or replace view every_course_student(semester, id, num)
as 
select semesters.longname as semester, courses.id,
count(student) as num
from semesters, courses, course_enrolments
where  semesters.id = courses.semester
and courses.id = course_enrolments.course
group by semesters.longname, courses.id
having count(student) > 10
;

create or replace view max_num(semester, maxnum)
as
select every_course_student.semester,
max(every_course_student.num) as maxnum
from every_course_student
group by every_course_student.semester
;

create or replace view Q6(semester, max_num_student)
as
select max_num.semester, max_num.maxnum as max_num_student
from max_num
where max_num.maxnum = (select min(max_num.maxnum) from max_num)
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q7:
create or replace view Q7(course, avgmark,semester)
as
select courses.id as course, avg(mark) :: numeric(4,2) as avgmark,semesters.name as semester
from courses,semesters,course_enrolments
where courses.id = course_enrolments.course
and semesters.id = courses.semester
and semesters.year in (2009,2010)
group by courses.id, semesters.name
having count(course_enrolments.mark) >= 20
and avg(course_enrolments.mark) > 80
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q8: 
create or replace view students_law(unswid)
as
select distinct people.unswid
from students,people,streams,semesters,program_enrolments,stream_enrolments
where students.stype = 'local'
and people.id = students.id
and streams.name = 'Law'
and semesters.year = '2008'
and program_enrolments.semester = semesters.id
and students.id = program_enrolments.student
and stream_enrolments.stream = streams.id
and program_enrolments.id = stream_enrolments.partOf
;

create or replace view student_enroll(unswid)
as
select distinct people.unswid
from people, orgunits,students, subjects, courses,course_enrolments
where students.stype = 'local'
and people.id = students.id
and subjects.offeredby = orgunits.id
and courses.subject = subjects.id
and course_enrolments.course = courses.id
and students.id = course_enrolments.student
and orgunits.name = 'Accounting'
or
students.stype = 'local'
and people.id = students.id
and subjects.offeredby = orgunits.id
and courses.subject = subjects.id
and course_enrolments.course = courses.id
and students.id = course_enrolments.student
and orgunits.name = 'Economics'
;

create or replace view Q8(num)
as
select count(*) as num
from 
(select students_law.unswid from students_law 
except 
select student_enroll.unswid from student_enroll)
as students_except
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q9:
create or replace view subject(id,year,term)
as
select subjects.id,semesters.year,semesters.term
from subjects,semesters,courses
where subjects.code like 'COMP9%'
and semesters.year between 2002 and 2013
and courses.semester = semesters.id
and subjects.id = courses.subject
;

create or replace view year(year)
as
select distinct semesters.year
from semesters
where semesters.year between 2002 and 2013
;

create or replace view term(term)
as
select distinct semesters.term
from semesters
where semesters.term = 'S1'
or semesters.term = 'S2'
;

create or replace view popular_subject_term(id,term)
as
select distinct A.id, A.term
from subject A
where not exists
(select B.year 
from year B
where not exists
(select * 
from subject C
where C.id = A.id
and C.term = A.term
and C.year = B.year))
;

create or replace view popular_subject(id)
as
select distinct A.id
from popular_subject_term A
where not exists
(select B.term
from term B
where not exists
(select *
from popular_subject_term C
where C.id = A.id
and C.term = B.term))
;

create or replace view student_popular_subject(unswid,name,id)
as
select distinct people.unswid, people.name, subjects.id as id
from people, popular_subject, subjects, courses, course_enrolments,students
where course_enrolments.grade in ('HD','DN')
and course_enrolments.student = students.id
and people.id = students.id
and courses.id = course_enrolments.course
and subjects.id = courses.subject
and popular_subject.id = subjects.id
;

create or replace view Q9(unswid, name)
as
select distinct A.unswid,A.name
from student_popular_subject A
where not exists
(select B.id 
from popular_subject B
where not exists
(select * 
from student_popular_subject C
where C.unswid = A.unswid
and C.name = A.name
and C.id = B.id))
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q10:
create or replace view room_need(unswid,longname)
as
select distinct rooms.unswid, rooms.longname
from rooms,room_types
where room_types.description = 'Lecture Theatre'
and rooms.rtype = room_types.id
;

create or replace view class_use(unswid,longname,num)
as
select distinct rooms.unswid, rooms.longname,
count(rooms.unswid) as num
from rooms,room_types,classes,courses,semesters
where room_types.description = 'Lecture Theatre'
and rooms.rtype = room_types.id
and semesters.year = 2010
and semesters.term = 'S2'
and courses.semester = semesters.id
and classes.course = courses.id
and rooms.id = classes.room
group by rooms.unswid, rooms.longname
order by num desc
;

create or replace view no_use_room(unswid,longname,num)
as
select distinct zero_room.unswid, zero_room.longname, 0 as num
from (select room_need.unswid, room_need.longname from room_need
except
select class_use.unswid,class_use.longname from class_use)
as zero_room
;

create or replace view Q10(unswid, longname, num, rank)
as
select all_room.unswid,all_room.longname,num, rank() over (order by num desc) as rank
from (select * from class_use
union
select * from no_use_room) as all_room
;
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q11:
create or replace view BSc_pass(unswid,name)
as
select distinct people.unswid,people.name
from people,course_enrolments,students,semesters,courses,program_degrees, program_enrolments,programs
where program_degrees.abbrev = 'BSc'
and programs.id = program_degrees.program
and program_enrolments.program = programs.id
and students.id = program_enrolments.student
and people.id = students.id
and course_enrolments.mark >= 50
and semesters.year = 2010
and semesters.term = 'S2'
and courses.semester = semesters.id
and course_enrolments.course = courses.id
and students.id = course_enrolments.student
;

create or replace view avg_80(unswid,name)
as
select distinct people.unswid, people.name
from BSc_pass,people,course_enrolments,courses,program_enrolments,semesters,students
where BSc_pass.unswid = people.unswid
and students.id = course_enrolments.student
and people.id = students.id
and course_enrolments.course = courses.id
and courses.semester = semesters.id
and semesters.id = program_enrolments.semester
and program_enrolments.student = students.id
and students.id = course_enrolments.student
and courses.semester = semesters.id
and semesters.year < 2011 
and course_enrolments.mark >= 50
group by people.unswid,people.name
having avg(mark)>=80
;

create or replace view Q11(unswid,name)
as
select people.unswid,people.name
from people, avg_80,semesters,course_enrolments,students,courses,programs,subjects,program_enrolments
where semesters.year < 2011
and course_enrolments.mark > 50
and people.unswid = avg_80.unswid
and students.id = course_enrolments.student
and people.id = students.id
and course_enrolments.course = courses.id
and courses.semester = semesters.id
and semesters.id = program_enrolments.semester
and subjects.id = courses.subject
and program_enrolments.student = students.id
and students.id = course_enrolments.student
and program_enrolments.program = programs.id
group by people.unswid,people.name, programs.uoc
having sum(subjects.uoc) >= programs.uoc
; 
--... SQL statements, possibly using other views/functions defined by you ...
;

-- Q12:
create or replace view student_MSc_fail(unswid, name, program, uoc)
as
select distinct people.unswid,people.name,programs.name as program,
sum(subjects.uoc) as uoc
from people, program_enrolments,program_degrees,students,subjects,programs,course_enrolments,semesters,courses
where cast(people.unswid as char(20)) like '329%'
and program_degrees.abbrev = 'MSc'
and course_enrolments.mark >=0
and courses.subject = subjects.id
and people.id = students.id
and courses.id = course_enrolments.course
and students.id = course_enrolments.student
and program_enrolments.student = students.id
and programs.id = program_degrees.program
and program_enrolments.program = programs.id
and courses.semester = semesters.id
and semesters.id = program_enrolments.semester
and course_enrolments.mark between 0 and 49
group by people.unswid,people.name,programs.name,subjects.uoc
;

create or replace view good(unswid,name,program,acacdmic_standing)
as
select distinct student_MSc_fail.unswid, student_MSc_fail.name,student_MSc_fail.program,'Good' as acacdmic_standing
from student_MSc_fail
where student_MSc_fail.uoc < 12
;

create or replace view probation(unswid,name,program,acacdmic_standing)
as
select distinct student_MSc_fail.unswid, student_MSc_fail.name,student_MSc_fail.program,'Probation' as acacdmic_standing
from student_MSc_fail
where student_MSc_fail.uoc between 12 and 18
;

create or replace view exclusion(unswid,name,program,acacdmic_standing)
as
select distinct student_MSc_fail.unswid, student_MSc_fail.name,student_MSc_fail.program,'Exclusion' as acacdmic_standing
from student_MSc_fail
where student_MSc_fail.uoc > 18
;

create or replace view student_MSc(unswid, name, program)
as
select distinct people.unswid,people.name,programs.name as program
from people, program_enrolments,program_degrees,students,programs,course_enrolments,semesters,courses
where cast(people.unswid as char(20)) like '329%'
and program_degrees.abbrev = 'MSc'
and course_enrolments.mark > 0
and people.id = students.id
and courses.id = course_enrolments.course
and students.id = course_enrolments.student
and program_enrolments.student = students.id
and programs.id = program_degrees.program
and program_enrolments.program = programs.id
and courses.semester = semesters.id
and semesters.id = program_enrolments.semester
;

create or replace view student_MSc_notfail(unswid, name, program,acacdmic_standing)
as
select distinct unswid,name,program,'Good' as acacdmic_standing
from ((select * from student_MSc)
except
(select unswid,name,program from student_MSc_fail)) as notfail
;

create or replace view Q12(unswid, name, program,acacdmic_standing)
as
select * from
(select * from good
union
select * from probation
union
select * from exclusion
union
select * from student_MSc_notfail) as all_standing
;
--... SQL statements, possibly using other views/functions defined by you ...
;
