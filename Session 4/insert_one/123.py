import pymongo
client =pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.c4e
a = {
    "title" : "Fix You",
    "author" : "ColdPlay",
    "content" : """When you try your best but you don't succeed 
When you get what you want but not what you need 
When you feel so tired but you can't sleep 
Stuck in reverse
When the tears come streaming down your face 
'Cause you lose something you can't replace 
When you love someone but it goes to waste 
What could it be worse?
Lights will guide you home 
And ignite your bones 
And I will try to fix you
But high up above or down below 
When you are too in love to let it show 
Oh but if you never try you'll never know 
Just what you're worth
Lights will guide you home 
And ignite your bones 
And I will try to fix you
Tears come streaming down your face
When you lose something you cannot replace
oh and tears come streaming down your face
And I
Tears streaming down your face
I promise you I will learn from all my mistakes
oh and the tears streaming down your face
And I
Lights will guide you home 
And ignite your bones 
And I will try to fix you
"""
}
db.posts.insert_one(a)
