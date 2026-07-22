// ===============================
// HANDS-ON 5
// MongoDB - CRUD & Aggregation
// ===============================

// Step 60
use college_nosql

// Step 61
db.createCollection("feedback")

// Step 62
db.feedback.insertMany([
{
student_id:1,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent teaching",
tags:["challenging","well-structured"],
attachments:[{filename:"notes.pdf",size_kb:240}]
},
{
student_id:2,
course_code:"CS101",
semester:"2022-ODD",
rating:4,
comments:"Very Good",
tags:["challenging","good-examples"],
attachments:[{filename:"db.pdf",size_kb:120}]
},
{
student_id:3,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent",
tags:["challenging"],
attachments:[{filename:"algo.pdf",size_kb:200}]
},
{
student_id:4,
course_code:"CS102",
semester:"2022-ODD",
rating:3,
comments:"Average",
tags:["database"],
attachments:[{filename:"sql.pdf",size_kb:150}]
},
{
student_id:5,
course_code:"CS102",
semester:"2022-ODD",
rating:2,
comments:"Needs Improvement",
tags:["hard"],
attachments:[{filename:"lab.pdf",size_kb:180}]
},
{
student_id:6,
course_code:"ME101",
semester:"2022-ODD",
rating:4,
comments:"Good",
tags:["mechanical"],
attachments:[{filename:"me.pdf",size_kb:130}]
},
{
student_id:7,
course_code:"EC101",
semester:"2022-ODD",
rating:5,
comments:"Excellent",
tags:["electronics"],
attachments:[{filename:"ec.pdf",size_kb:220}]
},
{
student_id:8,
course_code:"CS103",
semester:"2022-ODD",
rating:4,
comments:"Nice",
tags:["oop"],
attachments:[{filename:"oop.pdf",size_kb:175}]
},
{
student_id:9,
course_code:"CS103",
semester:"2021-EVEN",
rating:2,
comments:"Difficult",
tags:["coding"],
attachments:[{filename:"code.pdf",size_kb:160}]
},
{
student_id:10,
course_code:"CS101",
semester:"2021-EVEN",
rating:5,
comments:"Very Good",
tags:["challenging"],
attachments:[{filename:"extra.pdf",size_kb:190}]
}
])

// Step 63
db.feedback.insertOne({
student_id:11,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"No attachment document"
})

// Step 64
db.feedback.countDocuments()

// Step 65
db.feedback.find({rating:5})

// Step 66
db.feedback.find({
course_code:"CS101",
tags:"challenging"
})

// Step 67
db.feedback.find(
{},
{
student_id:1,
course_code:1,
rating:1,
_id:0
}
)

// Step 68
db.feedback.updateMany(
{rating:{$lt:3}},
{$set:{needs_review:true}}
)

// Step 69
db.feedback.updateMany(
{needs_review:true},
{$push:{tags:"reviewed"}}
)

// Step 70
db.feedback.deleteMany({
semester:"2021-EVEN"
})

// Step 71
db.feedback.aggregate([
{$match:{semester:"2022-ODD"}},
{$group:{
_id:"$course_code",
avg_rating:{$avg:"$rating"},
total_feedback:{$sum:1}
}},
{$sort:{avg_rating:-1}}
])

// Step 72
db.feedback.aggregate([
{$match:{semester:"2022-ODD"}},
{$group:{
_id:"$course_code",
avg_rating:{$avg:"$rating"},
total_feedback:{$sum:1}
}},
{$project:{
course_code:"$_id",
average_rating:{$round:["$avg_rating",1]},
total_feedback:1,
_id:0
}},
{$sort:{average_rating:-1}}
])

// Step 73
db.feedback.aggregate([
{$unwind:"$tags"},
{$group:{
_id:"$tags",
count:{$sum:1}
}},
{$sort:{count:-1}}
])

// Step 74
db.feedback.createIndex({course_code:1})

db.feedback.find({
course_code:"CS101"
}).explain("executionStats")