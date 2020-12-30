// !requires! >>>>>>>
const express             = require("express"),
	app                   = express(),
	bodyParser            = require("body-parser"),
	mongoose              = require('mongoose'),
    {spawn}                 = require('child_process'),
	methodOverride        = require("method-override");
// <<<<<<<< !requires!

// !setup! >>>>>>>>>>

// set mongoose up
mongoose.set('useFindAndModify', false);
mongoose.connect('mongodb://localhost:27017/yelp_camp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to DB!'))
.catch(error => console.log(error.message));

// set body parser and view engine
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(methodOverride("_method"));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
// <<<<<<<<<< !setup!

app.get("/", (req, res) => res.send("<h1>this is the bungee API!</h1>"))

app.post('/init', (req, res) => {

	var NumPlayers = req.body.players

    const pyProg = spawn('python', ['./usingAPIFiles/startGame.py', NumPlayers]);
	
    pyProg.stdout.on('data', function(data) {
		
        console.log(data.toString());
        res.send(data.toString());
    });
})

app.listen(1010, () => console.log("server is running on port 1010"));