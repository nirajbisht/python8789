

const jwt = require('jsonwebtoken');
let verify = { 
 userVerify:  (req,res,next)=>{
 
    jwt.verify(req.headers.token,'bisht', function(err, result) {
    if(err)
    {
        res.send({response_code:500,
        response_message:"token mot match"})
    }
    else
    {
        
        next();
    }
})
}
}
module.exports =verify;

const router = require('express').Router();
const user = require('../webservices/userController');
const auth=require('../authantication/userverify');

router.post('/signup',user.signup);
router.post('/login',user.login);
router.post('/userList',auth.userVerify,user.userList);
router.post('/userprofile',auth.userVerify,user.userprofile);
router.post('/deleteUser',auth.userVerify,user.deleteUser);
router.post('/mail',user.mail);
router.post('/forgetPassword',user.forgetPassword);
router.post('/resetPassword',auth.userVerify,user.resetPassword);
router.post('/mobOtp',auth.userVerify,user.mobOtp);
router.post('/verifyOtp',auth.userVerify,user.verifyOtp);
// router.post('/verifyToken',user.verifyToken);

module.exports = router;

const mongoose = require('mongoose');
const Schema = mongoose.Schema;
var mongoosePaginate = require('mongoose-paginate');
const prodSchema = new Schema({
	name:{
	type:String
	},
	categaryID: { type: Schema.Types.ObjectId, ref: 'Category'},
	Sub_categaryID: { type: Schema.Types.ObjectId,ref: 'Category'}

});
prodSchema.plugin(mongoosePaginate);
module.exports = mongoose.model('Product',prodSchema);


var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var multer=require('multer');
app.use(bodyParser.json({limit: '50mb'}))
app.use(bodyParser.urlencoded({extended: true}))

const path = require('path');

var port = process.env.PORT || 8080;

var storage = multer.diskStorage({
  destination: './upload/',
  filename: function (req, file, cb) {
    cb(null, file.fieldname + '-' + Date.now()+path.extname(file.originalname));
  }
});
var upload = multer({ storage: storage }).single('thakur');
app.use('/',express.static(path.join(__dirname,'/upload')));

app.post('/profile', function (req, res) {

  upload(req, res, function (err) {

    if (err) {

    respponseMesage:"error"
    }
    console.log(req.file);

    res.send({
    
    	respponseMesage:"imageup loaded"
    });

  })
})

app.listen(port, ()=>{
console.log('project listning on http://localhost:'+port);
});


var express = require("express")
var mongoose = require("mongoose")
var bodyParser = require("body-parser")
var app = express()
var socket = require('socket.io');
var http = require("http").Server(app)
var io = require("socket.io")(http)
var conString = "mongodb://localhost:27017/myData";
app.use(express.static(__dirname))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
const Schema = mongoose.Schema;


var Chats = mongoose.model("Chats", {
    name: { type: String },
    chat: { type: String },
    email: {type:String}
   
})

var onlineUsers = {};
var sockets = {};
var allClients = [];


mongoose.connect(conString, (err) => {
    console.log("Database connection established successfully")
})
io.on('connection', function (socket) {
     allClients.push(socket.id);

     console.log('new user connected ', socket.id);
     console.log("online user are", allClients)
      console.log("socket", sockets)

    socket.on('init', (data) => {
       
       var data=JSON.parse(JSON.stringify(data));
     
        console.log("init data",data)
        Chats.find({ "email": data.email }, (err, result) => {

            console.log('existing user or not==>>', result);
            if (err) {

            } else if (result.length == 0) {
                var chat = new Chats(data);
                chat.save((error, result2) => {
                    if (error) {
                        res.send({ response_code: 404, response_message: "Internal server error" })
                    } else {
                        onlineUsers[result2._id] = { data: result2, socketId: socket.id }
                        sockets[socket.id] = socket;
                        socket.emit('init', result2)
                        console.log(result2);
                        console.log(onlineUsers);
                    }
                })
            } else {
                Chats.findByIdAndUpdate({ "_id": result[0]._id },data, (err1, result1) => {
                    
                    onlineUsers[result1._id] = { data: result1, socketId: socket.id }
                    sockets[socket.id] = socket;
                    socket.emit('init', result1)
                    console.log(result1);
                    console.log('onlineUsers', onlineUsers);
                    console.log('sockets', sockets);                
                })
            }
        
        })
    })

    socket.on("message", (data) =>{
        data=JSON.parse(JSON.stringify(data));
        console.log('onlineUsers', onlineUsers);
        console.log('sockets', sockets);
        console.log("reciver id",data.reciever)
        console.log(onlineUsers[data.reciever].socketId)
       io.to(onlineUsers[data.reciever].socketId).emit('message', data);
    })
    socket.on('disconnect', (socketss)=> {
        var socketID=socket.id
      console.log('Got disconnect!', socketID);
      var i = allClients.indexOf(socket);
            allClients.splice(i, 1);
      console.log(allClients)
     delete sockets[socketID]
      console.log(socketID)
      console.log("bshvsdhjbvsd",sockets)
   });

})
var server = http.listen(8000, () => {
    console.log("I am listening on ", server.address().port)
})


"mail":(req, res)=>{
	console.log(`request for login is ${JSON.stringify(req.body)}`)

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'neerajbisht54321@gmail.com',
    pass: '9411593846'
  }
});

var mailOptions = {
  from: 'neerajbisht54321@gmail.com',
  to: 'shivangikitians@gmail.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
},
"forgetPassword":(req, res)=>{
	console.log(`request for login is ${JSON.stringify(req.body)}`)
	User.findOne({"email":req.body.email},(error,result)=>{
		if(error)
		{
			res.send({response_code:500,response_message:"Internal server error."})
		}else if(!result){
			res.send({response_code:401,response_message:"User doesn't exist."})
		}else{
			 var t=(Math.random().toString().slice(2,8));
			
                               var newPassword = bcrypt.hashSync(t, salt);
			 User.updateOne({"email":req.body.email},{"$set":{"password":newPassword}},(error,result)=>{
		if(error)

			{
			res.send({response_code:500,response_message:"Internal server error."})
			}
		else
		{
		 // User.updateOne({"email":req.body.email},{"$set":{"password":t}})
			 var transporter = nodemailer.createTransport({
				  service: 'gmail',
				  auth: {
				    user: 'neerajbisht54321@gmail.com',
				    pass: '9411593846'
				  }
				});

				var mailOptions = {
				  from: 'neerajbisht54321@gmail.com',
				  to: req.body.email,
				  subject: 'Sending Email using Node.js',
				  text: "your new password is="+t
				};

				transporter.sendMail(mailOptions, function(error, info){
				  if (error) {
				    console.log(error);
				  } else {
				    console.log('Email sent: ' + info.response);
				    res.send({response_code:200,
								data:result,
								response_message:"new password sent to register mail id "})
				  }
				});
			}
		})
	}

})
},
"resetPassword":(req, res)=>{
	console.log(`request for login is ${JSON.stringify(req.body)}`)
	 req.body.oldPassword = bcrypt.hashSync(req.body.oldPassword, salt);
	  req.body.newPassword = bcrypt.hashSync(req.body.newPassword, salt);
	User.findOne({"_id":req.body._id,"password":req.body.oldPassword},(error,result)=>{
		if(error)
		{
			res.send({response_code:500,response_message:"Internal server error."})
		}else if(!result)
		{
			res.send({response_code:401,response_message:"invalid user and password"})
		}else
		{
			 User.updateOne({"_id":req.body._id},{"$set":{"password":req.body.newPassword}},(error,result)=>{
		if(error)

			{
			res.send({response_code:500,response_message:"Internal server error."})
			}
		else if(!result)
		{
			 res.send({response_code:401,
								data:result,
								response_message:" user not found"})
		}
			else
			{
				res.send({response_code:401,
								data:result,
								response_message:" password update successfully"})
			}
		})

}
})
},
"mobOtp":(req,res)=>{
			{
				 var t=(Math.random().toString().slice(2,6));
				 User.updateOne({"_id":req.body._id},{"$set":{"otp":t}},(error,result)=>{
					if(error)
					{
						res.send({response_code:500,response_message:"Internal server error."})
					}
					else if(!result)
					{
						res.send({response_code:401,
						data:result,
						response_message:" user not found"})
					}
					
				})
				client.messages.create({
					to:'+917409556844',
					from:'+18312267822',
					body:t
				},function(err,data)
				{
					if (err)
					{	console.log(err);
						res.send({response_code:400,
						response_message:" Internal error"})
					}
					else
					{
						res.send({response_code:200,
						response_message:" Otp  send successfully"})
					}
			}) 
		}
	},


    const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');


app.use(cors())

mongoose.connect('mongodb://localhost:27017/MyDB',{useNewUrlParser:true});

app.use(bodyParser.json({
	limit:"50mb"
}));

app.use(bodyParser.urlencoded({
	extended:false
}))

app.use('', require('./routes/userRoutes'));
app.use('/api/v1/emp', require('./routes/empRoutes'));

app.listen(8000,()=>{
	console.log(`Server is listen on 8000`)
})